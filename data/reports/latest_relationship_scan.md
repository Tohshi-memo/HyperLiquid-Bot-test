# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T14:52:25.380707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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

- `risk_on_high->unknown_24h` score `373.4118` n `93` status `ready` deltaP `24.6528` edge `30.9533` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `373.4118` n `93` status `ready` deltaP `24.6528` edge `30.9533` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.5456` n `93` status `ready` deltaP `39.6282` edge `1.6663` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.5456` n `93` status `ready` deltaP `39.6282` edge `1.6663` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.2318` n `93` status `ready` deltaP `32.1181` edge `1.0552` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.2318` n `93` status `ready` deltaP `32.1181` edge `1.0552` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.3827` n `203` status `ready` deltaP `24.7289` edge `0.5912` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.3169` n `117` status `ready` deltaP `28.8058` edge `0.2882` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3169` n `117` status `ready` deltaP `28.8058` edge `0.2882` maxDD `-1.9733`
- `market_context_high->equity_24h` score `5.0247` n `203` status `ready` deltaP `18.2292` edge `0.2972` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.5483` n `117` status `ready` deltaP `24.914` edge `0.2988` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.5483` n `117` status `ready` deltaP `24.914` edge `0.2988` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `4.3743` n `93` status `ready` deltaP `18.2292` edge `0.243` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.3743` n `93` status `ready` deltaP `18.2292` edge `0.243` maxDD `0.0`
- `risk_on_high->index_24h` score `2.2678` n `93` status `ready` deltaP `19.5173` edge `0.0631` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.2678` n `93` status `ready` deltaP `19.5173` edge `0.0631` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.485` n `203` status `ready` deltaP `13.8761` edge `0.0706` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8673` n `117` status `ready` deltaP `4.097` edge `0.0802` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8673` n `117` status `ready` deltaP `4.097` edge `0.0802` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7991` n `93` status `ready` deltaP `17.0139` edge `0.1046` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
