# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T00:07:31.824607+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4319`

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

- `news_risk_high->crypto_alt_4h` score `-0.4037` n `146` status `ready` deltaP `7.0776` edge `0.1647` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.474` n `146` status `ready` deltaP `3.1513` edge `0.041` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6319` n `146` status `ready` deltaP `3.5127` edge `0.0039` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6915` n `146` status `ready` deltaP `-2.4418` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.3969` n `146` status `ready` deltaP `-6.4688` edge `-0.0108` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5245` n `146` status `ready` deltaP `-8.169` edge `-0.0188` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6267` n `146` status `ready` deltaP `1.5221` edge `0.0114` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.2689` n `146` status `ready` deltaP `-5.3668` edge `0.0125` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4665` n `146` status `ready` deltaP `-10.4982` edge `0.0011` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.584` n `146` status `ready` deltaP `-12.1628` edge `0.034` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.6395` n `146` status `ready` deltaP `-21.605` edge `-0.0235` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.8871` n `146` status `ready` deltaP `-5.5409` edge `-0.0311` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.874` n `146` status `ready` deltaP `-14.5358` edge `0.0095` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6806` n `146` status `ready` deltaP `-12.4049` edge `-0.0702` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.349` n `146` status `ready` deltaP `-9.7413` edge `-0.0622` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.0055` n `146` status `ready` deltaP `-16.6303` edge `-0.2814` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.2577` n `146` status `ready` deltaP `-14.6253` edge `0.1521` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.3658` n `146` status `ready` deltaP `2.2831` edge `0.0404` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.769` n `146` status `ready` deltaP `9.9778` edge `0.4031` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.9934` n `146` status `ready` deltaP `3.2304` edge `-0.2443` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
