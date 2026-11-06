# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T05:07:29.402172+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.1596` n `146` status `ready` deltaP `7.1521` edge `0.1955` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5144` n `146` status `ready` deltaP `3.3795` edge `0.0343` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6603` n `146` status `ready` deltaP `3.4431` edge `0.002` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7129` n `146` status `ready` deltaP `-2.8217` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4575` n `146` status `ready` deltaP `-7.4695` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.522` n `146` status `ready` deltaP `-8.092` edge `-0.019` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6869` n `146` status `ready` deltaP `0.994` edge `0.0072` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.3585` n `146` status `ready` deltaP `-5.4384` edge `0.0015` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.3804` n `146` status `ready` deltaP `-12.1628` edge `0.0601` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.5288` n `146` status `ready` deltaP `-11.1722` edge `0.0004` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.75` n `146` status `ready` deltaP `-4.7125` edge `-0.0252` maxDD `-9.4709`
- `news_risk_high->fx_24h` score `-2.8573` n `146` status `ready` deltaP `-24.8922` edge `-0.0295` maxDD `-2.336`
- `news_risk_high->commodity_4h` score `-4.0097` n `146` status `ready` deltaP `-15.6762` edge `0.0058` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.722` n `146` status `ready` deltaP `-8.7434` edge `-0.0166` maxDD `-24.1554`
- `news_risk_high->metal_4h` score `-5.7535` n `146` status `ready` deltaP `-12.9406` edge `-0.0727` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-9.1748` n `146` status `ready` deltaP `-16.9763` edge `-0.2932` maxDD `-16.6552`
- `news_risk_high->equity_4h` score `-9.7645` n `146` status `ready` deltaP `1.6037` edge `0.0117` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-9.9637` n `146` status `ready` deltaP `-16.3554` edge `0.1048` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-10.0182` n `146` status `ready` deltaP `9.9778` edge `0.549` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-12.5928` n `146` status `ready` deltaP `6.6906` edge `0.0404` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
