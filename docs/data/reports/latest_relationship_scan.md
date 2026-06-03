# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T18:37:34.810347+00:00`
- Price records: `672`
- Market context records: `2789`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.1616` n `142` status `ready` deltaP `5.9003` edge `0.2706` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.4608` n `142` status `ready` deltaP `3.3965` edge `0.5741` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8628` n `142` status `ready` deltaP `6.1856` edge `0.136` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5593` n `142` status `ready` deltaP `11.0377` edge `0.2824` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3169` n `142` status `ready` deltaP `13.3009` edge `0.0361` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0697` n `142` status `ready` deltaP `3.8817` edge `0.0414` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0992` n `142` status `ready` deltaP `4.0483` edge `0.0097` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5371` n `142` status `ready` deltaP `-0.5376` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6154` n `142` status `ready` deltaP `0.7316` edge `0.0008` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6842` n `142` status `ready` deltaP `-0.7316` edge `-0.0075` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6905` n `142` status `ready` deltaP `5.0962` edge `0.0535` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9256` n `142` status `ready` deltaP `3.7763` edge `0.0431` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0346` n `142` status `ready` deltaP `-3.1985` edge `0.0184` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1069` n `142` status `ready` deltaP `-3.2957` edge `0.0076` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.243` n `142` status `ready` deltaP `1.9624` edge `0.0213` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.3249` n `142` status `ready` deltaP `14.1854` edge `0.2291` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.4738` n `142` status `ready` deltaP `-2.0588` edge `-0.0219` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6592` n `142` status `ready` deltaP `-0.6012` edge `-0.0167` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.0985` n `142` status `ready` deltaP `-0.3134` edge `-0.0119` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4075` n `142` status `ready` deltaP `5.7347` edge `0.1437` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
