# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T14:52:35.750835+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `0.0343` n `146` status `ready` deltaP `7.6865` edge `0.2168` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5065` n `146` status `ready` deltaP `2.1819` edge `0.0433` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6833` n `146` status `ready` deltaP `-2.2229` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8544` n `146` status `ready` deltaP `1.6467` edge `-0.0022` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.353` n `146` status `ready` deltaP `-5.6968` edge `-0.0133` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4546` n `146` status `ready` deltaP `-7.5342` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8429` n `146` status `ready` deltaP `0.3044` edge `-0.0082` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.0139` n `146` status `ready` deltaP `-2.4742` edge `0.0425` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.2318` n `146` status `ready` deltaP `-7.8788` edge `0.0032` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4351` n `146` status `ready` deltaP `-18.6638` edge `-0.0169` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6454` n `146` status `ready` deltaP `-6.4863` edge `-0.0283` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-2.8586` n `146` status `ready` deltaP `5.861` edge `0.0809` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.2967` n `146` status `ready` deltaP `-8.3053` edge `-0.0468` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.4883` n `146` status `ready` deltaP `-9.9696` edge `0.0112` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8327` n `146` status `ready` deltaP `-5.5556` edge `-0.0452` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9433` n `146` status `ready` deltaP `-12.0244` edge `-0.0965` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.8206` n `146` status `ready` deltaP `14.8221` edge `0.4698` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.2869` n `146` status `ready` deltaP `-0.761` edge `-0.0994` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4168` n `146` status `ready` deltaP `12.3999` edge `0.4163` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.2585` n `146` status `ready` deltaP `-20.6807` edge `-0.0576` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
