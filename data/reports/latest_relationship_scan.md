# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T21:24:21.508772+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4454`

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

- `news_risk_high->crypto_alt_4h` score `0.3779` n `146` status `ready` deltaP `8.2192` edge `0.2573` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4223` n `146` status `ready` deltaP `2.1819` edge `0.0541` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7207` n `146` status `ready` deltaP `-2.8217` edge `-0.0035` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8963` n `146` status `ready` deltaP `1.1976` edge `-0.0027` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1077` n `146` status `ready` deltaP `-2.104` edge `-0.0058` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.494` n `146` status `ready` deltaP `12.2979` edge `0.1517` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.5348` n `146` status `ready` deltaP `-8.5366` edge `-0.0147` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7285` n `146` status `ready` deltaP `1.7243` edge `0.0511` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9756` n `146` status `ready` deltaP `-1.9024` edge `-0.0105` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2544` n `146` status `ready` deltaP `-16.4645` edge `-0.0084` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.6427` n `146` status `ready` deltaP `-11.9207` edge `-0.0041` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7147` n `146` status `ready` deltaP `-7.2348` edge `-0.0322` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1815` n `146` status `ready` deltaP `-7.8562` edge `-0.0402` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1163` n `146` status `ready` deltaP `-14.6091` edge `-0.0102` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.189` n `146` status `ready` deltaP `-1.965` edge `-0.0155` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9275` n `146` status `ready` deltaP `21.7989` edge `0.7942` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8047` n `146` status `ready` deltaP `-12.7068` edge `-0.0804` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-7.9646` n `146` status `ready` deltaP `18.8476` edge `0.661` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4704` n `146` status `ready` deltaP `-1.7499` edge `-0.1081` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2033` n `146` status `ready` deltaP `-19.9153` edge `-0.0581` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
