# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T01:37:32.032802+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.3851` n `146` status `ready` deltaP `6.9254` edge `0.1681` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6204` n `146` status `ready` deltaP `2.7807` edge `0.0247` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6879` n `146` status `ready` deltaP `-2.3726` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.6914` n `146` status `ready` deltaP `2.994` edge `0.0024` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4237` n `146` status `ready` deltaP `-6.9254` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5431` n `146` status `ready` deltaP `-8.3914` edge `-0.0197` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6662` n `146` status `ready` deltaP `0.9132` edge `0.0104` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.4044` n `146` status `ready` deltaP `-6.0372` edge `-0.0004` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4606` n `146` status `ready` deltaP `-10.4237` edge `0.0011` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.52` n `146` status `ready` deltaP `-12.1628` edge `0.0422` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.7114` n `146` status `ready` deltaP `-22.643` edge `-0.0258` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-3.0235` n `146` status `ready` deltaP `-5.7604` edge `-0.041` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.868` n `146` status `ready` deltaP `-14.5358` edge `0.01` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7326` n `146` status `ready` deltaP `-12.7093` edge `-0.0725` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.1829` n `146` status `ready` deltaP `-9.2847` edge `-0.0514` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.1316` n `146` status `ready` deltaP `-16.9763` edge `-0.2896` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.3789` n `146` status `ready` deltaP `-14.6253` edge `0.142` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4453` n `146` status `ready` deltaP `1.9787` edge `0.0358` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.2242` n `146` status `ready` deltaP `9.9778` edge `0.4485` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.3076` n `146` status `ready` deltaP `4.2684` edge `-0.1633` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
