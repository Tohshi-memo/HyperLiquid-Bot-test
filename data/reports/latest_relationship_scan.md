# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T05:22:30.808911+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.7392` n `146` status `ready` deltaP `9.2863` edge `0.2965` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3319` n `146` status `ready` deltaP `2.9304` edge `0.0607` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6763` n `146` status `ready` deltaP `-2.0732` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7393` n `146` status `ready` deltaP `2.6946` edge `0.0004` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.233` n `146` status `ready` deltaP `-4.3495` edge `-0.0069` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.32` n `146` status `ready` deltaP `12.2979` edge `0.1662` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4631` n `146` status `ready` deltaP `-7.622` edge `-0.0116` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.6443` n `146` status `ready` deltaP `2.5923` edge `0.0561` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7206` n `146` status `ready` deltaP `0.8415` edge `0.0039` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3329` n `146` status `ready` deltaP `-17.8534` edge `-0.0092` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.439` n `146` status `ready` deltaP `-9.8249` edge `-0.0011` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.456` n `146` status `ready` deltaP `-5.139` edge `-0.013` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-2.9921` n `146` status `ready` deltaP `-6.8083` edge `-0.0314` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.788` n `146` status `ready` deltaP `-12.1701` edge `0.0009` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.302` n `146` status `ready` deltaP `-3.0321` edge `-0.0178` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.9999` n `146` status `ready` deltaP `-10.2677` edge `-0.0296` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.5194` n `146` status `ready` deltaP `20.9309` edge `0.7241` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.4844` n `146` status `ready` deltaP `18.5003` edge `0.62` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.2777` n `146` status `ready` deltaP `0.994` edge `-0.027` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3201` n `146` status `ready` deltaP `-20.6098` edge `-0.0632` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
