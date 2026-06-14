# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T05:22:35.031714+00:00`
- Price records: `672`
- Market context records: `3862`
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

- `risk_on_high->unknown_4h` score `48.8214` n `72` status `ready` deltaP `8.0284` edge `6.4198` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.8214` n `72` status `ready` deltaP `8.0284` edge `6.4198` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.1902` n `32` status `ready` deltaP `34.0278` edge `2.6266` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.1902` n `32` status `ready` deltaP `34.0278` edge `2.6266` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9543` n `32` status `ready` deltaP `42.0139` edge `1.9661` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9543` n `32` status `ready` deltaP `42.0139` edge `1.9661` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5599` n `32` status `ready` deltaP `31.9444` edge `1.7655` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5599` n `32` status `ready` deltaP `31.9444` edge `1.7655` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3008` n `32` status `ready` deltaP `31.25` edge `0.7334` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3008` n `32` status `ready` deltaP `31.25` edge `0.7334` maxDD `0.0`
- `market_context_high->unknown_4h` score `8.1487` n `206` status `ready` deltaP `0.1805` edge `1.5844` maxDD `-35.6052`
- `market_context_high->unknown_24h` score `7.2413` n `130` status `ready` deltaP `-20.2725` edge `3.9117` maxDD `-200.1879`
- `market_context_high->equity_24h` score `6.7899` n `130` status `ready` deltaP `15.0908` edge `0.7682` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.9938` n `130` status `ready` deltaP `25.8654` edge `0.441` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.3632` n `72` status `ready` deltaP `18.6992` edge `0.4345` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.3632` n `72` status `ready` deltaP `18.6992` edge `0.4345` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.6481` n `130` status `ready` deltaP `20.9215` edge `0.3077` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6387` n `72` status `ready` deltaP `26.0162` edge `0.1599` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6387` n `72` status `ready` deltaP `26.0162` edge `0.1599` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.7831` n `130` status `ready` deltaP `0.999` edge `0.5883` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
