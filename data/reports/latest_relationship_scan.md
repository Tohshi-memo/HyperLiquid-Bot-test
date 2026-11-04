# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T11:22:32.859086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `0.0303` n `146` status `ready` deltaP `7.4593` edge `0.2178` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4685` n `146` status `ready` deltaP `2.1774` edge `0.0482` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7014` n `146` status `ready` deltaP `-2.5107` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8584` n `146` status `ready` deltaP `1.6418` edge `-0.0025` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3528` n `146` status `ready` deltaP `-5.7084` edge `-0.0132` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.476` n `146` status `ready` deltaP `-7.7508` edge `-0.0124` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.8473` n `146` status `ready` deltaP `-0.0521` edge `0.0477` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8707` n `146` status `ready` deltaP `-0.2311` edge `-0.0082` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.2688` n `146` status `ready` deltaP `8.2832` edge `0.1139` maxDD `-16.6552`
- `news_risk_high->commodity_1h` score `-2.3663` n `146` status `ready` deltaP `-9.08` edge `0.0` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.371` n `146` status `ready` deltaP `-17.9718` edge `-0.0133` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6511` n `146` status `ready` deltaP `-6.0417` edge `-0.032` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1614` n `146` status `ready` deltaP `-7.7101` edge `-0.0395` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7549` n `146` status `ready` deltaP `-11.7272` edge `0.0007` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7341` n `146` status `ready` deltaP `-4.7279` edge `-0.0425` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8788` n `146` status `ready` deltaP `-12.104` edge `-0.0906` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.3344` n `146` status `ready` deltaP `16.8982` edge `0.5183` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-10.7011` n `146` status `ready` deltaP `14.476` edge `0.4621` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.488` n `146` status `ready` deltaP `-1.2949` edge `-0.1126` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2489` n `146` status `ready` deltaP `-20.6807` edge `-0.0568` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
