# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T19:37:24.445251+00:00`
- Price records: `672`
- Market context records: `6422`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->crypto_alt_24h` score `12.431` n `32` status `ready` deltaP `31.9444` edge `0.8377` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.6612` n `146` status `ready` deltaP `17.2398` edge `0.7702` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.6171` n `32` status `ready` deltaP `55.7292` edge `0.1799` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2131` n `32` status `ready` deltaP `43.9787` edge `0.0625` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1125` n `32` status `ready` deltaP `35.2431` edge `0.1283` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.6334` n `32` status `ready` deltaP `13.5417` edge `0.4535` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4961` n `32` status `ready` deltaP `30.0898` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4889` n `32` status `ready` deltaP `14.128` edge `0.1434` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8575` n `32` status `ready` deltaP `10.1235` edge `0.0886` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6266` n `203` status `ready` deltaP `-7.075` edge `0.2002` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3379` n `197` status `ready` deltaP `10.5569` edge `0.0416` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.2602` n `197` status `ready` deltaP `9.8877` edge `0.0234` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2105` n `32` status `ready` deltaP `6.9798` edge `-0.0296` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2836` n `146` status `ready` deltaP `18.5978` edge `0.0965` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5231` n `203` status `ready` deltaP `1.275` edge `0.0022` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5629` n `197` status `ready` deltaP `7.4579` edge `0.048` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6048` n `32` status `ready` deltaP `-0.4491` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.6553` n `203` status `ready` deltaP `-1.98` edge `-0.0025` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6875` n `203` status `ready` deltaP `-2.8782` edge `0.003` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7478` n `203` status `ready` deltaP `-1.0678` edge `-0.002` maxDD `-0.9225`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
