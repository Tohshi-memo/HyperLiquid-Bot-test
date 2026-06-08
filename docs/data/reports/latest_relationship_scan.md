# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T00:37:25.355184+00:00`
- Price records: `672`
- Market context records: `3232`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.6238` n `103` status `ready` deltaP `20.0394` edge `2.7254` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.861` n `103` status `ready` deltaP `50.2512` edge `0.8629` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.8898` n `103` status `ready` deltaP `33.2255` edge `0.8581` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.9143` n `103` status `ready` deltaP `20.7845` edge `1.5895` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `3.1927` n `103` status `ready` deltaP `24.11` edge `2.3185` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `2.3578` n `130` status `ready` deltaP `18.3232` edge `0.1476` maxDD `-2.8619`
- `risk_on_high->crypto_major_1h` score `2.3049` n `30` status `ready` deltaP `9.3213` edge `0.3403` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.3049` n `30` status `ready` deltaP `9.3213` edge `0.3403` maxDD `-5.8885`
- `risk_on_high->metal_1h` score `0.3483` n `30` status `ready` deltaP `6.517` edge `0.0697` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3483` n `30` status `ready` deltaP `6.517` edge `0.0697` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.3474` n `30` status `ready` deltaP `2.2455` edge `0.1733` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.3474` n `30` status `ready` deltaP `2.2455` edge `0.1733` maxDD `-8.1649`
- `risk_on_high->equity_1h` score `-0.0154` n `30` status `ready` deltaP `0.7485` edge `0.0834` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `-0.0154` n `30` status `ready` deltaP `0.7485` edge `0.0834` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.2925` n `30` status `ready` deltaP `-1.5369` edge `0.0351` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.2925` n `30` status `ready` deltaP `-1.5369` edge `0.0351` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.3093` n `142` status `ready` deltaP `3.8205` edge `0.0186` maxDD `-2.2543`
- `market_context_high->index_1h` score `-0.504` n `142` status `ready` deltaP `3.9091` edge `0.0156` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.7207` n `130` status `ready` deltaP `9.7374` edge `0.1016` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.7484` n `142` status `ready` deltaP `3.8753` edge `0.1045` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
