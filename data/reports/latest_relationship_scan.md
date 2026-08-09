# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T06:37:28.105700+00:00`
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

- `market_context_high->equity_24h` score `3.6444` n `103` status `ready` deltaP `4.5729` edge `0.5792` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7127` n `103` status `ready` deltaP `13.2535` edge `0.1953` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3284` n `140` status `ready` deltaP `15.8841` edge `0.0721` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8888` n `143` status `ready` deltaP `11.2904` edge `0.0331` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8133` n `103` status `ready` deltaP `21.575` edge `0.0471` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.554` n `103` status `ready` deltaP `9.1002` edge `0.1635` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.2798` n `143` status `ready` deltaP `4.445` edge `-0.0034` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3584` n `140` status `ready` deltaP `7.1341` edge `-0.0021` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.4626` n `143` status `ready` deltaP `-2.1418` edge `-0.0061` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.7103` n `143` status `ready` deltaP `-5.1871` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9996` n `143` status `ready` deltaP `-0.6365` edge `0.0038` maxDD `-4.6286`
- `market_context_high->index_4h` score `-1.017` n `140` status `ready` deltaP `-2.0601` edge `-0.0105` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.0264` n `140` status `ready` deltaP `-1.8902` edge `-0.0181` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9564` n `143` status `ready` deltaP `-10.433` edge `-0.0293` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6046` n `140` status `ready` deltaP `-1.9381` edge `-0.0704` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1807` n `143` status `ready` deltaP `-10.6874` edge `-0.0616` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.1987` n `103` status `ready` deltaP `6.2197` edge `-0.0586` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.6621` n `140` status `ready` deltaP `-6.8598` edge `-0.0938` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.6258` n `103` status `ready` deltaP `-12.4461` edge `-0.1582` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.9061` n `143` status `ready` deltaP `-6.0938` edge `-0.5735` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
