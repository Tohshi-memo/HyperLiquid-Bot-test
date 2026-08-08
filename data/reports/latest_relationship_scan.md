# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T21:52:26.581678+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `market_context_high->equity_24h` score `2.9868` n `103` status `ready` deltaP `4.5729` edge `0.5244` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4338` n `103` status `ready` deltaP `12.2118` edge `0.179` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6398` n `110` status `ready` deltaP `15.9063` edge `0.0979` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0167` n `117` status `ready` deltaP `12.0938` edge `0.0384` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8822` n `103` status `ready` deltaP `22.2694` edge `0.0513` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4323` n `103` status `ready` deltaP `9.1002` edge `0.1479` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4921` n `117` status `ready` deltaP `2.0306` edge `-0.005` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5406` n `117` status `ready` deltaP `-3.5518` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.5997` n `117` status `ready` deltaP `2.6819` edge `0.015` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.6041` n `117` status `ready` deltaP `-3.1897` edge `-0.0066` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6551` n `110` status `ready` deltaP `-1.7212` edge `-0.012` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.7667` n `110` status `ready` deltaP `2.4501` edge `-0.0049` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0925` n `110` status `ready` deltaP `-3.5671` edge `-0.0154` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9893` n `117` status `ready` deltaP `-11.2877` edge `-0.0276` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2471` n `110` status `ready` deltaP `0.8204` edge `-0.059` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.6389` n `117` status `ready` deltaP `-8.5496` edge `-0.0559` maxDD `-5.2274`
- `market_context_high->crypto_major_24h` score `-3.7159` n `103` status `ready` deltaP `6.2197` edge `-0.1017` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.2034` n `103` status `ready` deltaP `-12.4461` edge `-0.123` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7328` n `110` status `ready` deltaP `-13.6807` edge `-0.138` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.3368` n `117` status `ready` deltaP `-4.9376` edge `-0.6171` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
