# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T00:22:28.475313+00:00`
- Price records: `672`
- Market context records: `6555`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `market_context_high->unknown_24h` score `6.3979` n `144` status `ready` deltaP `11.8934` edge `0.7839` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.8211` n `207` status `ready` deltaP `-5.1202` edge `0.276` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3478` n `144` status `ready` deltaP `13.1307` edge `0.2116` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.3882` n `196` status `ready` deltaP `11.7004` edge `0.0258` maxDD `-0.7164`
- `market_context_high->crypto_alt_4h` score `-0.1267` n `196` status `ready` deltaP `8.7264` edge `0.1025` maxDD `-8.0324`
- `market_context_high->equity_4h` score `-0.3824` n `196` status `ready` deltaP `9.893` edge `0.0549` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.3843` n `207` status `ready` deltaP `0.3847` edge `-0.0011` maxDD `-0.7249`
- `market_context_high->crypto_major_4h` score `-0.5193` n `196` status `ready` deltaP `11.1716` edge `0.088` maxDD `-12.6576`
- `market_context_high->crypto_major_1h` score `-0.5244` n `207` status `ready` deltaP `6.474` edge `0.0162` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5564` n `207` status `ready` deltaP `6.1883` edge `0.0187` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5716` n `207` status `ready` deltaP `-0.7246` edge `0.0035` maxDD `-0.7564`
- `market_context_high->equity_1h` score `-0.7509` n `207` status `ready` deltaP `2.0922` edge `0.0008` maxDD `-4.2147`
- `market_context_high->commodity_1h` score `-0.8887` n `207` status `ready` deltaP `-0.1873` edge `-0.0045` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.9655` n `196` status `ready` deltaP `-17.0079` edge `0.2735` maxDD `-10.5788`
- `market_context_high->metal_4h` score `-1.2113` n `196` status `ready` deltaP `0.8306` edge `0.035` maxDD `-2.6662`
- `market_context_high->metal_1h` score `-1.2599` n `207` status `ready` deltaP `-3.446` edge `-0.0013` maxDD `-2.1239`
- `market_context_high->metal_24h` score `-1.9805` n `144` status `ready` deltaP `5.966` edge `0.0882` maxDD `-5.7746`
- `market_context_high->commodity_4h` score `-2.0371` n `196` status `ready` deltaP `-1.3471` edge `-0.0113` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-3.025` n `196` status `ready` deltaP `-3.3256` edge `-0.0087` maxDD `-3.3635`
- `market_context_high->fx_24h` score `-3.8682` n `144` status `ready` deltaP `-5.1343` edge `-0.0082` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
