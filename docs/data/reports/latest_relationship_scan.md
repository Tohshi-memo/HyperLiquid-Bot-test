# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T00:07:28.041514+00:00`
- Price records: `672`
- Market context records: `3736`
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

- `risk_on_high->crypto_major_24h` score `28.7874` n `32` status `ready` deltaP `29.6875` edge `2.2053` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.7874` n `32` status `ready` deltaP `29.6875` edge `2.2053` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.2375` n `32` status `ready` deltaP `33.3333` edge `1.6309` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.2375` n `32` status `ready` deltaP `33.3333` edge `1.6309` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.2613` n `32` status `ready` deltaP `30.9028` edge `1.5809` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.2613` n `32` status `ready` deltaP `30.9028` edge `1.5809` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5833` n `32` status `ready` deltaP `32.2917` edge `0.75` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5833` n `32` status `ready` deltaP `32.2917` edge `0.75` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.3503` n `32` status `ready` deltaP `18.2927` edge `0.8528` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.3503` n `32` status `ready` deltaP `18.2927` edge `0.8528` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.9448` n `156` status `ready` deltaP `18.5897` edge `0.6692` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.219` n `156` status `ready` deltaP `25.2404` edge `0.3806` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `4.3689` n `156` status `ready` deltaP `6.5304` edge `0.7669` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.2613` n `156` status `ready` deltaP `25.7212` edge `0.3268` maxDD `-9.1203`
- `risk_on_high->crypto_alt_4h` score `1.8618` n `32` status `ready` deltaP `-0.2287` edge `0.3411` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.8618` n `32` status `ready` deltaP `-0.2287` edge `0.3411` maxDD `-11.7537`
- `risk_on_high->metal_24h` score `1.5856` n `32` status `ready` deltaP `15.625` edge `0.0541` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.5856` n `32` status `ready` deltaP `15.625` edge `0.0541` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.4003` n `32` status `ready` deltaP `8.1555` edge `0.2386` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4003` n `32` status `ready` deltaP `8.1555` edge `0.2386` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
