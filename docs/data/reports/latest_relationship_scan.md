# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T00:52:25.777586+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2624`

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

- `market_context_high->unknown_1h` score `12010.0544` n `108` status `ready` deltaP `1.1367` edge `1000.8501` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7456.6569` n `108` status `ready` deltaP `-0.0903` edge `621.4171` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `23.483` n `88` status `ready` deltaP `42.1559` edge `1.7352` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.9122` n `88` status `ready` deltaP `25.6156` edge `1.4957` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.7738` n `108` status `ready` deltaP `4.2457` edge `0.4014` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.1467` n `108` status `ready` deltaP `5.4652` edge `0.2667` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.7424` n `88` status `ready` deltaP `19.0656` edge `0.2436` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.5751` n `108` status `ready` deltaP `19.0888` edge `0.0551` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.189` n `108` status `ready` deltaP `5.0898` edge `0.0168` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2032` n `108` status `ready` deltaP `5.1453` edge `0.0793` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2538` n `108` status `ready` deltaP `3.4154` edge `0.0059` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.6919` n `108` status `ready` deltaP `-1.4859` edge `0.0434` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0295` n `108` status `ready` deltaP `7.0914` edge `0.0448` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6468` n `108` status `ready` deltaP `-11.8485` edge `-0.0023` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8212` n `108` status `ready` deltaP `-2.2245` edge `-0.0026` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.4163` n `108` status `ready` deltaP `-9.8193` edge `-0.0277` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.4198` n `108` status `ready` deltaP `-15.56` edge `-0.0049` maxDD `-1.794`
- `market_context_high->fx_24h` score `-7.3404` n `88` status `ready` deltaP `-25.6787` edge `-0.0132` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1248` n `108` status `ready` deltaP `-29.2626` edge `-0.1127` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.2695` n `108` status `ready` deltaP `-6.8992` edge `-0.0443` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
