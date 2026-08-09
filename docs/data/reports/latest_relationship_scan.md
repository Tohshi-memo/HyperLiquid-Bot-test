# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T14:22:34.031761+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10825`

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

- `market_context_high->equity_24h` score `3.7942` n `103` status `ready` deltaP `4.2257` edge `0.594` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3966` n `103` status `ready` deltaP `9.7812` edge `0.1921` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.219` n `143` status `ready` deltaP `15.3569` edge `0.0665` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7761` n `143` status `ready` deltaP `10.6916` edge `0.0277` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7122` n `103` status `ready` deltaP `21.4013` edge `0.0353` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4304` n `103` status `ready` deltaP `6.8433` edge `0.1627` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3481` n `143` status `ready` deltaP `3.6965` edge `-0.0041` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3746` n `143` status `ready` deltaP `-0.6448` edge `-0.0048` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5077` n `143` status `ready` deltaP `5.523` edge `-0.0038` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6815` n `143` status `ready` deltaP `-4.738` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.816` n `143` status `ready` deltaP `0.1514` edge `-0.0085` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9229` n `143` status `ready` deltaP `-0.3371` edge `0.0082` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9995` n `143` status `ready` deltaP `-1.5084` edge `-0.0172` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9216` n `143` status `ready` deltaP `-10.2833` edge `-0.0274` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4285` n `143` status `ready` deltaP `-0.3517` edge `-0.0663` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2047` n `143` status `ready` deltaP `-11.1365` edge `-0.0606` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.7073` n `143` status `ready` deltaP `-7.5143` edge `-0.0932` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.0547` n `103` status `ready` deltaP `1.8794` edge `-0.101` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.3149` n `103` status `ready` deltaP `-17.4808` edge `-0.2654` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7897` n `143` status `ready` deltaP `-5.7944` edge `-0.5658` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
