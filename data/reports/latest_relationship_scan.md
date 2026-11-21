# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T12:52:26.512121+00:00`
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

- `market_context_high->unknown_1h` score `10015.3397` n `126` status `ready` deltaP `1.0146` edge `834.6247` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6090.7939` n `126` status `ready` deltaP `-0.467` edge `507.5998` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1828` n `126` status `ready` deltaP `4.251` edge `0.0147` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3077` n `126` status `ready` deltaP `2.7088` edge `0.0037` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.6031` n `126` status `ready` deltaP `10.4239` edge `0.0338` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4286` n `126` status `ready` deltaP `-9.2553` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8467` n `126` status `ready` deltaP `5.6886` edge `0.0141` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8693` n `126` status `ready` deltaP `-5.9645` edge `0.0017` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2571` n `126` status `ready` deltaP `-7.9223` edge `-0.0221` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.5419` n `126` status `ready` deltaP `-5.0135` edge `-0.0151` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.6886` n `126` status `ready` deltaP `1.9603` edge `-0.0053` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.3778` n `126` status `ready` deltaP `-4.6431` edge `-0.0228` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.8971` n `126` status `ready` deltaP `-2.4802` edge `0.0816` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.406` n `121` status `ready` deltaP `-13.3394` edge `-0.0062` maxDD `-6.4295`
- `market_context_high->commodity_4h` score `-6.904` n `126` status `ready` deltaP `-18.9677` edge `-0.0796` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.1525` n `121` status `ready` deltaP `9.5572` edge `0.1137` maxDD `-50.8765`
- `market_context_high->crypto_alt_4h` score `-8.3438` n `126` status `ready` deltaP `-3.5473` edge `0.0096` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-9.6826` n `121` status `ready` deltaP `19.532` edge `0.5011` maxDD `-138.8141`
- `market_context_high->crypto_alt_24h` score `-13.0146` n `121` status `ready` deltaP `8.2602` edge `0.2168` maxDD `-144.233`
- `market_context_high->index_24h` score `-14.405` n `121` status `ready` deltaP `-26.9857` edge `-0.121` maxDD `-38.2941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
