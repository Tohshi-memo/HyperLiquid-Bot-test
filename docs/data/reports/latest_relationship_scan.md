# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T12:37:29.281659+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_4h` score `0.239` n `142` status `ready` deltaP `6.2586` edge `0.2343` maxDD `-12.6306`
- `news_risk_high->crypto_alt_24h` score `-0.3442` n `120` status `ready` deltaP `16.9792` edge `0.6002` maxDD `-51.9355`
- `news_risk_high->fx_1h` score `-0.5346` n `146` status `ready` deltaP `0.6214` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5493` n `146` status `ready` deltaP `1.134` edge `0.0448` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8168` n `120` status `ready` deltaP `13.4375` edge `0.1313` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0976` n `146` status `ready` deltaP `-0.7485` edge `-0.0065` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1587` n `142` status `ready` deltaP `-1.8293` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.279` n `146` status `ready` deltaP `-4.9483` edge `-0.0088` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.1225` n `120` status `ready` deltaP `-14.7222` edge `-0.0031` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2215` n `142` status `ready` deltaP `-4.4573` edge `-0.025` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3757` n `146` status `ready` deltaP `-8.4776` edge `-0.0048` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.8168` n `120` status `ready` deltaP `-9.2014` edge `-0.0156` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.9167` n `146` status `ready` deltaP `-7.5342` edge `-0.0561` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3386` n `146` status `ready` deltaP `-8.7544` edge `-0.0473` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1009` n `142` status `ready` deltaP `-13.3373` edge `-0.0174` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5439` n `142` status `ready` deltaP `-4.4658` edge `-0.0284` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.4339` n `120` status `ready` deltaP `7.1181` edge `0.2654` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.1959` n `142` status `ready` deltaP `-14.2369` edge `-0.1028` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.3021` n `142` status `ready` deltaP `-3.2957` edge `-0.2063` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.5769` n `120` status `ready` deltaP `-25.9723` edge `-0.1512` maxDD `-28.8982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
