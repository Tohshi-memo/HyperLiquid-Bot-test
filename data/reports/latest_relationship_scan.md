# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T19:37:29.048879+00:00`
- Price records: `672`
- Market context records: `3717`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13025`

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

- `risk_on_high->crypto_major_24h` score `29.657` n `32` status `ready` deltaP `31.4236` edge `2.2662` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.657` n `32` status `ready` deltaP `31.4236` edge `2.2662` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.3875` n `32` status `ready` deltaP `33.3333` edge `1.6434` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3875` n `32` status `ready` deltaP `33.3333` edge `1.6434` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.8001` n `32` status `ready` deltaP `30.9028` edge `1.6258` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.8001` n `32` status `ready` deltaP `30.9028` edge `1.6258` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.7944` n `32` status `ready` deltaP `33.1597` edge `0.7618` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.7944` n `32` status `ready` deltaP `33.1597` edge `0.7618` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.1487` n `32` status `ready` deltaP `17.378` edge `0.8421` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.1487` n `32` status `ready` deltaP `17.378` edge `0.8421` maxDD `-5.9781`
- `market_context_high->equity_24h` score `4.8027` n `161` status `ready` deltaP `15.942` edge `0.588` maxDD `-16.1913`
- `market_context_high->index_24h` score `4.6412` n `161` status `ready` deltaP `23.2218` edge `0.3459` maxDD `-7.1159`
- `risk_on_high->metal_24h` score `2.1349` n `32` status `ready` deltaP `18.5764` edge `0.0802` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.1349` n `32` status `ready` deltaP `18.5764` edge `0.0802` maxDD `-0.7574`
- `market_context_high->metal_24h` score `2.0163` n `161` status `ready` deltaP `18.7705` edge `0.2623` maxDD `-10.2193`
- `risk_on_high->crypto_alt_4h` score `1.8309` n `32` status `ready` deltaP `-0.9909` edge `0.3436` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.8309` n `32` status `ready` deltaP `-0.9909` edge `0.3436` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.583` n `32` status `ready` deltaP `8.4604` edge `0.26` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.583` n `32` status `ready` deltaP `8.4604` edge `0.26` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `0.9969` n `32` status `ready` deltaP `1.9274` edge `0.2219` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
