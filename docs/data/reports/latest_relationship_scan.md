# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T09:52:29.333923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4288`

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

- `market_context_high->unknown_1h` score `12066.3835` n `106` status `ready` deltaP `0.2061` edge `1005.5504` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7547.1175` n `106` status `ready` deltaP `-2.1169` edge `628.9711` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.3277` n `106` status `ready` deltaP `2.4545` edge `0.0081` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3915` n `106` status `ready` deltaP `2.141` edge `0.0018` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1388` n `106` status `ready` deltaP `-7.5783` edge `-0.0014` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.51` n `106` status `ready` deltaP `-0.0115` edge `0.0037` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8293` n `106` status `ready` deltaP `2.9347` edge `-0.0431` maxDD `-13.8788`
- `market_context_high->equity_1h` score `-1.9579` n `106` status `ready` deltaP `6.4682` edge `-0.0087` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.0873` n `106` status `ready` deltaP `1.5416` edge `-0.0036` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.5045` n `106` status `ready` deltaP `-11.1117` edge `-0.0271` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.429` n `106` status `ready` deltaP `-13.6274` edge `-0.0316` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.7344` n `106` status `ready` deltaP `-5.361` edge `-0.0644` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-4.8989` n `106` status `ready` deltaP `-8.3432` edge `-0.0033` maxDD `-5.9453`
- `market_context_high->commodity_4h` score `-6.782` n `106` status `ready` deltaP `-17.2688` edge `-0.0904` maxDD `-14.7712`
- `market_context_high->metal_24h` score `-10.2841` n `106` status `ready` deltaP `-9.3913` edge `0.0152` maxDD `-52.1012`
- `market_context_high->crypto_major_4h` score `-11.383` n `106` status `ready` deltaP `-8.968` edge `-0.1959` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-11.5671` n `106` status `ready` deltaP `-9.5777` edge `-0.2188` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.7337` n `106` status `ready` deltaP `-27.8335` edge `-0.3575` maxDD `-62.4905`
- `market_context_high->crypto_major_24h` score `-15.8278` n `106` status `ready` deltaP `7.0951` edge `-0.0165` maxDD `-152.134`
- `market_context_high->index_24h` score `-16.1463` n `106` status `ready` deltaP `-33.3333` edge `-0.1837` maxDD `-39.8349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
