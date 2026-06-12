# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T02:22:32.787035+00:00`
- Price records: `672`
- Market context records: `3644`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `37.7809` n `32` status `ready` deltaP `42.8819` edge `2.8668` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `37.7809` n `32` status `ready` deltaP `42.8819` edge `2.8668` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `34.328` n `32` status `ready` deltaP `44.9653` edge `2.5609` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `34.328` n `32` status `ready` deltaP `44.9653` edge `2.5609` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `30.0282` n `32` status `ready` deltaP `42.0139` edge `2.2374` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `30.0282` n `32` status `ready` deltaP `42.0139` edge `2.2374` maxDD `-0.8779`
- `risk_on_high->index_24h` score `19.5464` n `32` status `ready` deltaP `44.9653` edge `1.3291` maxDD `0.0`
- `risk_on_and_context->index_24h` score `19.5464` n `32` status `ready` deltaP `44.9653` edge `1.3291` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.8722` n `32` status `ready` deltaP `21.3415` edge `0.9593` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.8722` n `32` status `ready` deltaP `21.3415` edge `0.9593` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `11.582` n `32` status `ready` deltaP `30.5556` edge `0.7876` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `11.582` n `32` status `ready` deltaP `30.5556` edge `0.7876` maxDD `-0.7574`
- `market_context_high->equity_24h` score `10.0401` n `157` status `ready` deltaP `22.0354` edge `1.2562` maxDD `-35.3144`
- `market_context_high->index_24h` score `9.1504` n `157` status `ready` deltaP `30.3156` edge `0.732` maxDD `-11.3924`
- `market_context_high->crypto_major_24h` score `3.7759` n `157` status `ready` deltaP `9.0642` edge `0.9609` maxDD `-49.5335`
- `market_context_high->metal_24h` score `3.7474` n `157` status `ready` deltaP `24.8629` edge `0.7099` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `3.3332` n `32` status `ready` deltaP `1.753` edge `0.4505` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.3332` n `32` status `ready` deltaP `1.753` edge `0.4505` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.561` n `32` status `ready` deltaP `10.1372` edge `0.3742` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.561` n `32` status `ready` deltaP `10.1372` edge `0.3742` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
