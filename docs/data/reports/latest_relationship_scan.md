# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T01:07:29.290661+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.0197` n `146` status `ready` deltaP `4.2558` edge `0.2378` maxDD `-14.0916`
- `news_risk_high->crypto_alt_24h` score `-0.3053` n `126` status `ready` deltaP `21.0565` edge `0.771` maxDD `-65.3749`
- `news_risk_high->crypto_alt_1h` score `-0.4939` n `146` status `ready` deltaP `1.2837` edge `0.0509` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5883` n `146` status `ready` deltaP `-0.4265` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8726` n `126` status `ready` deltaP `12.5744` edge `0.1299` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9191` n `146` status `ready` deltaP `1.0479` edge `-0.0036` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2411` n `146` status `ready` deltaP `-3.3537` edge `-0.0116` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3366` n `146` status `ready` deltaP `-5.6968` edge `-0.0112` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0741` n `146` status `ready` deltaP `-3.1219` edge `-0.015` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2629` n `126` status `ready` deltaP `-3.9931` edge `0.0207` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3193` n `146` status `ready` deltaP `-8.3279` edge `-0.0011` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5433` n `126` status `ready` deltaP `-20.6102` edge `-0.0178` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6298` n `146` status `ready` deltaP `-6.0372` edge `-0.0293` maxDD `-16.4088`
- `news_risk_high->equity_24h` score `-2.6663` n `126` status `ready` deltaP `16.1954` edge `0.5597` maxDD `-67.0937`
- `news_risk_high->crypto_major_1h` score `-3.2127` n `146` status `ready` deltaP `-8.0059` edge `-0.0418` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7962` n `146` status `ready` deltaP `-12.0177` edge `-0.0008` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8863` n `146` status `ready` deltaP `-7.6052` edge `-0.036` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0346` n `146` status `ready` deltaP `-14.2312` edge `-0.0894` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.4579` n `126` status `ready` deltaP `-14.9305` edge `-0.0076` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.5208` n `146` status `ready` deltaP `-1.7499` edge `-0.1123` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
