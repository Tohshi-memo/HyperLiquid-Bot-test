# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T08:07:32.307614+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4588`

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

- `market_context_high->unknown_1h` score `11398.6675` n `111` status `ready` deltaP `0.7161` edge `949.904` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7067.4887` n `111` status `ready` deltaP `-1.6919` edge `588.9992` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2242` n `111` status `ready` deltaP `4.0405` edge `0.0108` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3349` n `111` status `ready` deltaP `2.6987` edge `0.0028` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2593` n `111` status `ready` deltaP `-9.0212` edge `-0.0017` maxDD `-0.4478`
- `market_context_high->crypto_major_1h` score `-1.389` n `111` status `ready` deltaP `4.2011` edge `0.0049` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.6153` n `111` status `ready` deltaP `-1.6439` edge `0.0027` maxDD `-1.5726`
- `market_context_high->equity_1h` score `-1.693` n `111` status `ready` deltaP `7.6496` edge `0.0055` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-1.7723` n `111` status `ready` deltaP `4.2188` edge `0.0048` maxDD `-10.1161`
- `market_context_high->crypto_alt_1h` score `-2.1926` n `111` status `ready` deltaP `-4.5059` edge `-0.04` maxDD `-13.8848`
- `market_context_high->commodity_1h` score `-2.4353` n `111` status `ready` deltaP `-9.9167` edge `-0.0251` maxDD `-4.2715`
- `market_context_high->index_4h` score `-3.13` n `111` status `ready` deltaP `-10.6103` edge `-0.0268` maxDD `-7.0639`
- `market_context_high->fx_24h` score `-5.1401` n `111` status `ready` deltaP `-7.8078` edge `-0.0024` maxDD `-6.2445`
- `market_context_high->commodity_4h` score `-6.7692` n `111` status `ready` deltaP `-17.4165` edge `-0.0862` maxDD `-14.9432`
- `market_context_high->metal_24h` score `-9.6327` n `111` status `ready` deltaP `-5.2693` edge `0.042` maxDD `-52.1012`
- `market_context_high->crypto_major_4h` score `-9.7958` n `111` status `ready` deltaP `-6.0784` edge `-0.0829` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-10.3591` n `111` status `ready` deltaP `-6.6881` edge `-0.1374` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.8923` n `111` status `ready` deltaP `-27.4681` edge `-0.3434` maxDD `-63.7737`
- `market_context_high->crypto_major_24h` score `-14.6863` n `111` status `ready` deltaP `9.2624` edge `0.1154` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.7325` n `111` status `ready` deltaP `-31.0107` edge `-0.1647` maxDD `-39.8349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
