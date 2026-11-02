"""The public validator must ignore a worktree's .git pointer and nothing else."""

from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate_public_repo.sh"
BASH = shutil.which("bash")
# Built from parts so this file does not trip the scanner it tests.
HOME = "/" + "Users/someone/"


def run(tree, path=None):
    env = dict(os.environ)
    if path is not None:
        env["PATH"] = path
    return subprocess.run([BASH, str(tree / "scripts/validate_public_repo.sh")],
                          capture_output=True, text=True, env=env)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tree = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tree)
        (self.tree / "scripts").mkdir()
        shutil.copy(SCRIPT, self.tree / "scripts")
        (self.tree / "README.md").write_text("A clean public file.\n")
        self.assertIsNotNone(shutil.which("rg"), "ripgrep is required to run the validator")

    def write(self, rel, body):
        target = self.tree / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body)

    def test_worktree_git_pointer_is_not_published_content(self):
        self.write(".git", f"gitdir: {HOME}repo/.git/worktrees/wt\n")
        result = run(self.tree)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_absolute_path_in_published_file_still_fails(self):
        self.write(".git", f"gitdir: {HOME}repo/.git/worktrees/wt\n")
        self.write("knowledge/note.md", f"Open {HOME}private/file.md\n")
        result = run(self.tree)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("local absolute paths remain", result.stderr)

    def test_nested_git_named_file_is_still_scanned(self):
        self.write("docs/.git", f"gitdir: {HOME}elsewhere\n")
        result = run(self.tree)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("local absolute paths remain", result.stderr)

    def test_unapproved_partner_name_still_fails(self):
        self.write("knowledge/deck.md", "Partner: " + "Master" + "card\n")
        result = run(self.tree)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unapproved partner names remain", result.stderr)

    def test_missing_ripgrep_fails_instead_of_passing(self):
        bin_dir = self.tree / "bin-without-rg"
        bin_dir.mkdir()
        for tool in ("dirname", "node"):
            found = shutil.which(tool)
            if found:
                (bin_dir / tool).symlink_to(found)
        self.write("knowledge/note.md", f"Open {HOME}private/file.md\n")
        result = run(self.tree, path=str(bin_dir))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ripgrep", result.stderr)


if __name__ == "__main__":
    unittest.main()
