# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T04:52:27.947879+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.7501` n `146` status `ready` deltaP `9.2863` edge `0.2979` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3022` n `146` status `ready` deltaP `3.0801` edge `0.0635` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6584` n `146` status `ready` deltaP `-1.7738` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7309` n `146` status `ready` deltaP `2.6946` edge `0.0011` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2214` n `146` status `ready` deltaP `-4.1998` edge `-0.0064` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.32` n `146` status `ready` deltaP `12.2979` edge `0.1662` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4638` n `146` status `ready` deltaP `-7.622` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.6655` n `146` status `ready` deltaP `2.2451` edge `0.0557` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7293` n `146` status `ready` deltaP `0.6891` edge `0.0038` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.329` n `146` status `ready` deltaP `-17.8534` edge `-0.0087` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.4147` n `146` status `ready` deltaP `-4.9893` edge `-0.0087` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4282` n `146` status `ready` deltaP `-9.8249` edge `-0.0002` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.9657` n `146` status `ready` deltaP `-6.8083` edge `-0.0292` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7892` n `146` status `ready` deltaP `-12.1701` edge `0.0008` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3178` n `146` status `ready` deltaP `-3.1845` edge `-0.0181` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0011` n `146` status `ready` deltaP `-10.2677` edge `-0.0297` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.4319` n `146` status `ready` deltaP `21.2781` edge `0.733` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.3978` n `146` status `ready` deltaP `18.8476` edge `0.6249` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.2923` n `146` status `ready` deltaP `0.8415` edge `-0.0272` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2863` n `146` status `ready` deltaP `-20.2626` edge `-0.0627` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
