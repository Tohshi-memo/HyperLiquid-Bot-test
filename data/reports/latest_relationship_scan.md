# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T13:52:29.836359+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0127` n `146` status `ready` deltaP `7.3073` edge `0.2133` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4987` n `146` status `ready` deltaP `2.0322` edge `0.0453` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7082` n `146` status `ready` deltaP `-2.672` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8376` n `146` status `ready` deltaP `1.7964` edge `-0.0018` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.325` n `146` status `ready` deltaP `-5.2477` edge `-0.0127` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4603` n `146` status `ready` deltaP `-7.5988` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8581` n `146` status `ready` deltaP `0.0729` edge `-0.0086` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-1.9654` n `146` status `ready` deltaP `-1.7822` edge `0.0441` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.2869` n `146` status `ready` deltaP `-8.3279` edge `0.0016` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.398` n `146` status `ready` deltaP `-18.1448` edge `-0.0156` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6251` n `146` status `ready` deltaP `-6.3366` edge `-0.0267` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-2.6976` n `146` status `ready` deltaP `6.5531` edge `0.0897` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.2355` n `146` status `ready` deltaP `-8.1556` edge `-0.0427` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.5338` n `146` status `ready` deltaP `-10.2074` edge `0.009` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8261` n `146` status `ready` deltaP `-5.4878` edge `-0.0451` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0147` n `146` status `ready` deltaP `-12.4079` edge `-0.0999` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.7379` n `146` status `ready` deltaP `15.1681` edge `0.4781` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-11.3014` n `146` status `ready` deltaP `13.092` edge `0.4213` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.446` n `146` status `ready` deltaP `-1.2949` edge `-0.1091` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2345` n `146` status `ready` deltaP `-20.6807` edge `-0.0556` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
