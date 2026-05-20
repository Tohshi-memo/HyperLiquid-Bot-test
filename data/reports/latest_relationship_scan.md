# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T21:37:20.655479+00:00`
- Price records: `672`
- Market context records: `1359`
- Flow alert records: `5826`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_major_24h` score `13.3667` n `133` status `ready` deltaP `32.7576` edge `1.0087` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6846` n `133` status `ready` deltaP `12.7454` edge `1.1388` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.8087` n `133` status `ready` deltaP `28.4736` edge `0.8292` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1338` n `133` status `ready` deltaP `23.3279` edge `0.2976` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8701` n `133` status `ready` deltaP `16.2685` edge `0.3634` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3068` n `158` status `ready` deltaP `12.0041` edge `0.1827` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `1.357` n `133` status `ready` deltaP `-9.2966` edge `0.3802` maxDD `-11.411`
- `market_context_high->fx_24h` score `1.2666` n `133` status `ready` deltaP `14.3053` edge `0.0574` maxDD `-0.4441`
- `market_context_high->metal_4h` score `0.1648` n `158` status `ready` deltaP `12.9496` edge `0.0705` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.0375` n `170` status `ready` deltaP `2.869` edge `0.0286` maxDD `-1.9017`
- `market_context_high->index_1h` score `0.0263` n `170` status `ready` deltaP `4.8151` edge `0.0155` maxDD `-1.6329`
- `market_context_high->index_4h` score `0.0071` n `158` status `ready` deltaP `5.0556` edge `0.0761` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.1872` n `170` status `ready` deltaP `6.9743` edge `-0.0005` maxDD `-2.9326`
- `market_context_high->fx_1h` score `-0.3026` n `170` status `ready` deltaP `1.733` edge `-0.0039` maxDD `-0.3821`
- `market_context_high->commodity_1h` score `-0.5221` n `170` status `ready` deltaP `0.7168` edge `0.0132` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8189` n `170` status `ready` deltaP `-0.2237` edge `0.0203` maxDD `-3.6309`
- `market_context_high->unknown_24h` score `-1.1202` n `133` status `ready` deltaP `-4.2581` edge `0.208` maxDD `-10.1706`
- `market_context_high->crypto_major_1h` score `-1.1508` n `170` status `ready` deltaP `-3.422` edge `-0.0182` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.3064` n `158` status `ready` deltaP `8.3533` edge `0.1674` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.5458` n `158` status `ready` deltaP `1.4318` edge `0.0194` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
