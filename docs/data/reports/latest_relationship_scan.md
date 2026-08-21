# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T17:51:16.847245+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `0.6156` n `133` status `ready` deltaP `8.0884` edge `0.0201` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1647` n `133` status `ready` deltaP `10.4565` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.114` n `128` status `ready` deltaP `8.3651` edge `0.0091` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1323` n `133` status `ready` deltaP `2.1791` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2295` n `133` status `ready` deltaP `6.4146` edge `0.0348` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3612` n `133` status `ready` deltaP `0.233` edge `-0.006` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5395` n `128` status `ready` deltaP `2.5534` edge `-0.0246` maxDD `-1.5942`
- `market_context_high->unknown_4h` score `-0.5736` n `128` status `ready` deltaP `20.8079` edge `-0.1426` maxDD `-0.5133`
- `market_context_high->crypto_alt_1h` score `-0.6476` n `133` status `ready` deltaP `0.7193` edge `0.0214` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.6705` n `133` status `ready` deltaP `-4.4212` edge `0.0001` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6953` n `128` status `ready` deltaP `-1.6958` edge `0.0072` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.7173` n `128` status `ready` deltaP `0.4954` edge `0.0083` maxDD `-2.618`
- `market_context_high->commodity_24h` score `-0.7704` n `105` status `ready` deltaP `1.9842` edge `0.1059` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1921` n `133` status `ready` deltaP `-1.1008` edge `-0.043` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.2457` n `128` status `ready` deltaP `3.5823` edge `-0.0007` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8751` n `128` status `ready` deltaP `-3.0869` edge `0.0537` maxDD `-15.8819`
- `market_context_high->fx_24h` score `-2.7249` n `105` status `ready` deltaP `-9.5238` edge `-0.0026` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.7991` n `128` status `ready` deltaP `0.0762` edge `-0.215` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2511` n `105` status `ready` deltaP `-6.4633` edge `-0.0517` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7217` n `105` status `ready` deltaP `-18.4574` edge `-0.1515` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
