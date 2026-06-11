# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T05:22:29.488498+00:00`
- Price records: `672`
- Market context records: `3554`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13202`

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

- `risk_on_high->crypto_major_24h` score `51.7717` n `32` status `ready` deltaP `56.667` edge `3.9408` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `51.7717` n `32` status `ready` deltaP `56.667` edge `3.9408` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `46.4619` n `32` status `ready` deltaP `56.3204` edge `3.5115` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `46.4619` n `32` status `ready` deltaP `56.3204` edge `3.5115` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.7262` n `32` status `ready` deltaP `54.0728` edge `3.3667` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.7262` n `32` status `ready` deltaP `54.0728` edge `3.3667` maxDD `0.0`
- `risk_on_high->index_24h` score `25.6036` n `32` status `ready` deltaP `53.8995` edge `1.7743` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.6036` n `32` status `ready` deltaP `53.8995` edge `1.7743` maxDD `0.0`
- `market_context_high->equity_24h` score `19.0823` n `156` status `ready` deltaP `30.9959` edge `2.0248` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6427` n `32` status `ready` deltaP `37.0342` edge `1.3328` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6427` n `32` status `ready` deltaP `37.0342` edge `1.3328` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `16.3376` n `156` status `ready` deltaP `21.9715` edge `1.9881` maxDD `-54.8486`
- `market_context_high->index_24h` score `14.2189` n `156` status `ready` deltaP `38.5149` edge `1.1498` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `14.0498` n `32` status `ready` deltaP `26.6768` edge `1.1052` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.0498` n `32` status `ready` deltaP `26.6768` edge `1.1052` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.3748` n `156` status `ready` deltaP `16.4967` edge `1.7255` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6093` n `156` status `ready` deltaP `31.1047` edge `1.2222` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.651` n `32` status `ready` deltaP `6.936` edge `0.6091` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.651` n `32` status `ready` deltaP `6.936` edge `0.6091` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.8444` n `32` status `ready` deltaP `16.0823` edge `0.4991` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
