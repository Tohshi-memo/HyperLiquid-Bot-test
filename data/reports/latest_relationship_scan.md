# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T15:52:29.811949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13774`

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

- `market_context_high->index_1h` score `0.1231` n `132` status `ready` deltaP `9.7169` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0753` n `120` status `ready` deltaP `7.5915` edge `0.0093` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.096` n `132` status `ready` deltaP `2.8625` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2524` n `132` status `ready` deltaP `6.1241` edge `0.0338` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3397` n `132` status `ready` deltaP `0.617` edge `-0.0058` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5884` n `120` status `ready` deltaP `1.6972` edge `-0.0259` maxDD `-1.5342`
- `market_context_high->commodity_24h` score `-0.5969` n `105` status `ready` deltaP `3.373` edge `0.1111` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.634` n `120` status `ready` deltaP `1.3516` edge `0.0093` maxDD `-2.301`
- `market_context_high->crypto_alt_1h` score `-0.6351` n `132` status `ready` deltaP `0.7259` edge `0.0224` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.6458` n `132` status `ready` deltaP `-4.051` edge `0.0008` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6939` n `120` status `ready` deltaP `-1.8191` edge `0.0082` maxDD `-2.4692`
- `market_context_high->unknown_1h` score `-0.8152` n `132` status `ready` deltaP `7.8434` edge `-0.0975` maxDD `-0.4843`
- `market_context_high->crypto_major_1h` score `-1.1517` n `132` status `ready` deltaP `-0.9844` edge `-0.0386` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.154` n `120` status `ready` deltaP `-0.6606` edge `0.0738` maxDD `-12.7214`
- `market_context_high->crypto_alt_4h` score `-1.5881` n `120` status `ready` deltaP `2.3171` edge `-0.0208` maxDD `-5.4926`
- `market_context_high->unknown_4h` score `-2.1261` n `120` status `ready` deltaP `20.376` edge `-0.2691` maxDD `-0.5133`
- `market_context_high->fx_24h` score `-2.8552` n `105` status `ready` deltaP `-10.9127` edge `-0.0042` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.0344` n `120` status `ready` deltaP `-0.315` edge `-0.232` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2449` n `105` status `ready` deltaP `-6.4633` edge `-0.0509` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.5981` n `105` status `ready` deltaP `-17.4157` edge `-0.1426` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
