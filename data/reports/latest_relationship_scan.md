# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T01:52:29.084753+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1656.3158` n `134` status `ready` deltaP `-2.7908` edge `138.0879` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `41.0663` n `134` status `ready` deltaP `5.142` edge `3.4012` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.7235` n `134` status `ready` deltaP `31.2707` edge `0.0368` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3042` n `134` status `ready` deltaP `9.8557` edge `0.0112` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1669` n `134` status `ready` deltaP `12.7184` edge `0.051` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.1104` n `134` status `ready` deltaP `7.1655` edge `0.0642` maxDD `-5.2213`
- `market_context_high->metal_4h` score `0.0909` n `134` status `ready` deltaP `13.087` edge `0.014` maxDD `-1.8344`
- `market_context_high->equity_1h` score `-0.0512` n `134` status `ready` deltaP `3.2845` edge `0.0614` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1353` n `134` status `ready` deltaP `2.9806` edge `-0.0014` maxDD `-0.1986`
- `market_context_high->equity_24h` score `-0.1521` n `134` status `ready` deltaP `13.8812` edge `0.1705` maxDD `-14.0571`
- `market_context_high->commodity_1h` score `-0.32` n `134` status `ready` deltaP `1.6445` edge `0.0138` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.6058` n `134` status `ready` deltaP `-1.9976` edge `-0.0045` maxDD `-0.4545`
- `market_context_high->equity_4h` score `-0.6312` n `134` status `ready` deltaP `0.2571` edge `0.0758` maxDD `-6.008`
- `market_context_high->crypto_alt_1h` score `-0.6801` n `134` status `ready` deltaP `4.0464` edge `0.0723` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8893` n `134` status `ready` deltaP `-2.6946` edge `-0.0003` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.4106` n `134` status `ready` deltaP `1.3682` edge `0.0064` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5204` n `134` status `ready` deltaP `3.9257` edge `0.0436` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.5976` n `134` status `ready` deltaP `7.8563` edge `0.0723` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.1495` n `134` status `ready` deltaP `-4.6051` edge `-0.0164` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.0213` n `134` status `ready` deltaP `5.2446` edge `0.0085` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
