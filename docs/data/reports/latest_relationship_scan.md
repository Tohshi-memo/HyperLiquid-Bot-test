# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T05:07:36.996028+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4576`

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

- `market_context_high->unknown_1h` score `10052.8508` n `123` status `ready` deltaP `1.1075` edge `837.75` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6070.6626` n `123` status `ready` deltaP `-0.813` edge `505.9245` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2016` n `123` status `ready` deltaP `4.2342` edge `0.0124` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4711` n `123` status `ready` deltaP `1.026` edge `0.0026` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8386` n `123` status `ready` deltaP `7.876` edge `0.0206` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3837` n `123` status `ready` deltaP `-8.7094` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.7959` n `123` status `ready` deltaP `-4.5732` edge `0.0018` maxDD `-1.7916`
- `market_context_high->equity_1h` score `-1.9583` n `123` status `ready` deltaP `4.3632` edge `0.0053` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3988` n `123` status `ready` deltaP `-9.5431` edge `-0.0231` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8137` n `123` status `ready` deltaP `-7.5711` edge `-0.0207` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.1096` n `123` status `ready` deltaP `0.0633` edge `-0.0319` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9798` n `123` status `ready` deltaP `-7.339` edge `-0.055` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.7516` n `123` status `ready` deltaP `-3.9126` edge `-0.0184` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-5.8389` n `123` status `ready` deltaP `-7.9988` edge `-0.0007` maxDD `-6.9375`
- `market_context_high->crypto_alt_4h` score `-6.2655` n `123` status `ready` deltaP `-4.0651` edge `-0.0949` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.9391` n `123` status `ready` deltaP `-19.3089` edge `-0.0805` maxDD `-15.5229`
- `market_context_high->metal_24h` score `-8.2566` n `123` status `ready` deltaP `3.0826` edge `0.101` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.1742` n `123` status `ready` deltaP `12.4662` edge `0.2879` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.0958` n `123` status `ready` deltaP `-27.8244` edge `-0.1287` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.8173` n `123` status `ready` deltaP `3.7432` edge `0.0654` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
