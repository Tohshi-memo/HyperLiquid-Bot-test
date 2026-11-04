# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T19:07:33.896952+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4030`

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

- `news_risk_high->crypto_alt_4h` score `0.0658` n `146` status `ready` deltaP `8.0668` edge `0.2183` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.466` n `146` status `ready` deltaP `2.9304` edge `0.0435` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6171` n `146` status `ready` deltaP `-1.0253` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8292` n `146` status `ready` deltaP `1.9461` edge `-0.0021` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4106` n `146` status `ready` deltaP `-6.595` edge `-0.0147` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4204` n `146` status `ready` deltaP `-7.0122` edge `-0.0102` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8734` n `146` status `ready` deltaP `-0.0731` edge `-0.0096` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1789` n `146` status `ready` deltaP `-8.0285` edge `0.0086` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.2163` n `146` status `ready` deltaP `-5.2424` edge `0.035` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4558` n `146` status `ready` deltaP `-18.8368` edge `-0.0184` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5682` n `146` status `ready` deltaP `-6.3366` edge `-0.0194` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2716` n `146` status `ready` deltaP `-7.2574` edge `-0.0517` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.2956` n `146` status `ready` deltaP `-10.036` edge `0.0277` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-3.6423` n `146` status `ready` deltaP `2.9199` edge `0.0352` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.8621` n `146` status `ready` deltaP `-5.6235` edge `-0.0472` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2343` n `146` status `ready` deltaP `-11.7921` edge `-0.1223` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.1673` n `146` status `ready` deltaP `14.6491` edge `0.4265` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.8955` n `146` status `ready` deltaP `0.2318` edge `-0.0734` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4559` n `146` status `ready` deltaP `11.8809` edge `0.4165` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.0785` n `146` status `ready` deltaP `-20.6807` edge `-0.0426` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
