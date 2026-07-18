# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T12:37:25.309483+00:00`
- Price records: `672`
- Market context records: `7140`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.7071` n `142` status `ready` deltaP `17.1183` edge `0.0148` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1255` n `154` status `ready` deltaP `4.7943` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4628` n `154` status `ready` deltaP `-2.0511` edge `0.0393` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6168` n `154` status `ready` deltaP `-0.2003` edge `0.0253` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6568` n `154` status `ready` deltaP `3.3965` edge `0.0342` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7237` n `154` status `ready` deltaP `-2.1444` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7449` n `154` status `ready` deltaP `1.3939` edge `-0.0049` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3998` n `154` status `ready` deltaP `-5.2998` edge `-0.0052` maxDD `-2.0897`
- `market_context_high->commodity_4h` score `-2.0981` n `142` status `ready` deltaP `-4.9209` edge `-0.0385` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-2.2678` n `142` status `ready` deltaP `-5.4685` edge `0.0184` maxDD `-5.3411`
- `market_context_high->metal_4h` score `-2.8274` n `142` status `ready` deltaP `-8.3004` edge `-0.0123` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5342` n `154` status `ready` deltaP `-0.4064` edge `-0.0446` maxDD `-15.1096`
- `market_context_high->index_4h` score `-3.9146` n `142` status `ready` deltaP `-1.0972` edge `-0.049` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.494` n `133` status `ready` deltaP `-13.4581` edge `-0.1539` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9875` n `133` status `ready` deltaP `-16.0518` edge `-0.0259` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.2742` n `142` status `ready` deltaP `0.0429` edge `-0.0066` maxDD `-24.9898`
- `market_context_high->crypto_alt_4h` score `-5.5719` n `142` status `ready` deltaP `-3.7981` edge `-0.0432` maxDD `-23.6645`
- `market_context_high->unknown_24h` score `-10.1215` n `133` status `ready` deltaP `-32.8765` edge `-0.1096` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.0813` n `142` status `ready` deltaP `-2.4261` edge `-0.2507` maxDD `-64.8586`
- `market_context_high->metal_24h` score `-14.4808` n `133` status `ready` deltaP `-29.8663` edge `-0.1895` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
