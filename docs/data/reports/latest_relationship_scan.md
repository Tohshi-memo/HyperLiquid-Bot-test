# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T16:37:27.416136+00:00`
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

- `market_context_high->unknown_24h` score `13.3215` n `90` status `ready` deltaP `6.5278` edge `1.0709` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.4989` n `98` status `ready` deltaP `1.2226` edge `0.4663` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5667` n `98` status `ready` deltaP `16.5132` edge `0.1051` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.9684` n `90` status `ready` deltaP `25.0695` edge `0.0776` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9406` n `90` status `ready` deltaP `2.0139` edge `0.224` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.5708` n `104` status `ready` deltaP `8.7402` edge `0.0309` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0565` n `104` status `ready` deltaP `6.4083` edge `-0.003` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0284` n `98` status `ready` deltaP `11.2588` edge `0.0073` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.633` n `104` status `ready` deltaP `-3.3164` edge `-0.0096` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7779` n `104` status `ready` deltaP `-3.8749` edge `-0.0205` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8294` n `98` status `ready` deltaP `2.0315` edge `0.0036` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.4086` n `90` status `ready` deltaP `0.9027` edge `-0.0423` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5077` n `104` status `ready` deltaP `-4.7674` edge `-0.0228` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.71` n `98` status `ready` deltaP `-2.1808` edge `-0.0657` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7893` n `104` status `ready` deltaP `2.1707` edge `-0.0903` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9929` n `98` status `ready` deltaP `-10.8232` edge `-0.0579` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5467` n `90` status `ready` deltaP `-11.5973` edge `-0.0297` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.3504` n `104` status `ready` deltaP `3.6734` edge `-0.259` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4144` n `104` status `ready` deltaP `-11.6248` edge `-0.0697` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0535` n `90` status `ready` deltaP `10.6598` edge `-0.0257` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
