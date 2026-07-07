# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T14:07:32.264559+00:00`
- Price records: `672`
- Market context records: `5988`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.4726` n `30` status `ready` deltaP `68.4028` edge `0.1667` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.5286` n `30` status `ready` deltaP `33.8889` edge `0.172` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1287` n `30` status `ready` deltaP `42.7439` edge `0.0637` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2154` n `30` status `ready` deltaP `26.6267` edge `0.021` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0291` n `233` status `ready` deltaP `7.5905` edge `0.1446` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.792` n `30` status `ready` deltaP `9.8902` edge `0.0823` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1748` n `30` status `ready` deltaP `5.1697` edge `0.0341` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0703` n `30` status `ready` deltaP `9.2361` edge `0.0346` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4094` n `30` status `ready` deltaP `1.5369` edge `-0.0261` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4351` n `233` status `ready` deltaP `-1.0331` edge `0.0023` maxDD `-1.0955`
- `market_context_high->equity_1h` score `-0.4731` n `233` status `ready` deltaP `3.5087` edge `0.0288` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5802` n `233` status `ready` deltaP `1.4225` edge `-0.004` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.7696` n `233` status `ready` deltaP `-1.6422` edge `-0.0015` maxDD `-0.8015`
- `market_context_high->equity_24h` score `-0.869` n `206` status `ready` deltaP `21.7452` edge `0.3194` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0586` n `30` status `ready` deltaP `-9.7006` edge `-0.0196` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1441` n `233` status `ready` deltaP `2.3509` edge `0.0144` maxDD `-9.807`
- `market_context_high->index_1h` score `-1.16` n `233` status `ready` deltaP `-1.2027` edge `0.0027` maxDD `-1.3078`
- `market_context_high->index_4h` score `-1.1859` n `233` status `ready` deltaP `0.2545` edge `0.015` maxDD `-3.165`
- `market_context_high->commodity_4h` score `-1.2259` n `233` status `ready` deltaP `-0.4305` edge `-0.0019` maxDD `-4.8588`
- `market_context_high->crypto_alt_1h` score `-1.2413` n `233` status `ready` deltaP `1.2927` edge `0.0075` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
