# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T12:37:26.604492+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2584`

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

- `market_context_high->unknown_1h` score `10018.2197` n `126` status `ready` deltaP `1.0146` edge `834.8647` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6093.7831` n `126` status `ready` deltaP `-0.467` edge `507.8489` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.182` n `126` status `ready` deltaP `4.251` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3077` n `126` status `ready` deltaP `2.7088` edge `0.0037` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5929` n `126` status `ready` deltaP `10.5763` edge `0.0341` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4406` n `126` status `ready` deltaP `-9.405` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8335` n `126` status `ready` deltaP `5.8383` edge `0.0142` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8772` n `126` status `ready` deltaP `-6.1169` edge `0.0017` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2559` n `126` status `ready` deltaP `-7.9223` edge `-0.022` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.5273` n `126` status `ready` deltaP `-4.8611` edge `-0.0149` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.679` n `126` status `ready` deltaP `1.9603` edge `-0.0045` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.3706` n `126` status `ready` deltaP `-4.6431` edge `-0.0222` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.8408` n `126` status `ready` deltaP `-2.3278` edge `0.0878` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.3874` n `120` status `ready` deltaP `-13.4028` edge `-0.0058` maxDD `-6.3041`
- `market_context_high->commodity_4h` score `-6.8906` n `126` status `ready` deltaP `-18.8153` edge `-0.0795` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.0452` n `120` status `ready` deltaP `9.757` edge `0.1131` maxDD `-50.5532`
- `market_context_high->crypto_alt_4h` score `-8.2596` n `126` status `ready` deltaP `-3.3948` edge `0.0156` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-9.0207` n `120` status `ready` deltaP `20.0347` edge `0.5271` maxDD `-134.7068`
- `market_context_high->crypto_alt_24h` score `-12.3959` n `120` status `ready` deltaP `8.6459` edge `0.2408` maxDD `-140.3457`
- `market_context_high->index_24h` score `-14.293` n `120` status `ready` deltaP `-26.9444` edge `-0.121` maxDD `-37.903`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
