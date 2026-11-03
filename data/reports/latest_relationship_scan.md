# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T23:07:31.070390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.3912` n `146` status `ready` deltaP `8.2192` edge `0.259` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4332` n `146` status `ready` deltaP `2.1819` edge `0.0527` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7121` n `146` status `ready` deltaP `-2.672` edge `-0.0034` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9143` n `146` status `ready` deltaP `1.0479` edge `-0.0032` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1248` n `146` status `ready` deltaP `-2.4034` edge `-0.006` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.4448` n `146` status `ready` deltaP `12.2979` edge `0.1558` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.485` n `146` status `ready` deltaP `-7.7744` edge `-0.0134` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7402` n `146` status `ready` deltaP `1.7243` edge `0.0496` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9701` n `146` status `ready` deltaP `-1.9024` edge `-0.0098` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2388` n `146` status `ready` deltaP `-16.4645` edge `-0.0064` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.6307` n `146` status `ready` deltaP `-11.771` edge `-0.0041` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7514` n `146` status `ready` deltaP `-7.3845` edge `-0.0359` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1696` n `146` status `ready` deltaP `-7.7065` edge `-0.0402` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1187` n `146` status `ready` deltaP `-14.6091` edge `-0.0104` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.2242` n `146` status `ready` deltaP `-2.2699` edge `-0.0164` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9673` n `146` status `ready` deltaP `21.7989` edge `0.7891` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.7393` n `146` status `ready` deltaP `-12.2495` edge `-0.078` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.2058` n `146` status `ready` deltaP `18.8476` edge `0.6409` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4776` n `146` status `ready` deltaP `-1.7499` edge `-0.1087` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2357` n `146` status `ready` deltaP `-19.9153` edge `-0.0608` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
