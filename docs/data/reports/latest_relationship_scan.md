# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T09:52:28.263808+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8030`

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

- `market_context_high->unknown_4h` score `30.6036` n `114` status `ready` deltaP `-3.0248` edge `2.6351` maxDD `-1.8373`
- `market_context_high->crypto_alt_24h` score `18.6224` n `47` status `ready` deltaP `16.5226` edge `1.6712` maxDD `-13.3586`
- `market_context_high->crypto_major_24h` score `13.2006` n `47` status `ready` deltaP `28.1545` edge `1.6803` maxDD `-9.0494`
- `risk_on_high->crypto_alt_4h` score `3.7596` n `48` status `ready` deltaP `18.1911` edge `0.2368` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.7596` n `48` status `ready` deltaP `18.1911` edge `0.2368` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4363` n `48` status `ready` deltaP `32.6728` edge `0.308` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4363` n `48` status `ready` deltaP `32.6728` edge `0.308` maxDD `-4.1548`
- `market_context_high->equity_24h` score `2.7531` n `47` status `ready` deltaP `4.8832` edge `0.4607` maxDD `-7.5571`
- `market_context_high->unknown_1h` score `1.9411` n `114` status `ready` deltaP `-4.6512` edge `0.2264` maxDD `-1.024`
- `market_context_high->index_24h` score `1.8417` n `47` status `ready` deltaP `26.2892` edge `0.1169` maxDD `-0.4833`
- `market_context_high->crypto_major_4h` score `1.2916` n `114` status `ready` deltaP `11.4008` edge `0.2384` maxDD `-10.8754`
- `risk_on_high->crypto_alt_1h` score `0.8112` n `48` status `ready` deltaP `5.6387` edge `0.0897` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8112` n `48` status `ready` deltaP `5.6387` edge `0.0897` maxDD `-2.4421`
- `market_context_high->crypto_alt_1h` score `0.7413` n `114` status `ready` deltaP `6.9545` edge `0.1105` maxDD `-4.9401`
- `market_context_high->crypto_alt_4h` score `0.4013` n `114` status `ready` deltaP `4.9235` edge `0.2422` maxDD `-13.3262`
- `risk_on_high->crypto_major_1h` score `0.3352` n `48` status `ready` deltaP `4.6158` edge `0.0775` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3352` n `48` status `ready` deltaP `4.6158` edge `0.0775` maxDD `-3.2233`
- `market_context_high->metal_24h` score `0.3337` n `47` status `ready` deltaP `11.8351` edge `0.0495` maxDD `-2.1826`
- `market_context_high->crypto_major_1h` score `0.1293` n `114` status `ready` deltaP `2.2035` edge `0.0782` maxDD `-3.4384`
- `market_context_high->metal_1h` score `-0.1563` n `114` status `ready` deltaP `4.9428` edge `0.0031` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
