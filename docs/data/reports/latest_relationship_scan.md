# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T17:22:29.956919+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0125` n `146` status `ready` deltaP `7.7619` edge `0.2103` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5954` n `146` status `ready` deltaP `1.8825` edge `0.0339` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6163` n `146` status `ready` deltaP `-1.0253` edge `-0.0021` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8424` n `146` status `ready` deltaP `1.7964` edge `-0.0022` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4099` n `146` status `ready` deltaP `-6.595` edge `-0.0146` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4236` n `146` status `ready` deltaP `-7.0122` edge `-0.0106` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8221` n `146` status `ready` deltaP `0.6891` edge `-0.0081` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1237` n `146` status `ready` deltaP `-4.0313` edge `0.0388` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.1298` n `146` status `ready` deltaP `-7.5794` edge `0.0097` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4437` n `146` status `ready` deltaP `-18.6638` edge `-0.018` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6009` n `146` status `ready` deltaP `-6.4863` edge `-0.0226` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-3.297` n `146` status `ready` deltaP `4.1309` edge `0.0559` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.3939` n `146` status `ready` deltaP `-7.8562` edge `-0.0579` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.3988` n `146` status `ready` deltaP `-10.036` edge `0.0191` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8283` n `146` status `ready` deltaP `-5.4711` edge `-0.0454` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1697` n `146` status `ready` deltaP `-11.9446` edge `-0.1159` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.0328` n `146` status `ready` deltaP `14.8221` edge `0.4426` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9435` n `146` status `ready` deltaP `0.2318` edge `-0.0774` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.3983` n `146` status `ready` deltaP `11.8809` edge `0.4213` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.2357` n `146` status `ready` deltaP `-20.6807` edge `-0.0557` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
