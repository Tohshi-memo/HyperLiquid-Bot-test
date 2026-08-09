# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T11:52:26.737447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9825`

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

- `market_context_high->equity_24h` score `3.834` n `103` status `ready` deltaP `4.5729` edge `0.595` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.548` n `103` status `ready` deltaP `11.3437` edge `0.1943` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.0673` n `143` status `ready` deltaP `13.985` edge `0.063` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7785` n `143` status `ready` deltaP `10.6916` edge `0.0279` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7356` n `103` status `ready` deltaP `21.4013` edge `0.0383` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5308` n `103` status `ready` deltaP `8.5794` edge `0.164` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3205` n `143` status `ready` deltaP `3.9959` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3746` n `143` status `ready` deltaP `-0.6448` edge `-0.0048` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4931` n `143` status `ready` deltaP `5.6755` edge `-0.0036` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6643` n `143` status `ready` deltaP `-4.4386` edge `-0.006` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.76` n `143` status `ready` deltaP `0.7612` edge `-0.0079` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8725` n `143` status `ready` deltaP `0.2618` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9654` n `143` status `ready` deltaP `-0.8986` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8461` n `143` status `ready` deltaP `-9.6845` edge `-0.0251` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3837` n `143` status `ready` deltaP `-0.0469` edge `-0.0646` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1064` n `143` status `ready` deltaP `-10.388` edge `-0.0574` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.5209` n `143` status `ready` deltaP `-6.2948` edge `-0.0858` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.6807` n `103` status `ready` deltaP `3.6155` edge `-0.0814` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.6865` n `103` status `ready` deltaP `-15.7447` edge `-0.2246` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7478` n `143` status `ready` deltaP `-5.3453` edge `-0.5653` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
