# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T04:07:23.090243+00:00`
- Price records: `672`
- Market context records: `2527`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

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

- `market_context_high->crypto_alt_4h` score `4.962` n `162` status `ready` deltaP `23.1595` edge `0.527` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.8275` n `119` status `ready` deltaP `19.548` edge `0.3048` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.4493` n `162` status `ready` deltaP `16.5368` edge `0.3582` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1833` n `119` status `ready` deltaP `11.6363` edge `0.5916` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.9622` n `162` status `ready` deltaP `11.2485` edge `0.1935` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0295` n `162` status `ready` deltaP `8.7344` edge `0.1463` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5938` n `162` status `ready` deltaP `7.6495` edge `0.1179` maxDD `-4.2199`
- `market_context_high->index_4h` score `-0.0042` n `162` status `ready` deltaP `7.2004` edge `0.0358` maxDD `-2.3986`
- `market_context_high->index_24h` score `-0.0582` n `119` status `ready` deltaP `3.1994` edge `0.0719` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0663` n `119` status `ready` deltaP `0.531` edge `0.6837` maxDD `-43.6595`
- `market_context_high->equity_24h` score `-0.3054` n `119` status `ready` deltaP `17.1379` edge `0.013` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3664` n `162` status `ready` deltaP `4.2083` edge `0.0128` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4255` n `162` status `ready` deltaP `1.2512` edge `0.0056` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4827` n `162` status `ready` deltaP `0.73` edge `0.0092` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.5428` n `162` status `ready` deltaP `0.6358` edge `0.004` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5924` n `162` status `ready` deltaP `1.5894` edge `0.012` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.7682` n `162` status `ready` deltaP `1.402` edge `0.0126` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.7898` n `162` status `ready` deltaP `0.2015` edge `0.0167` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8893` n `119` status `ready` deltaP `2.5589` edge `0.004` maxDD `-2.4729`
- `market_context_high->metal_4h` score `-0.9389` n `162` status `ready` deltaP `2.8663` edge `0.0414` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
