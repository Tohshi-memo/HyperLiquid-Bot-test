# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T13:37:29.303947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1385.0278` n `143` status `ready` deltaP `-2.7256` edge `115.5299` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `45.1805` n `143` status `ready` deltaP `5.6594` edge `3.7406` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.4338` n `143` status `ready` deltaP `21.4404` edge `0.0035` maxDD `-0.8231`
- `market_context_high->commodity_4h` score `0.206` n `143` status `ready` deltaP `12.9371` edge `0.0528` maxDD `-1.0837`
- `market_context_high->fx_1h` score `0.061` n `143` status `ready` deltaP `6.0446` edge `0.0006` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0819` n `143` status `ready` deltaP `7.9394` edge `0.0068` maxDD `-0.9512`
- `market_context_high->fx_4h` score `-0.1925` n `143` status `ready` deltaP `5.0657` edge `0.0014` maxDD `-0.4545`
- `market_context_high->metal_4h` score `-0.3418` n `143` status `ready` deltaP `10.0333` edge `0.0041` maxDD `-3.5181`
- `market_context_high->commodity_1h` score `-0.4214` n `143` status `ready` deltaP `1.2479` edge `0.0116` maxDD `-0.7359`
- `market_context_high->crypto_major_1h` score `-0.6278` n `143` status `ready` deltaP `3.797` edge `0.0225` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.7837` n `143` status `ready` deltaP `-4.1927` edge `-0.0045` maxDD `-1.4415`
- `market_context_high->fx_24h` score `-1.0401` n `143` status `ready` deltaP `5.2497` edge `0.0114` maxDD `-0.9792`
- `market_context_high->equity_1h` score `-1.3735` n `143` status `ready` deltaP `-0.3497` edge `0.0016` maxDD `-8.3615`
- `market_context_high->crypto_alt_1h` score `-1.6997` n `143` status `ready` deltaP `1.0447` edge `0.0059` maxDD `-11.7957`
- `market_context_high->metal_24h` score `-2.1783` n `143` status `ready` deltaP `1.1545` edge `-0.0056` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.897` n `143` status `ready` deltaP `-9.5227` edge `-0.0303` maxDD `-4.8104`
- `market_context_high->crypto_major_4h` score `-3.3757` n `143` status `ready` deltaP `2.5275` edge `-0.0413` maxDD `-25.333`
- `market_context_high->equity_4h` score `-3.825` n `143` status `ready` deltaP `-3.9453` edge `-0.1017` maxDD `-22.3241`
- `market_context_high->crypto_major_24h` score `-3.8474` n `143` status `ready` deltaP `-3.8316` edge `0.018` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.5524` n `143` status `ready` deltaP `4.6572` edge `-0.1347` maxDD `-14.0571`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
