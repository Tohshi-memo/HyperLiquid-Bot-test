# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T11:37:31.019791+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.0029` n `146` status `ready` deltaP `7.3073` edge `0.2153` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4841` n `146` status `ready` deltaP `2.0282` edge `0.0472` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7006` n `146` status `ready` deltaP `-2.5107` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8584` n `146` status `ready` deltaP `1.6418` edge `-0.0025` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3435` n `146` status `ready` deltaP `-5.5591` edge `-0.013` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4752` n `146` status `ready` deltaP `-7.7508` edge `-0.0123` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.8602` n `146` status `ready` deltaP `-0.2251` edge `0.0472` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8731` n `146` status `ready` deltaP `-0.2311` edge `-0.0085` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.3127` n `146` status `ready` deltaP `8.1102` edge `0.1114` maxDD `-16.6552`
- `news_risk_high->fx_24h` score `-2.3726` n `146` status `ready` deltaP `-17.9718` edge `-0.0135` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3794` n `146` status `ready` deltaP `-9.2292` edge `-0.0001` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6503` n `146` status `ready` deltaP `-6.0417` edge `-0.0319` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1842` n `146` status `ready` deltaP `-7.8593` edge `-0.0404` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7332` n `146` status `ready` deltaP `-11.5752` edge `0.0015` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7377` n `146` status `ready` deltaP `-4.7279` edge `-0.0428` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9294` n `146` status `ready` deltaP `-12.2559` edge `-0.0938` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.4019` n `146` status `ready` deltaP `16.7252` edge `0.5108` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-10.8001` n `146` status `ready` deltaP `14.303` edge `0.455` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.5338` n `146` status `ready` deltaP `-1.4469` edge `-0.1154` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2405` n `146` status `ready` deltaP `-20.6807` edge `-0.0561` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
