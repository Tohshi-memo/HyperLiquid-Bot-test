# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T19:37:25.424947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `12.946` n `90` status `ready` deltaP `4.4445` edge `1.0535` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.3512` n `104` status `ready` deltaP `-1.6182` edge `0.3896` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5271` n `104` status `ready` deltaP `16.7683` edge `0.1001` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9164` n `90` status `ready` deltaP `2.0139` edge `0.2209` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8973` n `90` status `ready` deltaP `24.7223` edge `0.0708` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4323` n `109` status `ready` deltaP `7.7597` edge `0.0259` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0428` n `109` status `ready` deltaP `6.1322` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0525` n `104` status `ready` deltaP `10.6004` edge `0.0086` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5113` n `109` status `ready` deltaP `-1.2608` edge `-0.0077` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7838` n `104` status `ready` deltaP `2.6383` edge `0.0054` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.821` n `109` status `ready` deltaP `-4.5542` edge `-0.0215` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.4867` n `90` status `ready` deltaP `0.5555` edge `-0.05` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5853` n `109` status `ready` deltaP `-5.2876` edge `-0.0258` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.7056` n `104` status `ready` deltaP `-1.0318` edge `-0.0728` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.925` n `109` status `ready` deltaP `0.3709` edge `-0.0957` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.2115` n `104` status `ready` deltaP `-13.7078` edge `-0.0667` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.409` n `90` status `ready` deltaP `-10.2084` edge `-0.0213` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4602` n `109` status `ready` deltaP `-11.8978` edge `-0.0717` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6461` n `109` status `ready` deltaP `1.7332` edge `-0.2707` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0397` n `90` status `ready` deltaP `10.8334` edge `-0.0251` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
