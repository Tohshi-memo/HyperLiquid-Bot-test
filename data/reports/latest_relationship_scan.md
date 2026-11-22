# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T06:07:27.010532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4558`

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

- `market_context_high->unknown_1h` score `10454.4648` n `119` status `ready` deltaP `0.7522` edge `871.2202` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6390.3915` n `119` status `ready` deltaP `-1.0863` edge `532.5704` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.154` n `119` status `ready` deltaP `5.0609` edge `0.013` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3483` n `119` status `ready` deltaP `2.516` edge `0.0029` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8839` n `119` status `ready` deltaP `7.4247` edge `0.0178` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.5437` n `119` status `ready` deltaP `-10.664` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->crypto_major_1h` score `-1.7075` n `119` status `ready` deltaP `1.6756` edge `-0.0191` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.7555` n `119` status `ready` deltaP `-3.8827` edge `0.0018` maxDD `-1.7455`
- `market_context_high->equity_1h` score `-1.8242` n `119` status `ready` deltaP `5.9352` edge `0.006` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4305` n `119` status `ready` deltaP `-9.7897` edge `-0.0241` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.77` n `119` status `ready` deltaP `-6.92` edge `-0.0214` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.764` n `119` status `ready` deltaP `-6.7856` edge `-0.0532` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.5262` n `119` status `ready` deltaP `-3.1795` edge `0.0056` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-5.5881` n `119` status `ready` deltaP `-7.5615` edge `-0.0014` maxDD `-6.7757`
- `market_context_high->crypto_alt_4h` score `-6.094` n `119` status `ready` deltaP `-3.3319` edge `-0.0778` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.8938` n `119` status `ready` deltaP `-18.6257` edge `-0.0826` maxDD `-15.4168`
- `market_context_high->metal_24h` score `-8.6942` n `119` status `ready` deltaP `0.4318` edge `0.0822` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.6579` n `119` status `ready` deltaP `11.6844` edge `0.2311` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.3888` n `119` status `ready` deltaP `-29.7429` edge `-0.1409` maxDD `-40.1237`
- `market_context_high->crypto_alt_24h` score `-16.2658` n `119` status `ready` deltaP `3.2184` edge `0.0114` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
