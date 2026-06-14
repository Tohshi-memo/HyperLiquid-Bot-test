# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T05:03:27.560613+00:00`
- Price records: `672`
- Market context records: `3860`
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

- `risk_on_high->unknown_4h` score `48.8417` n `72` status `ready` deltaP `8.0284` edge `6.4224` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.8417` n `72` status `ready` deltaP `8.0284` edge `6.4224` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.1866` n `32` status `ready` deltaP `34.0278` edge `2.6263` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.1866` n `32` status `ready` deltaP `34.0278` edge `2.6263` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9519` n `32` status `ready` deltaP `42.0139` edge `1.9659` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9519` n `32` status `ready` deltaP `42.0139` edge `1.9659` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5803` n `32` status `ready` deltaP `31.9444` edge `1.7672` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5803` n `32` status `ready` deltaP `31.9444` edge `1.7672` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3044` n `32` status `ready` deltaP `31.25` edge `0.7337` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3044` n `32` status `ready` deltaP `31.25` edge `0.7337` maxDD `0.0`
- `market_context_high->unknown_4h` score `8.169` n `206` status `ready` deltaP `0.1805` edge `1.587` maxDD `-35.6052`
- `market_context_high->unknown_24h` score `7.9666` n `129` status `ready` deltaP `-20.0339` edge `4.0031` maxDD `-200.1879`
- `market_context_high->equity_24h` score `6.8032` n `129` status `ready` deltaP `14.8821` edge `0.7707` maxDD `-14.5715`
- `market_context_high->index_24h` score `6.0421` n `129` status `ready` deltaP `25.8236` edge `0.4453` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.2958` n `72` status `ready` deltaP `18.5467` edge `0.4299` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.2958` n `72` status `ready` deltaP `18.5467` edge `0.4299` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.6637` n `129` status `ready` deltaP `20.9222` edge `0.309` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6157` n `72` status `ready` deltaP `25.8638` edge `0.159` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6157` n `72` status `ready` deltaP `25.8638` edge `0.159` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.6935` n `129` status `ready` deltaP `0.7187` edge `0.5827` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
