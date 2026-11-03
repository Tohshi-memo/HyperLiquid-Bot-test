# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T00:52:37.836842+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4836`

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

- `news_risk_high->crypto_alt_4h` score `0.0378` n `146` status `ready` deltaP `4.4082` edge `0.2391` maxDD `-14.0916`
- `news_risk_high->crypto_alt_24h` score `-0.3643` n `126` status `ready` deltaP `20.8829` edge `0.7646` maxDD `-65.3749`
- `news_risk_high->crypto_alt_1h` score `-0.4799` n `146` status `ready` deltaP `1.4334` edge `0.0517` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5883` n `146` status `ready` deltaP `-0.4265` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8757` n `126` status `ready` deltaP `12.5744` edge `0.1295` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9047` n `146` status `ready` deltaP `1.1976` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2419` n `146` status `ready` deltaP `-3.3537` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3366` n `146` status `ready` deltaP `-5.6968` edge `-0.0112` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0733` n `146` status `ready` deltaP `-3.1219` edge `-0.0149` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2781` n `126` status `ready` deltaP `-4.1667` edge `0.0199` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3049` n `146` status `ready` deltaP `-8.1782` edge `-0.0009` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5418` n `126` status `ready` deltaP `-20.6102` edge `-0.0176` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.615` n `146` status `ready` deltaP `-5.8875` edge `-0.0284` maxDD `-16.4088`
- `news_risk_high->equity_24h` score `-2.737` n `126` status `ready` deltaP `16.0218` edge `0.5518` maxDD `-67.0937`
- `news_risk_high->crypto_major_1h` score `-3.1863` n `146` status `ready` deltaP `-7.8562` edge `-0.0406` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7804` n `146` status `ready` deltaP `-11.8652` edge `-0.0005` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8717` n `146` status `ready` deltaP `-7.4528` edge `-0.0358` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9996` n `146` status `ready` deltaP `-14.0787` edge `-0.0875` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.521` n `126` status `ready` deltaP `-15.1041` edge `-0.0117` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.4798` n `146` status `ready` deltaP `-1.5975` edge `-0.1099` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
