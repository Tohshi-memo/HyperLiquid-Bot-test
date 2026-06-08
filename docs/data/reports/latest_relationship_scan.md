# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T15:07:28.311520+00:00`
- Price records: `672`
- Market context records: `3290`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `11391`

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

- `risk_on_high->crypto_major_4h` score `15.7949` n `32` status `ready` deltaP `29.7256` edge `1.2303` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.7949` n `32` status `ready` deltaP `29.7256` edge `1.2303` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.5782` n `109` status `ready` deltaP `17.076` edge `2.6111` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `11.7865` n `109` status `ready` deltaP `42.7099` edge `0.7403` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.1351` n `109` status `ready` deltaP `29.9408` edge `0.8171` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.4333` n `32` status `ready` deltaP `10.8994` edge `0.7312` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4333` n `32` status `ready` deltaP `10.8994` edge `0.7312` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.5997` n `109` status `ready` deltaP `19.8506` edge `1.5554` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.7756` n `32` status `ready` deltaP `15.0152` edge `0.4974` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7756` n `32` status `ready` deltaP `15.0152` edge `0.4974` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.2322` n `169` status `ready` deltaP `19.6701` edge `0.1507` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `1.9746` n `32` status `ready` deltaP `6.4184` edge `0.3173` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.9746` n `32` status `ready` deltaP `6.4184` edge `0.3173` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.1245` n `32` status `ready` deltaP `1.1433` edge `0.1953` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.1245` n `32` status `ready` deltaP `1.1433` edge `0.1953` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `0.4276` n `109` status `ready` deltaP `17.3006` edge `2.0094` maxDD `-152.2601`
- `risk_on_high->commodity_4h` score `0.3211` n `32` status `ready` deltaP `9.2226` edge `0.052` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `0.3211` n `32` status `ready` deltaP `9.2226` edge `0.052` maxDD `-3.6044`
- `risk_on_high->metal_1h` score `0.2985` n `32` status `ready` deltaP `6.5494` edge `0.0631` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2985` n `32` status `ready` deltaP `6.5494` edge `0.0631` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
