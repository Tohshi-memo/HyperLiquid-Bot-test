# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T03:52:17.597579+00:00`
- Price records: `672`
- Market context records: `2208`
- Flow alert records: `8248`
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

- `market_context_high->crypto_alt_4h` score `12.7955` n `132` status `ready` deltaP `36.8441` edge `0.9143` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7741` n `132` status `ready` deltaP `42.2811` edge `0.7523` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4599` n `132` status `ready` deltaP `21.3738` edge `0.3804` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8174` n `43` status `ready` deltaP `31.7002` edge `0.3452` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4134` n `132` status `ready` deltaP `23.4156` edge `0.2378` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2003` n `132` status `ready` deltaP `17.4152` edge `0.1983` maxDD `-1.817`
- `market_context_high->index_4h` score `3.199` n `132` status `ready` deltaP `26.3165` edge `0.1595` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9411` n `132` status `ready` deltaP `15.9091` edge `0.2254` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.9359` n `132` status `ready` deltaP `26.7677` edge `0.5477` maxDD `-32.8525`
- `market_context_high->index_24h` score `2.3159` n `132` status `ready` deltaP `10.3851` edge `0.2466` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.2012` n `43` status `ready` deltaP `27.8892` edge `0.0159` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.8126` n `132` status `ready` deltaP `17.803` edge `0.9419` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4443` n `43` status `ready` deltaP `21.3445` edge `0.025` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.2963` n `43` status `ready` deltaP `14.4675` edge `0.0839` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.2723` n `132` status `ready` deltaP `16.6759` edge `0.1336` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.2363` n `43` status `ready` deltaP `-3.2934` edge `0.3012` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7736` n `43` status `ready` deltaP `11.0639` edge `0.0934` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2908` n `132` status `ready` deltaP `9.041` edge `0.0428` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.1628` n `43` status `ready` deltaP `4.4075` edge `0.0435` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
