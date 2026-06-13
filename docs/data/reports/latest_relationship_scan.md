# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T00:52:27.930176+00:00`
- Price records: `672`
- Market context records: `3739`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13153`

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

- `risk_on_high->crypto_major_24h` score `28.6998` n `32` status `ready` deltaP `29.6875` edge `2.198` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.6998` n `32` status `ready` deltaP `29.6875` edge `2.198` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.2651` n `32` status `ready` deltaP `33.3333` edge `1.6332` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.2651` n `32` status `ready` deltaP `33.3333` edge `1.6332` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.2025` n `32` status `ready` deltaP `30.9028` edge `1.576` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.2025` n `32` status `ready` deltaP `30.9028` edge `1.576` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5033` n `32` status `ready` deltaP `31.7708` edge `0.7468` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5033` n `32` status `ready` deltaP `31.7708` edge `0.7468` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.2207` n `32` status `ready` deltaP `18.2927` edge `0.842` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.2207` n `32` status `ready` deltaP `18.2927` edge `0.842` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.7228` n `156` status `ready` deltaP `18.5897` edge `0.6632` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.4332` n `156` status `ready` deltaP `26.6426` edge `0.3891` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `4.6029` n `156` status `ready` deltaP `6.5304` edge `0.7864` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.4826` n `156` status `ready` deltaP `27.1234` edge `0.3359` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.6828` n `169` status `ready` deltaP `8.7143` edge `0.2722` maxDD `-10.5381`
- `risk_on_high->crypto_alt_4h` score `1.6289` n `32` status `ready` deltaP `-0.3811` edge `0.3227` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.6289` n `32` status `ready` deltaP `-0.3811` edge `0.3227` maxDD `-11.7537`
- `risk_on_high->metal_24h` score `1.5043` n `32` status `ready` deltaP `15.1042` edge `0.0508` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.5043` n `32` status `ready` deltaP `15.1042` edge `0.0508` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.3039` n `32` status `ready` deltaP `7.6982` edge `0.2293` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
