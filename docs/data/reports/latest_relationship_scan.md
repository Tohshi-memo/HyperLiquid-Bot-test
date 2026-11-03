# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T01:37:30.224121+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0023` n `146` status `ready` deltaP `4.1033` edge `0.236` maxDD `-14.0916`
- `news_risk_high->crypto_alt_24h` score `-0.1617` n `126` status `ready` deltaP `21.4038` edge `0.7871` maxDD `-65.3749`
- `news_risk_high->crypto_alt_1h` score `-0.4931` n `146` status `ready` deltaP `1.2837` edge `0.051` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5883` n `146` status `ready` deltaP `-0.4265` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8679` n `126` status `ready` deltaP `12.5744` edge `0.1305` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9454` n `146` status `ready` deltaP `0.7485` edge `-0.0038` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2403` n `146` status `ready` deltaP `-3.3537` edge `-0.0115` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3257` n `146` status `ready` deltaP `-5.5471` edge `-0.0108` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0931` n `146` status `ready` deltaP `-3.4268` edge `-0.0154` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2292` n `126` status `ready` deltaP `-3.6459` edge `0.0227` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3349` n `146` status `ready` deltaP `-8.4776` edge `-0.0014` maxDD `-3.2657`
- `news_risk_high->equity_24h` score `-2.5094` n `126` status `ready` deltaP `16.5426` edge `0.5775` maxDD `-67.0937`
- `news_risk_high->fx_24h` score `-2.5449` n `126` status `ready` deltaP `-20.6102` edge `-0.018` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6509` n `146` status `ready` deltaP `-6.3366` edge `-0.03` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2319` n `146` status `ready` deltaP `-8.1556` edge `-0.0424` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.812` n `146` status `ready` deltaP `-12.1701` edge `-0.0011` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9033` n `146` status `ready` deltaP `-7.7577` edge `-0.0364` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0938` n `146` status `ready` deltaP `-14.536` edge `-0.0923` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.2897` n `126` status `ready` deltaP `-14.5833` edge `0.0041` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.4748` n `126` status `ready` deltaP `-26.1408` edge `-0.0931` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
