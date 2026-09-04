# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T07:52:25.542887+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11478`

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

- `risk_on_high->unknown_4h` score `20.9545` n `133` status `ready` deltaP `8.5412` edge `1.7511` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.9545` n `133` status `ready` deltaP `8.5412` edge `1.7511` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `13.7327` n `178` status `ready` deltaP `11.4347` edge `1.1377` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.2756` n `133` status `ready` deltaP `-0.7542` edge `1.0857` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.2756` n `133` status `ready` deltaP `-0.7542` edge `1.0857` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.87` n `188` status `ready` deltaP `0.8536` edge `0.9632` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.591` n `159` status `ready` deltaP `16.837` edge `0.4549` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `1.1168` n `133` status `ready` deltaP `12.8081` edge `0.4222` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.1168` n `133` status `ready` deltaP `12.8081` edge `0.4222` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.4818` n `65` status `ready` deltaP `7.1599` edge `0.0403` maxDD `-0.7681`
- `risk_on_high->metal_1h` score `0.1117` n `133` status `ready` deltaP `12.2631` edge `0.0038` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1117` n `133` status `ready` deltaP `12.2631` edge `0.0038` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0418` n `65` status `ready` deltaP `4.977` edge `-0.0032` maxDD `-0.8275`
- `news_risk_high->commodity_24h` score `-0.1575` n `65` status `ready` deltaP `3.6351` edge `-0.0181` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.1657` n `65` status `ready` deltaP `4.5026` edge `0.0008` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1699` n `133` status `ready` deltaP `3.693` edge `-0.0019` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1699` n `133` status `ready` deltaP `3.693` edge `-0.0019` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.2474` n `133` status `ready` deltaP `4.751` edge `0.0494` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2474` n `133` status `ready` deltaP `4.751` edge `0.0494` maxDD `-5.4685`
- `market_context_high->metal_1h` score `-0.3326` n `188` status `ready` deltaP `6.332` edge `0.0008` maxDD `-2.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
