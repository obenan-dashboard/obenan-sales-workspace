# Concept product film

Obenan's concept product film is **held privately**. No rendition, poster or QR is stored in
this public repository, and no public address for it exists yet. The toolkit teaser section
shows it only when a person supplies the reviewed rendition to the build (see
[SALES_TOOLKIT.md](../../knowledge/engagement/SALES_TOOLKIT.md)). Without it, the build
leaves the teaser section out.

[DESCRIPTION.md](DESCRIPTION.md) is the scene by scene text alternative.

## Why it is held

Frame review of the 1080p master on 1 November 2026 found third party content in most of
the product screens, so a short clean cut would not show the product:

| Time | Content |
| --- | --- |
| About 12 to 15 s and 39 to 41 s | A business selector naming a real restaurant with a street address |
| About 22 to 30 s | A real hotel's name, street address and photograph |
| About 12 to 55 s | A photograph of a person as the signed-in user and in the chat |
| About 20 to 21 s | A grid of food photographs of unknown origin |
| 0 to 67 s | A song with vocals on the master's soundtrack |

A disclaimer does not replace permission.

## Approval needed

Before the film is published or sent outside a meeting, Obenan needs, in writing:

1. The restaurant's consent to show its name and address, or a cut that removes it.
2. The hotel's consent to show its name, address and photograph, or a cut that removes it.
3. The pictured person's consent to show their photograph, or a cut that replaces it.
4. The origin and licence of the food photographs.
5. A licence for the soundtrack, or keep the film silent as the rendition is.
6. An approved public host and address for the film. No new storage provider is added here.

Once these are recorded, add the approved address to the build with `--film-url` so the PDF
carries a clickable poster, link and QR.

## Held files

| File | Use | SHA-256 |
| --- | --- | --- |
| `obenan-concept-film-720p.mp4` | Web rendition, 1280x720 H.264, no audio, 67.6 s, 3,719,495 bytes | `1d1dc9d8120d892aedefb1418b6cf7596cf14c03513c5db7d8f9c7fcb4f1dee0` |
| `obenan-concept-film-poster.jpg` | Poster frame at 10 s and the PDF still | `52550d4b36da8a7f87efcce20089f52df582795677271ca035e446d0c2dd6cbe` |

The build refuses a rendition or poster whose checksum differs from this table.

Two masters are held privately by Obenan:

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

Every page that shows the film labels it a historical concept film. It shows product ideas,
not a deployment, a customer result or a live account. It uses legacy wave branding and
concept gauges; never quote a score or number from it. Built pages load it with
`preload="none"`, visible controls, a poster and no autoplay. PDFs show the poster, never
the video bytes.
