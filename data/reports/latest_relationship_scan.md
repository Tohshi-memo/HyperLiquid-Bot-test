# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T02:07:34.464285+00:00`
- Price records: `672`
- Market context records: `3643`
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

- `risk_on_high->crypto_major_24h` score `37.9844` n `32` status `ready` deltaP `43.0556` edge `2.8826` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `37.9844` n `32` status `ready` deltaP `43.0556` edge `2.8826` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `34.5711` n `32` status `ready` deltaP `45.1389` edge `2.58` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `34.5711` n `32` status `ready` deltaP `45.1389` edge `2.58` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `30.2449` n `32` status `ready` deltaP `42.1875` edge `2.2543` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `30.2449` n `32` status `ready` deltaP `42.1875` edge `2.2543` maxDD `-0.8779`
- `risk_on_high->index_24h` score `19.6899` n `32` status `ready` deltaP `45.1389` edge `1.3399` maxDD `0.0`
- `risk_on_and_context->index_24h` score `19.6899` n `32` status `ready` deltaP `45.1389` edge `1.3399` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.9214` n `32` status `ready` deltaP `21.3415` edge `0.9634` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.9214` n `32` status `ready` deltaP `21.3415` edge `0.9634` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `11.7387` n `32` status `ready` deltaP `30.7292` edge `0.7995` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `11.7387` n `32` status `ready` deltaP `30.7292` edge `0.7995` maxDD `-0.7574`
- `market_context_high->equity_24h` score `10.2832` n `157` status `ready` deltaP `22.209` edge `1.2753` maxDD `-35.3144`
- `market_context_high->index_24h` score `9.2939` n `157` status `ready` deltaP `30.4892` edge `0.7428` maxDD `-11.3924`
- `market_context_high->crypto_major_24h` score `3.9794` n `157` status `ready` deltaP `9.2379` edge `0.9767` maxDD `-49.5335`
- `market_context_high->metal_24h` score `3.8493` n `157` status `ready` deltaP `25.0365` edge `0.7218` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `3.3982` n `32` status `ready` deltaP `1.9055` edge `0.4549` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.3982` n `32` status `ready` deltaP `1.9055` edge `0.4549` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.5752` n `32` status `ready` deltaP `10.2896` edge `0.375` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5752` n `32` status `ready` deltaP `10.2896` edge `0.375` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
