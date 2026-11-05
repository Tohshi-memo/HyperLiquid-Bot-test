# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T04:52:30.362873+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3872`

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

- `news_risk_high->crypto_alt_4h` score `-0.5267` n `146` status `ready` deltaP `5.6277` edge `0.1586` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6227` n `146` status `ready` deltaP `1.8825` edge `0.0304` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7183` n `146` status `ready` deltaP `-2.8217` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7322` n `146` status `ready` deltaP `2.994` edge `-0.001` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5251` n `146` status `ready` deltaP `-8.2417` edge `-0.0184` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5983` n `146` status `ready` deltaP `-9.9085` edge `-0.0137` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8042` n `146` status `ready` deltaP `0.6891` edge `-0.0058` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1322` n `146` status `ready` deltaP `-7.5794` edge `0.0095` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4367` n `146` status `ready` deltaP `-18.6638` edge `-0.0171` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5511` n `146` status `ready` deltaP `-5.8875` edge `-0.0202` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8156` n `146` status `ready` deltaP `-11.8168` edge `0.002` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1017` n `146` status `ready` deltaP `-9.4262` edge `0.0398` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3616` n `146` status `ready` deltaP `-7.4071` edge `-0.0582` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4436` n `146` status `ready` deltaP `-9.8918` edge `-0.0672` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.8993` n `146` status `ready` deltaP `-3.8276` edge `-0.1079` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.6755` n `146` status `ready` deltaP `-12.4019` edge `-0.155` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.7422` n `146` status `ready` deltaP `-20.1616` edge `0.0653` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.8757` n `146` status `ready` deltaP `0.6891` edge `-0.0748` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-13.4986` n `146` status `ready` deltaP `7.9016` edge `-0.0838` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-13.6098` n `146` status `ready` deltaP `9.9778` edge `0.2497` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
