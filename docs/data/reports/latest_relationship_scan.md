# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T00:22:36.507980+00:00`
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

- `market_context_high->unknown_1h` score `10126.2737` n `126` status `ready` deltaP `1.314` edge `843.8672` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6165.8517` n `126` status `ready` deltaP `-0.3145` edge `513.8536` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.2158` n `108` status `ready` deltaP `26.794` edge `1.0404` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.2288` n `126` status `ready` deltaP `3.3528` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2734` n `126` status `ready` deltaP `3.3076` edge `0.0041` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5415` n `126` status `ready` deltaP `11.3385` edge `0.0356` maxDD `-10.1161`
- `market_context_high->crypto_alt_24h` score `-1.2583` n `108` status `ready` deltaP `13.8311` edge `0.793` maxDD `-72.5383`
- `market_context_high->fx_1h` score `-1.3711` n `126` status `ready` deltaP `-8.5068` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.9042` n `126` status `ready` deltaP `5.2395` edge `0.0123` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.988` n `126` status `ready` deltaP `-7.9462` edge `-0.0003` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2248` n `126` status `ready` deltaP `-7.4732` edge `-0.0224` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3325` n `126` status `ready` deltaP `-2.727` edge `-0.0129` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5219` n `126` status `ready` deltaP `2.5591` edge `0.0046` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2327` n `126` status `ready` deltaP `-3.7449` edge `-0.0167` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.4468` n `126` status `ready` deltaP `-0.3461` edge `0.1251` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.6678` n `108` status `ready` deltaP `12.963` edge `0.1306` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.8571` n `108` status `ready` deltaP `-19.9074` edge `-0.0114` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.021` n `126` status `ready` deltaP `-20.3397` edge `-0.0802` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.6037` n `126` status `ready` deltaP `-0.0412` edge `0.0479` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.9108` n `108` status `ready` deltaP `-26.3888` edge `-0.137` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
