# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T19:22:27.888981+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2800`

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

- `market_context_high->unknown_1h` score `10152.8861` n `126` status `ready` deltaP `1.4638` edge `846.0839` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6197.9853` n `126` status `ready` deltaP `-0.3145` edge `516.5314` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.6705` n `108` status `ready` deltaP `26.794` edge `1.0987` maxDD `-57.8734`
- `market_context_high->crypto_alt_24h` score `-0.0307` n `108` status `ready` deltaP `13.8311` edge `0.8953` maxDD `-72.5383`
- `market_context_high->metal_1h` score `-0.1665` n `126` status `ready` deltaP `4.4007` edge `0.0158` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2703` n `126` status `ready` deltaP `3.4573` edge `0.0035` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.505` n `126` status `ready` deltaP `12.1007` edge `0.0352` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4094` n `126` status `ready` deltaP `-8.9559` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7952` n `126` status `ready` deltaP `6.1377` edge `0.0154` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9903` n `126` status `ready` deltaP `-7.9462` edge `-0.0006` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2056` n `126` status `ready` deltaP `-7.4732` edge `-0.0208` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3781` n `126` status `ready` deltaP `-2.727` edge `-0.0167` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.3839` n `126` status `ready` deltaP `2.7088` edge `0.0151` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.0816` n `126` status `ready` deltaP `-3.2958` edge `-0.0071` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.1758` n `126` status `ready` deltaP `1.0259` edge `0.1507` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8982` n `108` status `ready` deltaP `12.963` edge `0.1114` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.7575` n `108` status `ready` deltaP `-18.6921` edge `-0.0112` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8536` n `126` status `ready` deltaP `-19.8824` edge `-0.0693` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.023` n `126` status `ready` deltaP `1.7881` edge `0.0841` maxDD `-46.5016`
- `market_context_high->index_24h` score `-13.1568` n `108` status `ready` deltaP `-26.3888` edge `-0.1575` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
