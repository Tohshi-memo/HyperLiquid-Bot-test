# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T19:22:37.928827+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2646`

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

- `market_context_high->unknown_1h` score `9987.0413` n `126` status `ready` deltaP `1.1643` edge `832.2655` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6040.5541` n `126` status `ready` deltaP `-0.9243` edge `503.4162` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2942` n `126` status `ready` deltaP `2.4546` edge `0.0124` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3941` n `126` status `ready` deltaP `1.2118` edge `0.0026` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8705` n `126` status `ready` deltaP `6.9178` edge `0.0229` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4645` n `126` status `ready` deltaP `-9.7044` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1679` n `126` status `ready` deltaP `3.2934` edge `0.0033` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4224` n `126` status `ready` deltaP `-9.8684` edge `-0.0229` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8094` n `126` status `ready` deltaP `-7.7574` edge `-0.0191` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2715` n `126` status `ready` deltaP `-0.1355` edge `-0.0399` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9271` n `126` status `ready` deltaP `-6.4395` edge `-0.0566` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.3218` n `126` status `ready` deltaP `-5.8339` edge `-0.0787` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4541` n `126` status `ready` deltaP `-13.1697` edge `-0.0041` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.1279` n `126` status `ready` deltaP `-21.4068` edge `-0.082` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.8866` n `126` status `ready` deltaP `6.5228` edge `0.1089` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.4763` n `126` status `ready` deltaP `-6.4436` edge `-0.1488` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.6873` n `126` status `ready` deltaP `14.3601` edge `0.3377` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8051` n `126` status `ready` deltaP `-26.1409` edge `-0.1157` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.9281` n `126` status `ready` deltaP `3.4722` edge `0.053` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
