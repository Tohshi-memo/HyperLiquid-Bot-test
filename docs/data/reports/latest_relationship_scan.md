# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T11:37:35.031725+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2602`

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

- `market_context_high->unknown_1h` score `10021.2353` n `126` status `ready` deltaP `1.0146` edge `835.116` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6099.9405` n `126` status `ready` deltaP `-0.3145` edge `508.361` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1735` n `126` status `ready` deltaP `4.4007` edge `0.0149` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2999` n `126` status `ready` deltaP `2.8585` edge `0.0037` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5534` n `126` status `ready` deltaP `11.1861` edge `0.0351` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4406` n `126` status `ready` deltaP `-9.405` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7904` n `126` status `ready` deltaP `6.2874` edge `0.0148` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8757` n `126` status `ready` deltaP `-6.1169` edge `0.0019` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2044` n `126` status `ready` deltaP `-7.3235` edge `-0.0217` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.4749` n `126` status `ready` deltaP `-4.2513` edge `-0.0146` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5914` n `126` status `ready` deltaP `2.2597` edge `0.0008` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.3142` n `126` status `ready` deltaP `-4.3437` edge `-0.0195` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.6141` n `126` status `ready` deltaP `-1.718` edge `0.1128` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4526` n `120` status `ready` deltaP `-14.0973` edge `-0.0066` maxDD `-6.3041`
- `market_context_high->commodity_4h` score `-6.8358` n `126` status `ready` deltaP `-18.2055` edge `-0.079` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.0464` n `120` status `ready` deltaP `9.757` edge `0.113` maxDD `-50.5532`
- `market_context_high->crypto_alt_4h` score `-7.9588` n `126` status `ready` deltaP `-2.7851` edge `0.0366` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-9.0855` n `120` status `ready` deltaP `20.0347` edge `0.5188` maxDD `-134.7068`
- `market_context_high->crypto_alt_24h` score `-12.4099` n `120` status `ready` deltaP `8.6459` edge `0.239` maxDD `-140.3457`
- `market_context_high->index_24h` score `-14.3242` n `120` status `ready` deltaP `-26.9444` edge `-0.1236` maxDD `-37.903`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
