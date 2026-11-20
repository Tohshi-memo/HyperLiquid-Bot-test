# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T18:37:36.458427+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2758`

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

- `market_context_high->unknown_1h` score `10163.3849` n `126` status `ready` deltaP `1.6135` edge `846.9578` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6200.8617` n `126` status `ready` deltaP `-0.3145` edge `516.7711` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `4.9018` n `107` status `ready` deltaP `27.4257` edge `1.1586` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.5755` n `107` status `ready` deltaP `14.3156` edge `0.9479` maxDD `-66.63`
- `market_context_high->metal_1h` score `-0.1579` n `126` status `ready` deltaP `4.5504` edge `0.0159` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2804` n `126` status `ready` deltaP `3.3076` edge `0.0032` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.512` n `126` status `ready` deltaP `12.1007` edge `0.0343` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3975` n `126` status `ready` deltaP `-8.8062` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8287` n `126` status `ready` deltaP `5.988` edge `0.0136` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.965` n `126` status `ready` deltaP `-7.4889` edge `-0.0004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1816` n `126` status `ready` deltaP `-7.3235` edge `-0.0198` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.4277` n `126` status `ready` deltaP `-3.0318` edge `-0.0188` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.4583` n `126` status `ready` deltaP `2.4094` edge `0.0109` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1104` n `126` status `ready` deltaP `-3.4455` edge `-0.0085` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.2608` n `126` status `ready` deltaP `1.0259` edge `0.1398` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.6386` n `107` status `ready` deltaP `13.2139` edge `0.115` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.7807` n `107` status `ready` deltaP `-18.9674` edge `-0.0113` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8356` n `126` status `ready` deltaP `-19.8824` edge `-0.0678` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.1022` n `126` status `ready` deltaP `1.7881` edge `0.0775` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.9898` n `107` status `ready` deltaP `-26.3369` edge `-0.157` maxDD `-30.9921`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
