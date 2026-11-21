# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T19:37:27.543650+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2640`

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

- `market_context_high->unknown_1h` score `9986.4629` n `126` status `ready` deltaP `1.1643` edge `832.2173` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6037.5097` n `126` status `ready` deltaP `-0.9243` edge `503.1625` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.302` n `126` status `ready` deltaP `2.3049` edge `0.0124` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3949` n `126` status `ready` deltaP `1.2118` edge `0.0025` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8823` n `126` status `ready` deltaP `6.7653` edge `0.0224` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4525` n `126` status `ready` deltaP `-9.5547` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1679` n `126` status `ready` deltaP `3.2934` edge `0.0033` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4356` n `126` status `ready` deltaP `-10.0181` edge `-0.023` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8106` n `126` status `ready` deltaP `-7.7574` edge `-0.0192` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2882` n `126` status `ready` deltaP `-0.2852` edge `-0.0403` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9211` n `126` status `ready` deltaP `-6.4395` edge `-0.0561` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.3726` n `126` status `ready` deltaP `-5.9863` edge `-0.0842` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4378` n `126` status `ready` deltaP `-12.996` edge `-0.0039` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.1279` n `126` status `ready` deltaP `-21.4068` edge `-0.082` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.91` n `126` status `ready` deltaP `6.3492` edge `0.1081` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.5231` n `126` status `ready` deltaP `-6.4436` edge `-0.1527` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.7462` n `126` status `ready` deltaP `14.1865` edge `0.3313` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8087` n `126` status `ready` deltaP `-26.1409` edge `-0.116` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.9668` n `126` status `ready` deltaP `3.2986` edge `0.0492` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
