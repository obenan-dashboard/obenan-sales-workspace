# Obenan dashboard preview

**APPROVED for public sales reuse by Seven on 2026-11-03.** This is the supplied Obenan
dashboard teaser, not confidential customer footage. The earlier agent-created publication
hold is superseded by that explicit approval. See the exact scope in the
[public proof register](../../knowledge/proof/PUBLIC_PROOF_REGISTER.md#obenan-dashboard-preview).

[Watch or download the dashboard preview](https://raw.githubusercontent.com/obenan-dashboard/obenan-sales-workspace/main/assets/product-film/obenan-concept-film-720p.mp4).

The 67.6-second silent video, [poster](obenan-concept-film-poster.jpg) and
[QR](obenan-concept-film-qr.svg) are stored here. Ordinary coffee and fitness builds embed
them automatically, with a clickable poster, public link and QR in the PDF. No private file,
login, new provider or extra package installation is needed. See
[SALES_TOOLKIT.md](../../knowledge/engagement/SALES_TOOLKIT.md). Use `--no-film` to omit the
teaser when it does not answer the buyer's question. Banking remains film-free.

[DESCRIPTION.md](DESCRIPTION.md) is the scene by scene text alternative.

## Scope of the supplied footage

Frame review of the 1080p master on 1 November 2026 recorded the following content:

| Time | Content |
| --- | --- |
| About 12 to 15 s and 39 to 41 s | A business selector naming a real restaurant with a street address |
| About 22 to 30 s | A real hotel's name, street address and photograph |
| About 12 to 55 s | A photograph of a person as the signed-in user and in the chat |
| About 20 to 21 s | A grid of food photographs of unknown origin |
| 0 to 67 s | A song with vocals on the master's soundtrack |

Approval records Seven's authority to distribute this supplied sales asset, not independently
verified third-party licences or permission to extract its people, business identities or
figures as separate proof. Only the silent rendition is published; no soundtrack is included.
Do not infer current features, account state or customer performance from its illustrative screens.

## Public files

| File | Use | SHA-256 |
| --- | --- | --- |
| `obenan-concept-film-720p.mp4` | Web rendition, 1280x720 H.264, no audio, 67.6 s, 3,719,495 bytes | `1d1dc9d8120d892aedefb1418b6cf7596cf14c03513c5db7d8f9c7fcb4f1dee0` |
| `obenan-concept-film-poster.jpg` | Poster frame at 10 s and the PDF still | `52550d4b36da8a7f87efcce20089f52df582795677271ca035e446d0c2dd6cbe` |
| `obenan-concept-film-qr.svg` | QR for the public video URL above, not a loopback address | `e502080dc418b7e25626d6a7ed5076b9fc31d4ef11ba909b19f2b722f5b35142` |

The build refuses a rendition, poster or default QR whose checksum differs from this table.
The existing filenames remain stable for compatibility; the customer-facing name is
"Obenan dashboard preview". A custom approved address can use `--film-url URL`; generating
its QR requires the existing optional `qrcode` tool described in the toolkit guide.

Two source masters remain outside this repository; only the optimized silent rendition is
needed for reuse:

| Master | Format | Bytes | SHA-256 |
| --- | --- | --- | --- |
| Obenan V2 AI colleague | 1920x1080 H.264, 29.97 fps, AAC | 12,743,022 | `99d690e2953e0f7ddb2b960e999f9a9e86975635fa728b99a8ee5ec6bcd4e16a` |
| Obi-Gleb high quality | 3840x2160 H.264, about 8.8 Mbps | 77,105,136 | `d56eaf5ecccdf210f69130667f8236f285b2e65257e1f5bcdc99c8598ae595c1` |

Both masters are 67.5675 s and show the same picture. The rendition was made from the
1080p master. The 4K master never goes into this repository.

```bash
ffmpeg -i master-1080p.mp4 -an -vf scale=1280:-2 -c:v libx264 -profile:v high \
  -preset slow -crf 25 -pix_fmt yuv420p -movflags +faststart obenan-concept-film-720p.mp4
ffmpeg -ss 10 -i obenan-concept-film-720p.mp4 -frames:v 1 -q:v 3 obenan-concept-film-poster.jpg
```

## Labelling

Every page that shows the film labels it "Obenan dashboard preview". It shows the product,
not a deployment, a customer result or a live account. It uses legacy wave branding and
concept gauges; never quote a score or number from it. Built pages load it with
`preload="none"`, visible controls, a poster and no autoplay. PDFs show the poster, never
the video bytes.
