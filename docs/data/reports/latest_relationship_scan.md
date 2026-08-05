# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T15:52:34.688056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11668`

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

- `market_context_high->unknown_24h` score `13.3997` n `90` status `ready` deltaP `6.875` edge `1.0751` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.5217` n `98` status `ready` deltaP `1.2226` edge `0.4682` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5315` n `98` status `ready` deltaP `16.2083` edge `0.1042` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.008` n `90` status `ready` deltaP `25.5903` edge `0.0792` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9273` n `90` status `ready` deltaP `2.0139` edge `0.2223` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4426` n `101` status `ready` deltaP `7.6332` edge `0.0276` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0502` n `101` status `ready` deltaP `5.1802` edge `-0.0037` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0561` n `98` status `ready` deltaP `10.8014` edge `0.0068` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5614` n `101` status `ready` deltaP `-2.2233` edge `-0.0077` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7057` n `101` status `ready` deltaP `-2.5464` edge `-0.0201` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8569` n `98` status `ready` deltaP `1.7266` edge `0.0021` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.4078` n `90` status `ready` deltaP `0.9027` edge `-0.0422` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5758` n `101` status `ready` deltaP `-5.3195` edge `-0.0248` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.6849` n `98` status `ready` deltaP `-2.0284` edge `-0.0635` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7848` n `101` status `ready` deltaP `2.7376` edge `-0.0935` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9882` n `98` status `ready` deltaP `-10.8232` edge `-0.0573` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.567` n `90` status `ready` deltaP `-11.5973` edge `-0.0323` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1675` n `101` status `ready` deltaP `5.0305` edge `-0.2528` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5523` n `101` status `ready` deltaP `-12.434` edge `-0.0758` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0421` n `90` status `ready` deltaP `10.8334` edge `-0.0254` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
