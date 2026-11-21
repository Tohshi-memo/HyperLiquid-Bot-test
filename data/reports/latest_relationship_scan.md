# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T12:07:22.521517+00:00`
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

- `market_context_high->unknown_1h` score `10021.2377` n `126` status `ready` deltaP `1.0146` edge `835.1162` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6099.8709` n `126` status `ready` deltaP `-0.3145` edge `508.3552` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1743` n `126` status `ready` deltaP `4.4007` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3077` n `126` status `ready` deltaP `2.7088` edge `0.0037` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5723` n `126` status `ready` deltaP `10.8812` edge `0.0347` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4525` n `126` status `ready` deltaP `-9.5547` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8191` n `126` status `ready` deltaP `5.988` edge `0.0144` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8765` n `126` status `ready` deltaP `-6.1169` edge `0.0018` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2308` n `126` status `ready` deltaP `-7.6229` edge `-0.0219` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.5005` n `126` status `ready` deltaP `-4.5562` edge `-0.0147` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.6298` n `126` status `ready` deltaP `2.11` edge `-0.0014` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.3358` n `126` status `ready` deltaP `-4.4934` edge `-0.0203` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.7118` n `126` status `ready` deltaP `-2.0229` edge `0.1023` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4212` n `120` status `ready` deltaP `-13.75` edge `-0.0063` maxDD `-6.3041`
- `market_context_high->commodity_4h` score `-6.8626` n `126` status `ready` deltaP `-18.5104` edge `-0.0792` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.0452` n `120` status `ready` deltaP `9.757` edge `0.1131` maxDD `-50.5532`
- `market_context_high->crypto_alt_4h` score `-8.0864` n `126` status `ready` deltaP `-3.09` edge `0.028` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-9.0465` n `120` status `ready` deltaP `20.0347` edge `0.5238` maxDD `-134.7068`
- `market_context_high->crypto_alt_24h` score `-12.3959` n `120` status `ready` deltaP `8.6459` edge `0.2408` maxDD `-140.3457`
- `market_context_high->index_24h` score `-14.3086` n `120` status `ready` deltaP `-26.9444` edge `-0.1223` maxDD `-37.903`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
