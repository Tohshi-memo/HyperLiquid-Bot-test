# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T21:37:28.314569+00:00`
- Price records: `672`
- Market context records: `3726`
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

- `risk_on_high->crypto_major_24h` score `29.2106` n `32` status `ready` deltaP `30.2083` edge `2.2371` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.2106` n `32` status `ready` deltaP `30.2083` edge `2.2371` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.2987` n `32` status `ready` deltaP `33.3333` edge `1.636` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.2987` n `32` status `ready` deltaP `33.3333` edge `1.636` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.5601` n `32` status `ready` deltaP `30.9028` edge `1.6058` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.5601` n `32` status `ready` deltaP `30.9028` edge `1.6058` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.6958` n `32` status `ready` deltaP `32.8125` edge `0.7559` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.6958` n `32` status `ready` deltaP `32.8125` edge `0.7559` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.3515` n `32` status `ready` deltaP `18.2927` edge `0.8529` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.3515` n `32` status `ready` deltaP `18.2927` edge `0.8529` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.734` n `156` status `ready` deltaP `18.5897` edge `0.6558` maxDD `-12.8184`
- `market_context_high->index_24h` score `4.9149` n `156` status `ready` deltaP `23.8381` edge `0.3646` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `3.2283` n `156` status `ready` deltaP `5.1282` edge `0.6812` maxDD `-31.0425`
- `market_context_high->metal_24h` score `3.1427` n `156` status `ready` deltaP `21.5144` edge `0.2908` maxDD `-9.1203`
- `risk_on_high->crypto_alt_4h` score `2.0336` n `32` status `ready` deltaP `-0.0762` edge `0.3544` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.0336` n `32` status `ready` deltaP `-0.0762` edge `0.3544` maxDD `-11.7537`
- `risk_on_high->metal_24h` score `1.8726` n `32` status `ready` deltaP `17.1875` edge `0.0676` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.8726` n `32` status `ready` deltaP `17.1875` edge `0.0676` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.5997` n `32` status `ready` deltaP `8.7652` edge `0.2601` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5997` n `32` status `ready` deltaP `8.7652` edge `0.2601` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
