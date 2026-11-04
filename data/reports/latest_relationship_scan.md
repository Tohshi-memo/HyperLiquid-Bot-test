# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T17:07:44.476330+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0094` n `146` status `ready` deltaP `7.7619` edge `0.2107` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.604` n `146` status `ready` deltaP `1.8825` edge `0.0328` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6163` n `146` status `ready` deltaP `-1.0253` edge `-0.0021` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8268` n `146` status `ready` deltaP `1.9461` edge `-0.0019` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.399` n `146` status `ready` deltaP `-6.4453` edge `-0.0142` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4236` n `146` status `ready` deltaP `-7.0122` edge `-0.0106` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8111` n `146` status `ready` deltaP `0.8415` edge `-0.0077` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.11` n `146` status `ready` deltaP `-3.8583` edge `0.0394` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.1442` n `146` status `ready` deltaP `-7.5794` edge `0.0085` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4437` n `146` status `ready` deltaP `-18.6638` edge `-0.018` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5822` n `146` status `ready` deltaP `-6.3366` edge `-0.0212` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-3.2472` n `146` status `ready` deltaP `4.3039` edge `0.0589` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.4203` n `146` status `ready` deltaP `-8.0059` edge `-0.0591` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.4204` n `146` status `ready` deltaP `-10.036` edge `0.0173` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8235` n `146` status `ready` deltaP `-5.4711` edge `-0.045` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1397` n `146` status `ready` deltaP `-11.9446` edge `-0.1134` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.0242` n `146` status `ready` deltaP `14.8221` edge `0.4437` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9193` n `146` status `ready` deltaP `0.3842` edge `-0.0764` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.3947` n `146` status `ready` deltaP `11.8809` edge `0.4216` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.2597` n `146` status `ready` deltaP `-20.6807` edge `-0.0577` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
