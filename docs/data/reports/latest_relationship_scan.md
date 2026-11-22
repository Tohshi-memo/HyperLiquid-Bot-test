# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T05:37:26.862797+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4590`

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

- `market_context_high->unknown_1h` score `10244.796` n `121` status `ready` deltaP `0.9328` edge `853.7466` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6227.8314` n `121` status `ready` deltaP `-0.9474` edge `519.0228` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.294` n `121` status `ready` deltaP `4.3772` edge `0.0128` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4042` n `121` status `ready` deltaP `1.8323` edge `0.0028` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8386` n `121` status `ready` deltaP `7.9949` edge `0.0198` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4569` n `121` status `ready` deltaP `-9.5945` edge `-0.0015` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.7715` n `121` status `ready` deltaP `-4.1613` edge `0.0019` maxDD `-1.7685`
- `market_context_high->equity_1h` score `-1.8906` n `121` status `ready` deltaP `5.2098` edge `0.0053` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4192` n `121` status `ready` deltaP `-9.738` edge `-0.0235` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.7622` n `121` status `ready` deltaP `-6.9126` edge `-0.0208` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.8945` n `121` status `ready` deltaP `0.8561` edge `-0.0276` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.934` n `121` status `ready` deltaP `-7.3304` edge `-0.0554` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.5584` n `121` status `ready` deltaP `-3.2138` edge `0.0017` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-5.7155` n `121` status `ready` deltaP `-7.7838` edge `-0.0011` maxDD `-6.8641`
- `market_context_high->crypto_alt_4h` score `-6.1176` n `121` status `ready` deltaP `-3.3663` edge `-0.0806` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.9131` n `121` status `ready` deltaP `-18.9729` edge `-0.0814` maxDD `-15.4566`
- `market_context_high->metal_24h` score `-8.4725` n `121` status `ready` deltaP `1.7791` edge `0.0917` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.432` n `121` status `ready` deltaP `11.7539` edge `0.2596` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.2994` n `121` status `ready` deltaP `-29.4235` edge `-0.135` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-16.0793` n `121` status `ready` deltaP `2.8295` edge `0.0379` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
