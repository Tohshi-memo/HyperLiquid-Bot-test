# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T10:37:29.773154+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9226`

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

- `market_context_high->equity_24h` score `8.3421` n `33` status `ready` deltaP `14.6939` edge `0.8345` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.1503` n `33` status `ready` deltaP `5.8397` edge `0.199` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.2181` n `33` status `ready` deltaP `14.5834` edge `0.1052` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.639` n `33` status `ready` deltaP `10.1326` edge `-0.0048` maxDD `-0.0933`
- `market_context_high->metal_1h` score `-0.3401` n `88` status `ready` deltaP `3.9467` edge `0.013` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4805` n `88` status `ready` deltaP `0.7417` edge `0.0017` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7157` n `86` status `ready` deltaP `-1.2372` edge `0.0271` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.7939` n `86` status `ready` deltaP `3.5841` edge `0.0077` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.8788` n `88` status `ready` deltaP `-5.709` edge `0.0085` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.921` n `86` status `ready` deltaP `0.2659` edge `0.0135` maxDD `-4.0015`
- `market_context_high->equity_1h` score `-1.2392` n `88` status `ready` deltaP `-5.709` edge `0.0628` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.2805` n `88` status `ready` deltaP `-13.4594` edge `-0.006` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.783` n `88` status `ready` deltaP `1.531` edge `-0.0409` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.8488` n `33` status `ready` deltaP `-1.8624` edge `-0.1693` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.2471` n `86` status `ready` deltaP `-8.9195` edge `-0.0105` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.045` n `88` status `ready` deltaP `-4.212` edge `-0.1` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-4.7415` n `86` status `ready` deltaP `1.7335` edge `-0.0287` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-5.7041` n `33` status `ready` deltaP `-5.8081` edge `-0.0228` maxDD `-26.7724`
- `market_context_high->crypto_alt_4h` score `-8.3714` n `86` status `ready` deltaP `2.4745` edge `-0.2023` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-9.9032` n `33` status `ready` deltaP `-19.4129` edge `-0.2127` maxDD `-31.6515`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
