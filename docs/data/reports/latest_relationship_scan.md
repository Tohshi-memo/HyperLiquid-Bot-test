# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T05:37:20.225291+00:00`
- Price records: `672`
- Market context records: `2216`
- Flow alert records: `8270`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9197`

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

- `market_context_high->crypto_alt_4h` score `13.0163` n `132` status `ready` deltaP `37.7587` edge `0.9266` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8853` n `132` status `ready` deltaP `42.8908` edge `0.7575` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5189` n `132` status `ready` deltaP `21.5263` edge `0.3843` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8624` n `43` status `ready` deltaP `32.3099` edge `0.3469` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.423` n `132` status `ready` deltaP `23.4156` edge `0.2386` maxDD `-5.0894`
- `market_context_high->index_4h` score `3.2306` n `132` status `ready` deltaP `26.6214` edge `0.1601` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.2147` n `132` status `ready` deltaP `17.4152` edge `0.1995` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.9986` n `132` status `ready` deltaP `16.2085` edge `0.2282` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.4451` n `132` status `ready` deltaP `25.5524` edge `0.5149` maxDD `-32.8525`
- `news_risk_high->fx_4h` score `2.234` n `43` status `ready` deltaP `28.1941` edge `0.0166` maxDD `-0.1382`
- `market_context_high->index_24h` score `2.0295` n `132` status `ready` deltaP `9.8642` edge `0.2262` maxDD `-4.1604`
- `news_risk_high->unknown_1h` score `1.5127` n `43` status `ready` deltaP `21.7936` edge `0.0277` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3553` n `43` status `ready` deltaP `14.62` edge `0.0878` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.3401` n `132` status `ready` deltaP `17.1332` edge `0.1362` maxDD `-4.7664`
- `market_context_high->crypto_major_24h` score `1.3337` n `132` status `ready` deltaP `16.5877` edge `0.8886` maxDD `-60.2561`
- `news_risk_high->equity_4h` score `1.2425` n `43` status `ready` deltaP `-3.2934` edge `0.302` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7346` n `43` status `ready` deltaP `10.4651` edge `0.0924` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4897` n `43` status `ready` deltaP `8.4389` edge `0.0102` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2728` n `132` status `ready` deltaP `9.041` edge `0.0413` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.1511` n `43` status `ready` deltaP `4.4075` edge `0.042` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
