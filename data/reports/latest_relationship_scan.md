# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T16:07:31.109429+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.0164` n `146` status `ready` deltaP `7.7619` edge `0.214` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.611` n `146` status `ready` deltaP `1.8825` edge `0.0319` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6412` n `146` status `ready` deltaP `-1.4744` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8412` n `146` status `ready` deltaP `1.7964` edge `-0.0021` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3795` n `146` status `ready` deltaP `-6.1459` edge `-0.0137` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.433` n `146` status `ready` deltaP `-7.1646` edge `-0.0108` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8182` n `146` status `ready` deltaP `0.6891` edge `-0.0076` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.0631` n `146` status `ready` deltaP `-3.1663` edge `0.0408` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.197` n `146` status `ready` deltaP `-7.5794` edge `0.0041` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4413` n `146` status `ready` deltaP `-18.6638` edge `-0.0177` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.608` n `146` status `ready` deltaP `-6.3366` edge `-0.0245` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-3.067` n `146` status `ready` deltaP `4.996` edge `0.0693` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.4754` n `146` status `ready` deltaP `-8.455` edge `-0.0607` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.4756` n `146` status `ready` deltaP `-10.036` edge `0.0127` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8247` n `146` status `ready` deltaP `-5.4711` edge `-0.0451` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0209` n `146` status `ready` deltaP `-11.9446` edge `-0.1035` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.9665` n `146` status `ready` deltaP `14.8221` edge `0.4511` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.0423` n `146` status `ready` deltaP `-0.0731` edge `-0.0836` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4463` n `146` status `ready` deltaP `11.8809` edge `0.4173` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.2993` n `146` status `ready` deltaP `-20.6807` edge `-0.061` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
