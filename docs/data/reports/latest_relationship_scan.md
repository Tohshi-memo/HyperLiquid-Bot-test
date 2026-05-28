# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T21:07:25.907309+00:00`
- Price records: `672`
- Market context records: `2178`
- Flow alert records: `8164`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.7203` n `132` status `ready` deltaP `36.2343` edge `0.9121` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7847` n `132` status `ready` deltaP `42.1286` edge `0.7542` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.6015` n `132` status `ready` deltaP `22.2885` edge `0.3861` maxDD `-2.4317`
- `market_context_high->unknown_24h` score `3.8499` n `132` status `ready` deltaP `29.3719` edge `0.6065` maxDD `-32.8525`
- `news_risk_high->commodity_4h` score `3.8018` n `43` status `ready` deltaP `31.7002` edge `0.3432` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.5812` n `132` status `ready` deltaP `24.1778` edge `0.2467` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2326` n `132` status `ready` deltaP `17.7146` edge `0.199` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.9362` n `132` status `ready` deltaP `16.0588` edge `0.224` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `2.8909` n `132` status `ready` deltaP `21.2752` edge `1.057` maxDD `-60.2561`
- `market_context_high->index_4h` score `2.7587` n `132` status `ready` deltaP `22.658` edge `0.1472` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.612` n `132` status `ready` deltaP `10.9059` edge `0.2678` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1696` n `43` status `ready` deltaP `27.5843` edge `0.0153` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.8359` n `132` status `ready` deltaP `23.548` edge `0.4806` maxDD `-33.1007`
- `market_context_high->metal_4h` score `1.4937` n `132` status `ready` deltaP `18.0478` edge `0.1429` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.4379` n `43` status `ready` deltaP `15.3822` edge `0.0896` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.4048` n `43` status `ready` deltaP `21.0451` edge `0.0237` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `1.3453` n `43` status `ready` deltaP `-2.5312` edge `0.3101` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.6957` n `43` status `ready` deltaP `10.016` edge `0.0904` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4633` n `43` status `ready` deltaP `8.1395` edge `0.01` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3328` n `132` status `ready` deltaP `9.3404` edge `0.0443` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
