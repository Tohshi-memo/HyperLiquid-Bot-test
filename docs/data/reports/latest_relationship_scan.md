# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T02:37:29.501663+00:00`
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

- `market_context_high->unknown_1h` score `9788.3238` n `126` status `ready` deltaP `0.8649` edge `815.7077` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `5853.8849` n `126` status `ready` deltaP `-0.6194` edge `487.8584` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2981` n `126` status `ready` deltaP `2.6043` edge `0.0109` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4758` n `126` status `ready` deltaP `-0.2852` edge `0.0021` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8931` n `126` status `ready` deltaP `6.9178` edge `0.02` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3915` n `126` status `ready` deltaP `-8.8062` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8376` n `126` status `ready` deltaP `-5.3547` edge `0.0017` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2931` n `126` status `ready` deltaP `-8.3714` edge `-0.0221` maxDD `-4.3877`
- `market_context_high->equity_1h` score `-2.3069` n `126` status `ready` deltaP `2.0958` edge `-0.0003` maxDD `-13.1399`
- `market_context_high->index_4h` score `-2.9309` n `126` status `ready` deltaP `-8.977` edge `-0.0211` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.5437` n `126` status `ready` deltaP `-0.884` edge `-0.0576` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.1573` n `126` status `ready` deltaP `-7.3377` edge `-0.0698` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.0335` n `126` status `ready` deltaP `-8.4822` edge `-0.0003` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.2787` n `126` status `ready` deltaP `-5.529` edge `-0.0752` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-6.954` n `126` status `ready` deltaP `-19.5775` edge `-0.0797` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.96` n `126` status `ready` deltaP `4.9603` edge `0.1132` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.2381` n `126` status `ready` deltaP `-5.9863` edge `-0.132` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.6271` n `126` status `ready` deltaP `13.4921` edge `0.3512` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8375` n `126` status `ready` deltaP `-26.1409` edge `-0.1184` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.4519` n `126` status `ready` deltaP `3.6458` edge `0.1129` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
