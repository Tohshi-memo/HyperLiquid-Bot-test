# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T07:52:32.216657+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4552`

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

- `market_context_high->unknown_1h` score `11269.6272` n `112` status `ready` deltaP `0.8126` edge `939.15` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6977.2263` n `112` status `ready` deltaP `-1.6115` edge `581.4768` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2078` n `112` status `ready` deltaP `4.3413` edge `0.0109` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3002` n `112` status `ready` deltaP `3.133` edge `0.0028` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.286` n `112` status `ready` deltaP `-9.351` edge `-0.0017` maxDD `-0.4504`
- `market_context_high->crypto_major_1h` score `-1.4285` n `112` status `ready` deltaP `3.8762` edge `0.002` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.6358` n `112` status `ready` deltaP `-1.9817` edge `0.0026` maxDD `-1.5956`
- `market_context_high->metal_4h` score `-1.7138` n `112` status `ready` deltaP `4.7256` edge `0.0063` maxDD `-10.1161`
- `market_context_high->equity_1h` score `-1.7167` n `112` status `ready` deltaP `7.3086` edge `0.0058` maxDD `-13.1399`
- `market_context_high->crypto_alt_1h` score `-2.2244` n `112` status `ready` deltaP `-4.7583` edge `-0.0424` maxDD `-13.8848`
- `market_context_high->commodity_1h` score `-2.4577` n `112` status `ready` deltaP `-10.1048` edge `-0.0253` maxDD `-4.3051`
- `market_context_high->index_4h` score `-3.0881` n `112` status `ready` deltaP `-10.1917` edge `-0.0261` maxDD `-7.0639`
- `market_context_high->fx_24h` score `-5.1934` n `112` status `ready` deltaP `-7.7629` edge `-0.0022` maxDD `-6.3066`
- `market_context_high->commodity_4h` score `-6.7782` n `112` status `ready` deltaP `-17.4652` edge `-0.0858` maxDD `-15.0091`
- `market_context_high->metal_24h` score `-9.5103` n `112` status `ready` deltaP `-4.489` edge `0.047` maxDD `-52.1012`
- `market_context_high->crypto_major_4h` score `-9.5699` n `112` status `ready` deltaP `-5.6838` edge `-0.0667` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-10.1941` n `112` status `ready` deltaP `-6.1411` edge `-0.1273` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.9284` n `112` status `ready` deltaP `-27.4554` edge `-0.3409` maxDD `-64.0175`
- `market_context_high->crypto_major_24h` score `-14.5168` n `112` status `ready` deltaP `9.6726` edge `0.1344` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.6818` n `112` status `ready` deltaP `-30.8532` edge `-0.1614` maxDD `-39.8449`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
