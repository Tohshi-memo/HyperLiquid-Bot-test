# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T15:56:03.373085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10826`

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

- `market_context_high->equity_24h` score `3.5452` n `104` status `ready` deltaP `3.8729` edge `0.5756` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.2571` n `104` status `ready` deltaP `8.9076` edge `0.1863` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.321` n `143` status `ready` deltaP `16.2716` edge `0.0689` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8253` n `143` status `ready` deltaP `11.1407` edge `0.0288` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.657` n `104` status `ready` deltaP `20.5929` edge `0.0336` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.361` n `104` status `ready` deltaP `6.063` edge `0.159` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.384` n `143` status `ready` deltaP `3.2474` edge `-0.0041` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4073` n `143` status `ready` deltaP `-1.2436` edge `-0.005` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5443` n `143` status `ready` deltaP `5.0657` edge `-0.0038` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6822` n `143` status `ready` deltaP `-4.738` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8964` n `143` status `ready` deltaP `-0.7632` edge `-0.0091` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9217` n `143` status `ready` deltaP `-0.3371` edge `0.0083` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.009` n `143` status `ready` deltaP `-1.6608` edge `-0.0174` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9863` n `143` status `ready` deltaP `-10.7324` edge `-0.0298` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5365` n `143` status `ready` deltaP `-1.2664` edge `-0.0692` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2802` n `143` status `ready` deltaP `-11.7353` edge `-0.0629` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.8765` n `143` status `ready` deltaP `-8.429` edge `-0.1012` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.1738` n `104` status `ready` deltaP `1.4557` edge `-0.1081` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.5208` n `104` status `ready` deltaP `-18.149` edge `-0.2781` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8185` n `143` status `ready` deltaP `-6.0938` edge `-0.5662` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
