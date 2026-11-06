# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T04:37:27.260453+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4314`

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

- `news_risk_high->crypto_alt_4h` score `-0.1831` n `146` status `ready` deltaP `6.9997` edge `0.1935` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5433` n `146` status `ready` deltaP `3.2298` edge `0.0316` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6615` n `146` status `ready` deltaP `3.4431` edge `0.0019` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7129` n `146` status `ready` deltaP `-2.8217` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4662` n `146` status `ready` deltaP `-7.622` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5228` n `146` status `ready` deltaP `-8.092` edge `-0.0191` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6846` n `146` status `ready` deltaP `0.994` edge `0.0075` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.3631` n `146` status `ready` deltaP `-5.4384` edge `0.0009` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.396` n `146` status `ready` deltaP `-12.1628` edge `0.0581` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.5444` n `146` status `ready` deltaP `-11.3219` edge `0.0001` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.7944` n `146` status `ready` deltaP `-5.0119` edge `-0.0269` maxDD `-9.4709`
- `news_risk_high->fx_24h` score `-2.8361` n `146` status `ready` deltaP `-24.5461` edge `-0.0291` maxDD `-2.336`
- `news_risk_high->commodity_4h` score `-4.0097` n `146` status `ready` deltaP `-15.6762` edge `0.0058` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.734` n `146` status `ready` deltaP `-8.7434` edge `-0.0176` maxDD `-24.1554`
- `news_risk_high->metal_4h` score `-5.7535` n `146` status `ready` deltaP `-12.9406` edge `-0.0727` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-9.1736` n `146` status `ready` deltaP `-16.9763` edge `-0.2931` maxDD `-16.6552`
- `news_risk_high->equity_4h` score `-9.6957` n `146` status `ready` deltaP `1.9086` edge `0.0154` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-9.9037` n `146` status `ready` deltaP `-16.3554` edge `0.1098` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-10.1574` n `146` status `ready` deltaP `9.9778` edge `0.5374` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-12.7964` n `146` status `ready` deltaP `6.3446` edge `0.0166` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
