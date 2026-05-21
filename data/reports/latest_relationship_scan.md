# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T16:22:21.626766+00:00`
- Price records: `672`
- Market context records: `1439`
- Flow alert records: `6057`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8797`

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

- `market_context_high->crypto_alt_24h` score `12.3209` n `154` status `ready` deltaP `28.7811` edge `1.0365` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.1263` n `154` status `ready` deltaP `13.5507` edge `1.0869` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6096` n `154` status `ready` deltaP `27.3539` edge `0.8983` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1469` n `154` status `ready` deltaP `19.3813` edge `0.325` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.5115` n `154` status `ready` deltaP `12.5271` edge `0.4418` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2546` n `212` status `ready` deltaP `6.5319` edge `0.144` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2032` n `154` status `ready` deltaP `10.4009` edge `0.0525` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1475` n `224` status `ready` deltaP `2.1492` edge `0.0334` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1649` n `224` status `ready` deltaP `3.3549` edge `0.0104` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.4822` n `224` status `ready` deltaP `0.5854` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6777` n `224` status `ready` deltaP `-0.5988` edge `0.009` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.6806` n `224` status `ready` deltaP `1.612` edge `0.0349` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.6942` n `212` status `ready` deltaP `-0.3682` edge `0.0535` maxDD `-3.7119`
- `market_context_high->crypto_alt_4h` score `-0.9523` n `212` status `ready` deltaP `9.1492` edge `0.1916` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.0671` n `212` status `ready` deltaP `-4.4926` edge `-0.0098` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.2177` n `212` status `ready` deltaP `5.042` edge `0.1358` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.2588` n `224` status `ready` deltaP `4.5873` edge `-0.0019` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.6267` n `212` status `ready` deltaP `5.856` edge `0.0216` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.681` n `224` status `ready` deltaP `-1.0639` edge `0.0027` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.1079` n `212` status `ready` deltaP `-10.2393` edge `-0.0194` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
