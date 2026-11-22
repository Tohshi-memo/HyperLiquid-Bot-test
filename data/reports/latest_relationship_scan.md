# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T01:52:36.218335+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4574`

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

- `market_context_high->unknown_1h` score `9786.2214` n `126` status `ready` deltaP `0.8649` edge `815.5325` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `5858.3873` n `126` status `ready` deltaP `-0.6194` edge `488.2336` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.3152` n `126` status `ready` deltaP `2.3049` edge `0.0107` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4852` n `126` status `ready` deltaP `-0.4349` edge `0.0019` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9128` n `126` status `ready` deltaP `6.6129` edge `0.0195` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3915` n `126` status `ready` deltaP `-8.8062` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8614` n `126` status `ready` deltaP `-5.812` edge `0.0017` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.3314` n `126` status `ready` deltaP `-8.8205` edge `-0.0223` maxDD `-4.3877`
- `market_context_high->equity_1h` score `-2.3489` n `126` status `ready` deltaP `1.7964` edge `-0.0018` maxDD `-13.1399`
- `market_context_high->index_4h` score `-2.9443` n `126` status `ready` deltaP `-9.1294` edge `-0.0212` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.6421` n `126` status `ready` deltaP `-1.1834` edge `-0.0638` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.2377` n `126` status `ready` deltaP `-7.6371` edge `-0.0745` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.0637` n `126` status `ready` deltaP `-8.8294` edge `-0.0005` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.4349` n `126` status `ready` deltaP `-5.8339` edge `-0.0932` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-6.9942` n `126` status `ready` deltaP `-20.0348` edge `-0.08` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.9864` n `126` status `ready` deltaP `4.9603` edge `0.111` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.4221` n `126` status `ready` deltaP `-6.2912` edge `-0.1453` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.7145` n `126` status `ready` deltaP `13.4921` edge `0.34` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8387` n `126` status `ready` deltaP `-26.1409` edge `-0.1185` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.5529` n `126` status `ready` deltaP `3.4722` edge `0.1011` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
