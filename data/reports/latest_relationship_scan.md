# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T08:22:25.408631+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4522`

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

- `market_context_high->unknown_1h` score `11527.9152` n `110` status `ready` deltaP `0.6178` edge `960.6753` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7163.2613` n `110` status `ready` deltaP `-1.7738` edge `596.9808` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2078` n `110` status `ready` deltaP `4.3413` edge `0.0109` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3096` n `110` status `ready` deltaP `3.0158` edge `0.0028` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.23` n `110` status `ready` deltaP `-8.6854` edge `-0.0016` maxDD `-0.4399`
- `market_context_high->crypto_major_1h` score `-1.3631` n `110` status `ready` deltaP `4.5346` edge `0.006` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.5933` n `110` status `ready` deltaP `-1.2999` edge `0.0029` maxDD `-1.5465`
- `market_context_high->equity_1h` score `-1.671` n `110` status `ready` deltaP `7.9994` edge `0.005` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-1.8292` n `110` status `ready` deltaP `3.7029` edge `0.0035` maxDD `-10.1161`
- `market_context_high->crypto_alt_1h` score `-2.1596` n `110` status `ready` deltaP `-4.2461` edge `-0.0375` maxDD `-13.8848`
- `market_context_high->commodity_1h` score `-2.4233` n `110` status `ready` deltaP `-9.7224` edge `-0.0254` maxDD `-4.2715`
- `market_context_high->index_4h` score `-3.1873` n `110` status `ready` deltaP `-11.1918` edge `-0.0277` maxDD `-7.0639`
- `market_context_high->fx_24h` score `-5.0859` n `110` status `ready` deltaP `-7.8503` edge `-0.0025` maxDD `-6.1856`
- `market_context_high->commodity_4h` score `-6.7642` n `110` status `ready` deltaP `-17.3642` edge `-0.0869` maxDD `-14.882`
- `market_context_high->metal_24h` score `-9.7575` n `110` status `ready` deltaP `-6.0637` edge `0.0369` maxDD `-52.1012`
- `market_context_high->crypto_major_4h` score `-10.0432` n `110` status `ready` deltaP `-6.6353` edge `-0.0998` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-10.5464` n `110` status `ready` deltaP `-7.245` edge `-0.1493` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.8591` n `110` status `ready` deltaP `-27.4779` edge `-0.3461` maxDD `-63.5449`
- `market_context_high->crypto_major_24h` score `-14.8508` n `110` status `ready` deltaP `8.8447` edge `0.0971` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.7847` n `110` status `ready` deltaP `-31.1679` edge `-0.168` maxDD `-39.8349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
