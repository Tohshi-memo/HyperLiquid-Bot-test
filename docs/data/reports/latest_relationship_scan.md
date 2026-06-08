# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T16:07:29.088637+00:00`
- Price records: `672`
- Market context records: `3294`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13141`

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

- `risk_on_high->crypto_major_4h` score `15.8117` n `32` status `ready` deltaP `29.7256` edge `1.2317` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8117` n `32` status `ready` deltaP `29.7256` edge `1.2317` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.7699` n `112` status `ready` deltaP `17.7332` edge `2.6313` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `11.1612` n `112` status `ready` deltaP `40.2033` edge `0.7049` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.4527` n `112` status `ready` deltaP `30.506` edge `0.8398` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.5329` n `32` status `ready` deltaP `10.8994` edge `0.7395` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5329` n `32` status `ready` deltaP `10.8994` edge `0.7395` maxDD `-11.7537`
- `market_context_high->equity_24h` score `7.0273` n `112` status `ready` deltaP `20.8582` edge `1.6035` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.7302` n `32` status `ready` deltaP `14.8628` edge `0.4926` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7302` n `32` status `ready` deltaP `14.8628` edge `0.4926` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.1608` n `173` status `ready` deltaP `19.3324` edge `0.147` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `1.9637` n `32` status `ready` deltaP `6.2687` edge `0.3169` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.9637` n `32` status `ready` deltaP `6.2687` edge `0.3169` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.1245` n `32` status `ready` deltaP `1.1433` edge `0.1953` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.1245` n `32` status `ready` deltaP `1.1433` edge `0.1953` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `0.9257` n `112` status `ready` deltaP `18.1051` edge `2.0679` maxDD `-152.2601`
- `risk_on_high->metal_1h` score `0.2518` n `32` status `ready` deltaP `6.1003` edge `0.0601` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2518` n `32` status `ready` deltaP `6.1003` edge `0.0601` maxDD `-1.4793`
- `risk_on_high->commodity_4h` score `0.2438` n `32` status `ready` deltaP `8.7652` edge `0.0486` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `0.2438` n `32` status `ready` deltaP `8.7652` edge `0.0486` maxDD `-3.6044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
