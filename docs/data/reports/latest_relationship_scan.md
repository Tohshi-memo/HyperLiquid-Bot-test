# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T12:22:26.633554+00:00`
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

- `market_context_high->unknown_1h` score `10021.1417` n `126` status `ready` deltaP `1.0146` edge `835.1082` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6096.8589` n `126` status `ready` deltaP `-0.3145` edge `508.1042` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1743` n `126` status `ready` deltaP `4.4007` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3077` n `126` status `ready` deltaP `2.7088` edge `0.0037` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5818` n `126` status `ready` deltaP `10.7288` edge `0.0345` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4525` n `126` status `ready` deltaP `-9.5547` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8215` n `126` status `ready` deltaP `5.988` edge `0.0142` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8772` n `126` status `ready` deltaP `-6.1169` edge `0.0017` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.244` n `126` status `ready` deltaP `-7.7726` edge `-0.022` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.5139` n `126` status `ready` deltaP `-4.7087` edge `-0.0148` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.6454` n `126` status `ready` deltaP `2.11` edge `-0.0027` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.3442` n `126` status `ready` deltaP `-4.4934` edge `-0.021` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.7673` n `126` status `ready` deltaP `-2.1753` edge `0.0962` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4049` n `120` status `ready` deltaP `-13.5764` edge `-0.0061` maxDD `-6.3041`
- `market_context_high->commodity_4h` score `-6.8772` n `126` status `ready` deltaP `-18.6629` edge `-0.0794` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.0452` n `120` status `ready` deltaP `9.757` edge `0.1131` maxDD `-50.5532`
- `market_context_high->crypto_alt_4h` score `-8.1574` n `126` status `ready` deltaP `-3.2424` edge `0.0231` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-9.0309` n `120` status `ready` deltaP `20.0347` edge `0.5258` maxDD `-134.7068`
- `market_context_high->crypto_alt_24h` score `-12.3928` n `120` status `ready` deltaP `8.6459` edge `0.2412` maxDD `-140.3457`
- `market_context_high->index_24h` score `-14.3002` n `120` status `ready` deltaP `-26.9444` edge `-0.1216` maxDD `-37.903`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
