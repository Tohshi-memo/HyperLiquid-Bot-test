# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T01:52:16.464720+00:00`
- Price records: `672`
- Market context records: `2517`
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

- `market_context_high->unknown_24h` score `4.9943` n `119` status `ready` deltaP `19.548` edge `0.3187` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.7708` n `153` status `ready` deltaP `21.9392` edge `0.5192` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.7985` n `153` status `ready` deltaP `17.4517` edge `0.3812` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2509` n `119` status `ready` deltaP `11.8099` edge `0.5991` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0985` n `153` status `ready` deltaP `12.1124` edge `0.1991` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0535` n `162` status `ready` deltaP `8.5847` edge `0.1493` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6717` n `162` status `ready` deltaP `8.0986` edge `0.1214` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0009` n `119` status `ready` deltaP `0.8782` edge `0.69` maxDD `-43.6595`
- `market_context_high->index_24h` score `-0.0174` n `119` status `ready` deltaP `3.1994` edge `0.0753` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.139` n `153` status `ready` deltaP `6.6705` edge `0.0281` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.1574` n `119` status `ready` deltaP `17.8324` edge `0.0207` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3875` n `162` status `ready` deltaP `3.9089` edge `0.0121` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4315` n `162` status `ready` deltaP `0.9518` edge `0.0071` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.45` n `162` status `ready` deltaP `1.1791` edge `0.0104` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.4638` n `162` status `ready` deltaP `1.534` edge `0.0046` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5132` n `162` status `ready` deltaP `2.0385` edge `0.0156` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.8065` n `162` status `ready` deltaP `0.0518` edge `0.0163` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8183` n `119` status `ready` deltaP `3.7742` edge `0.005` maxDD `-2.4729`
- `market_context_high->fx_4h` score `-0.9062` n `153` status `ready` deltaP `-0.0219` edge `0.0106` maxDD `-0.8774`
- `market_context_high->commodity_4h` score `-0.9937` n `153` status `ready` deltaP `3.6406` edge `0.0426` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
