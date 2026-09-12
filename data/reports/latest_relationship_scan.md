# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T17:22:29.431915+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12899`

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

- `market_context_high->unknown_24h` score `7643.0582` n `86` status `ready` deltaP `13.1258` edge `636.8392` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `5354.4157` n `43` status `ready` deltaP `15.4514` edge `446.0983` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5354.4157` n `43` status `ready` deltaP `15.4514` edge `446.0983` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.0043` n `82` status `ready` deltaP `-5.2505` edge `31.9942` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `22.0064` n `65` status `ready` deltaP `48.6779` edge `1.609` maxDD `-5.9719`
- `news_risk_high->crypto_alt_24h` score `16.9897` n `65` status `ready` deltaP `28.6351` edge `1.2737` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.5791` n `43` status `ready` deltaP `38.5457` edge `1.1476` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.5791` n `43` status `ready` deltaP `38.5457` edge `1.1476` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.7351` n `86` status `ready` deltaP `31.5689` edge `1.1002` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `10.5029` n `65` status `ready` deltaP `28.3173` edge `0.7346` maxDD `-1.8513`
- `risk_on_high->equity_24h` score `9.6328` n `43` status `ready` deltaP `40.625` edge `0.5319` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.6328` n `43` status `ready` deltaP `40.625` edge `0.5319` maxDD `0.0`
- `market_context_high->equity_24h` score `9.2644` n `86` status `ready` deltaP `40.625` edge `0.5012` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4832` n `44` status `ready` deltaP `41.505` edge `0.4674` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4832` n `44` status `ready` deltaP `41.505` edge `0.4674` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.2015` n `65` status `ready` deltaP `47.1928` edge `0.299` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `7.1015` n `65` status `ready` deltaP `45.2831` edge `0.3196` maxDD `-0.3759`
- `risk_on_high->index_24h` score `4.8962` n `43` status `ready` deltaP `49.4469` edge `0.0826` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8962` n `43` status `ready` deltaP `49.4469` edge `0.0826` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.128` n `44` status `ready` deltaP `36.1835` edge `0.1121` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
