# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T07:07:30.420833+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8827`

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

- `market_context_high->equity_24h` score `3.6756` n `103` status `ready` deltaP `4.5729` edge `0.5818` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7127` n `103` status `ready` deltaP `13.2535` edge `0.1953` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2716` n `140` status `ready` deltaP `15.5793` edge `0.0694` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8708` n `143` status `ready` deltaP `11.2904` edge `0.0316` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8063` n `103` status `ready` deltaP `21.575` edge `0.0462` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5563` n `103` status `ready` deltaP `9.1002` edge `0.1638` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.2798` n `143` status `ready` deltaP `4.445` edge `-0.0034` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3596` n `140` status `ready` deltaP `7.1341` edge `-0.0022` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.4455` n `143` status `ready` deltaP `-1.8424` edge `-0.0059` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.7025` n `143` status `ready` deltaP `-5.0374` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.984` n `143` status `ready` deltaP `-0.6365` edge `0.0051` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.9854` n `140` status `ready` deltaP `-1.7552` edge `-0.0099` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.0153` n `140` status `ready` deltaP `-1.7378` edge `-0.0177` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9432` n `143` status `ready` deltaP `-10.433` edge `-0.0282` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5684` n `140` status `ready` deltaP `-1.7857` edge `-0.0684` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1627` n `143` status `ready` deltaP `-10.6874` edge `-0.0601` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.1915` n `103` status `ready` deltaP `6.2197` edge `-0.058` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.6477` n `140` status `ready` deltaP `-6.8598` edge `-0.0926` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.6834` n `103` status `ready` deltaP `-12.4461` edge `-0.163` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8533` n `143` status `ready` deltaP `-6.0938` edge `-0.5691` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
