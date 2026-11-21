# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T09:52:28.808342+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2674`

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

- `market_context_high->unknown_1h` score `10035.0077` n `126` status `ready` deltaP `1.0146` edge `836.2637` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6117.8613` n `126` status `ready` deltaP `-0.3145` edge `509.8544` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1657` n `126` status `ready` deltaP `4.5504` edge `0.0149` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2991` n `126` status `ready` deltaP `2.8585` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5146` n `126` status `ready` deltaP `11.7958` edge `0.036` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4034` n `126` status `ready` deltaP `-8.9559` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7868` n `126` status `ready` deltaP `6.2874` edge `0.0151` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8828` n `126` status `ready` deltaP `-6.2693` edge `0.002` maxDD `-1.794`
- `market_context_high->crypto_major_24h` score `-2.0849` n `113` status `ready` deltaP `23.8032` edge `0.8248` maxDD `-91.7294`
- `market_context_high->commodity_1h` score `-2.2044` n `126` status `ready` deltaP `-7.3235` edge `-0.0217` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.4225` n `126` status `ready` deltaP `-3.6416` edge `-0.0143` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5543` n `126` status `ready` deltaP `2.5591` edge `0.0019` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.277` n `126` status `ready` deltaP `-4.194` edge `-0.0174` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.4343` n `126` status `ready` deltaP `-1.2607` edge `0.1328` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-6.3173` n `113` status `ready` deltaP `11.254` edge `0.1153` maxDD `-47.3418`
- `market_context_high->fx_24h` score `-6.4053` n `113` status `ready` deltaP `-14.4865` edge `-0.0066` maxDD `-5.7814`
- `market_context_high->commodity_4h` score `-6.809` n `126` status `ready` deltaP `-17.9007` edge `-0.0788` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.6965` n `126` status `ready` deltaP `-2.1753` edge `0.0544` maxDD `-46.5016`
- `market_context_high->crypto_alt_24h` score `-9.676` n `113` status `ready` deltaP `11.5367` edge `0.5026` maxDD `-102.5341`
- `market_context_high->index_24h` score `-13.3552` n `113` status `ready` deltaP `-26.6347` edge `-0.1176` maxDD `-34.4216`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
