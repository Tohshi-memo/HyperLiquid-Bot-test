# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T03:37:15.583021+00:00`
- Price records: `672`
- Market context records: `2207`
- Flow alert records: `8245`
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

- `market_context_high->crypto_alt_4h` score `12.7617` n `132` status `ready` deltaP `36.6917` edge `0.9125` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7511` n `132` status `ready` deltaP `42.1286` edge `0.7514` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4647` n `132` status `ready` deltaP `21.3738` edge `0.3808` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.819` n `43` status `ready` deltaP `31.7002` edge `0.3454` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3964` n `132` status `ready` deltaP `23.2631` edge `0.2374` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2015` n `132` status `ready` deltaP `17.4152` edge `0.1984` maxDD `-1.817`
- `market_context_high->index_4h` score `3.1832` n `132` status `ready` deltaP `26.1641` edge `0.1592` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.9822` n `132` status `ready` deltaP `26.9413` edge `0.5504` maxDD `-32.8525`
- `market_context_high->crypto_alt_1h` score `2.9219` n `132` status `ready` deltaP `15.7594` edge `0.2248` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.361` n `132` status `ready` deltaP `10.5587` edge `0.2492` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.2` n `43` status `ready` deltaP `27.8892` edge `0.0158` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.877` n `132` status `ready` deltaP `17.9766` edge `0.949` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4587` n `43` status `ready` deltaP `21.4942` edge `0.0252` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3011` n `43` status `ready` deltaP `14.4675` edge `0.0843` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.2577` n `132` status `ready` deltaP `16.5235` edge `0.1334` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.2252` n `43` status `ready` deltaP `-3.4459` edge `0.3008` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7829` n `43` status `ready` deltaP `11.2136` edge `0.0936` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3088` n `132` status `ready` deltaP `9.1907` edge `0.0433` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.1745` n `43` status `ready` deltaP `4.5572` edge `0.044` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
