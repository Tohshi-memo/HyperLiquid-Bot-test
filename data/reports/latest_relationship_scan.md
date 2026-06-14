# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T05:37:32.222042+00:00`
- Price records: `672`
- Market context records: `3863`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13683`

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

- `risk_on_high->unknown_4h` score `48.8019` n `72` status `ready` deltaP `8.0284` edge `6.4173` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.8019` n `72` status `ready` deltaP `8.0284` edge `6.4173` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.195` n `32` status `ready` deltaP `34.0278` edge `2.627` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.195` n `32` status `ready` deltaP `34.0278` edge `2.627` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9531` n `32` status `ready` deltaP `42.0139` edge `1.966` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9531` n `32` status `ready` deltaP `42.0139` edge `1.966` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5383` n `32` status `ready` deltaP `31.9444` edge `1.7637` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5383` n `32` status `ready` deltaP `31.9444` edge `1.7637` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2972` n `32` status `ready` deltaP `31.25` edge `0.7331` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2972` n `32` status `ready` deltaP `31.25` edge `0.7331` maxDD `0.0`
- `market_context_high->unknown_4h` score `8.1292` n `206` status `ready` deltaP `0.1805` edge `1.5819` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.7692` n `131` status `ready` deltaP `15.2963` edge `0.7651` maxDD `-14.5715`
- `market_context_high->unknown_24h` score `6.5255` n `131` status `ready` deltaP `-20.5073` edge `3.8215` maxDD `-200.1879`
- `market_context_high->index_24h` score `5.9443` n `131` status `ready` deltaP `25.9065` edge `0.4366` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.4198` n `72` status `ready` deltaP `18.8516` edge `0.4382` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.4198` n `72` status `ready` deltaP `18.8516` edge `0.4382` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.6166` n `131` status `ready` deltaP `20.9182` edge `0.3051` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6605` n `72` status `ready` deltaP `26.1687` edge `0.1607` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6605` n `72` status `ready` deltaP `26.1687` edge `0.1607` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.8664` n `131` status `ready` deltaP `1.2749` edge `0.5934` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
