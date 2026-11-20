# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T23:37:29.982487+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2736`

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

- `market_context_high->unknown_1h` score `10128.6581` n `126` status `ready` deltaP `1.314` edge `844.0659` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6171.2217` n `126` status `ready` deltaP `-0.3145` edge `514.3011` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.3515` n `108` status `ready` deltaP `26.794` edge `1.0578` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.2288` n `126` status `ready` deltaP `3.3528` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2835` n `126` status `ready` deltaP `3.1579` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5123` n `126` status `ready` deltaP `11.7958` edge `0.0363` maxDD `-10.1161`
- `market_context_high->crypto_alt_24h` score `-0.9931` n `108` status `ready` deltaP `13.8311` edge `0.8151` maxDD `-72.5383`
- `market_context_high->fx_1h` score `-1.3711` n `126` status `ready` deltaP `-8.5068` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.9246` n `126` status `ready` deltaP `5.0898` edge `0.0116` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9887` n `126` status `ready` deltaP `-7.9462` edge `-0.0004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2619` n `126` status `ready` deltaP `-7.9223` edge `-0.0225` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.29` n `126` status `ready` deltaP `-2.2696` edge `-0.0124` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5507` n `126` status `ready` deltaP `2.4094` edge `0.0032` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2891` n `126` status `ready` deltaP `-4.0443` edge `-0.0194` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.3442` n `126` status `ready` deltaP `0.1113` edge `0.1352` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.6798` n `108` status `ready` deltaP `12.963` edge `0.1296` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.8885` n `108` status `ready` deltaP `-20.2546` edge `-0.0117` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.0186` n `126` status `ready` deltaP `-20.3397` edge `-0.08` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.4544` n `126` status `ready` deltaP `0.4161` edge `0.0573` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.9444` n `108` status `ready` deltaP `-26.3888` edge `-0.1398` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
