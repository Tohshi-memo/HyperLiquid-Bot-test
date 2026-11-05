# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T01:07:31.172855+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.3471` n `146` status `ready` deltaP `6.8472` edge `0.1735` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5034` n `146` status `ready` deltaP `2.4813` edge `0.0417` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7245` n `146` status `ready` deltaP `-2.9714` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7897` n `146` status `ready` deltaP `2.3952` edge `-0.0018` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4543` n `146` status `ready` deltaP `-7.3435` edge `-0.0153` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5707` n `146` status `ready` deltaP `-9.4512` edge `-0.0132` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9634` n `146` status `ready` deltaP `-1.2926` edge `-0.013` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1466` n `146` status `ready` deltaP `-7.5794` edge `0.0083` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4429` n `146` status `ready` deltaP `-18.6638` edge `-0.0179` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.5379` n `146` status `ready` deltaP `-9.2217` edge `0.0203` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.5651` n `146` status `ready` deltaP `-6.0372` edge `-0.021` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.2128` n `146` status `ready` deltaP `-10.036` edge `0.0346` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3316` n `146` status `ready` deltaP `-7.5568` edge `-0.0547` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.9069` n `146` status `ready` deltaP `-1.2324` edge `-0.0425` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.1035` n `146` status `ready` deltaP `-7.6052` edge `-0.0541` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.7` n `146` status `ready` deltaP `-12.8592` edge `-0.154` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.2616` n `146` status `ready` deltaP `-0.8353` edge `-0.0968` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.3045` n `146` status `ready` deltaP `-20.6807` edge `0.0219` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-11.4682` n `146` status `ready` deltaP `10.4968` edge `0.1592` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-12.2971` n `146` status `ready` deltaP `11.8809` edge `0.3464` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
