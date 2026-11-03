# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T12:07:25.913110+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4288`

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

- `news_risk_high->crypto_alt_4h` score `0.307` n `146` status `ready` deltaP `6.3899` edge `0.2604` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4854` n `146` status `ready` deltaP `1.4334` edge `0.051` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6374` n `146` status `ready` deltaP `-1.3247` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8748` n `146` status `ready` deltaP `1.497` edge `-0.0029` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2222` n `146` status `ready` deltaP `-4.0501` edge `-0.0075` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3028` n `146` status `ready` deltaP `-4.4207` edge `-0.0124` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.9545` n `146` status `ready` deltaP `10.5617` edge `0.1249` maxDD `-16.6552`
- `news_risk_high->index_4h` score `-2.0207` n `146` status `ready` deltaP `-2.6646` edge `-0.0112` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1097` n `146` status `ready` deltaP `-2.4424` edge `0.03` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.3732` n `146` status `ready` deltaP `-17.159` edge `-0.019` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5134` n `146` status `ready` deltaP `-10.1243` edge `-0.0053` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6703` n `146` status `ready` deltaP `-6.636` edge `-0.0305` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.257` n `146` status `ready` deltaP `-8.7544` edge `-0.0405` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2891` n `146` status `ready` deltaP `-15.5238` edge `-0.0185` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3996` n `146` status `ready` deltaP `-4.2516` edge `-0.0178` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.1422` n `146` status `ready` deltaP `19.8892` edge `0.7794` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8058` n `146` status `ready` deltaP `-13.6214` edge `-0.0744` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-9.8746` n `146` status `ready` deltaP `15.0281` edge `0.5321` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.2434` n `146` status `ready` deltaP `-0.6828` edge `-0.0963` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.8759` n `146` status `ready` deltaP `-23.3876` edge `-0.091` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
