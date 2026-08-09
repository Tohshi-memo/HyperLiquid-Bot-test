# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T01:52:25.450133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.2532` n `103` status `ready` deltaP `4.5729` edge `0.5466` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6203` n `103` status `ready` deltaP `13.2535` edge `0.1876` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4244` n `121` status `ready` deltaP `14.0698` edge `0.0922` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8674` n `133` status `ready` deltaP `10.6029` edge `0.0359` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.849` n `103` status `ready` deltaP `22.0958` edge `0.0482` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4869` n `103` status `ready` deltaP `9.1002` edge `0.1549` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4201` n `133` status `ready` deltaP `2.7813` edge `-0.004` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.5111` n `121` status `ready` deltaP `5.4198` edge `-0.0034` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.5388` n `133` status `ready` deltaP `-3.5027` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6215` n `121` status `ready` deltaP `-0.926` edge `-0.013` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6453` n `133` status `ready` deltaP `-3.9518` edge `-0.0068` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.8838` n `133` status `ready` deltaP `0.5864` edge `0.0053` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0258` n `121` status `ready` deltaP `-2.1052` edge `-0.0166` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1236` n `133` status `ready` deltaP `-11.7734` edge `-0.0343` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3144` n `121` status `ready` deltaP `1.3291` edge `-0.068` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0558` n `133` status `ready` deltaP `-10.1369` edge `-0.0647` maxDD `-6.4562`
- `market_context_high->crypto_major_24h` score `-3.6523` n `103` status `ready` deltaP `6.2197` edge `-0.0964` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.4758` n `103` status `ready` deltaP `-12.4461` edge `-0.1457` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.669` n `121` status `ready` deltaP `-12.689` edge `-0.1393` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.3638` n `133` status `ready` deltaP `-5.7854` edge `-0.6137` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
