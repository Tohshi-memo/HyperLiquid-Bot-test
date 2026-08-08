# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T22:52:25.576390+00:00`
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

- `market_context_high->equity_24h` score `3.0216` n `103` status `ready` deltaP `4.5729` edge `0.5273` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4554` n `103` status `ready` deltaP `12.2118` edge `0.1808` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.7026` n `113` status `ready` deltaP `16.6468` edge `0.0982` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0465` n `121` status `ready` deltaP `12.5105` edge `0.0381` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8752` n `103` status `ready` deltaP `22.2694` edge `0.0504` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4448` n `103` status `ready` deltaP `9.1002` edge `0.1495` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4617` n `121` status `ready` deltaP `2.3655` edge `-0.0047` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5528` n `121` status `ready` deltaP `-3.7722` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6309` n `113` status `ready` deltaP `-1.1966` edge `-0.0124` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.6391` n `121` status `ready` deltaP `2.5647` edge `0.0125` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.6638` n `121` status `ready` deltaP `-4.293` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.6896` n `113` status `ready` deltaP `3.3685` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.1665` n `113` status `ready` deltaP `-4.8551` edge `-0.0163` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1582` n `121` status `ready` deltaP `-12.7851` edge `-0.0317` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2573` n `113` status `ready` deltaP `1.1278` edge `-0.0619` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.9514` n `121` status `ready` deltaP `-10.0188` edge `-0.0629` maxDD `-5.9672`
- `market_context_high->crypto_major_24h` score `-3.7939` n `103` status `ready` deltaP `6.2197` edge `-0.1082` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.3438` n `103` status `ready` deltaP `-12.4461` edge `-0.1347` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7658` n `113` status `ready` deltaP `-13.3742` edge `-0.1428` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.3253` n `121` status `ready` deltaP `-4.689` edge `-0.6178` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
