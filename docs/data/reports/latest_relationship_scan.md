# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T20:52:28.778883+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10858`

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

- `market_context_high->metal_24h` score `1.4047` n `117` status `ready` deltaP `7.3585` edge `0.1256` maxDD `-2.2743`
- `market_context_high->equity_24h` score `1.2844` n `117` status `ready` deltaP `3.0182` edge `0.3929` maxDD `-21.1456`
- `market_context_high->commodity_4h` score `1.1486` n `143` status `ready` deltaP `14.7472` edge `0.0647` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7503` n `150` status `ready` deltaP `10.3533` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.599` n `117` status `ready` deltaP `20.633` edge `0.0259` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.0731` n `117` status `ready` deltaP `5.5823` edge `0.1253` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5065` n `150` status `ready` deltaP `1.6866` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.607` n `150` status `ready` deltaP `-3.3353` edge `-0.006` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7404` n `143` status `ready` deltaP `2.7791` edge `-0.0049` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.8162` n `150` status `ready` deltaP `-3.5389` edge `-0.0055` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.9574` n `143` status `ready` deltaP `-1.5254` edge `-0.0091` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9737` n `150` status `ready` deltaP `-0.507` edge `0.0051` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0217` n `143` status `ready` deltaP `-1.9657` edge `-0.017` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8404` n `150` status `ready` deltaP `-9.1177` edge `-0.0284` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.583` n `143` status `ready` deltaP `-2.0286` edge `-0.068` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2853` n `150` status `ready` deltaP `-12.0279` edge `-0.0606` maxDD `-7.3059`
- `market_context_high->crypto_alt_4h` score `-4.1304` n `143` status `ready` deltaP `-9.0387` edge `-0.1183` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.2755` n `117` status `ready` deltaP `1.7896` edge `-0.1188` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.6738` n `117` status `ready` deltaP `-16.3061` edge `-0.2198` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.908` n `150` status `ready` deltaP `-7.3333` edge `-0.5654` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
