# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T10:52:28.333151+00:00`
- Price records: `672`
- Market context records: `3885`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13645`

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

- `risk_on_high->unknown_4h` score `47.4086` n `72` status `ready` deltaP `5.8943` edge `6.2529` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.4086` n `72` status `ready` deltaP `5.8943` edge `6.2529` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.3954` n `32` status `ready` deltaP `34.0278` edge `2.6437` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.3954` n `32` status `ready` deltaP `34.0278` edge `2.6437` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8931` n `32` status `ready` deltaP `42.0139` edge `1.961` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8931` n `32` status `ready` deltaP `42.0139` edge `1.961` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2125` n `32` status `ready` deltaP `30.9028` edge `1.7435` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2125` n `32` status `ready` deltaP `30.9028` edge `1.7435` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1592` n `32` status `ready` deltaP `30.0347` edge `0.7297` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1592` n `32` status `ready` deltaP `30.0347` edge `0.7297` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.0989` n `205` status `ready` deltaP `-1.7073` edge `1.4624` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.3775` n `148` status `ready` deltaP `18.3653` edge `0.712` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.4304` n `72` status `ready` deltaP `19.6138` edge `0.434` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.4304` n `72` status `ready` deltaP `19.6138` edge `0.434` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.1006` n `148` status `ready` deltaP `25.305` edge `0.3703` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.513` n `148` status `ready` deltaP `22.5178` edge `0.2858` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4374` n `72` status `ready` deltaP `24.3394` edge `0.1543` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4374` n `72` status `ready` deltaP `24.3394` edge `0.1543` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3029` n `148` status `ready` deltaP `5.396` edge `0.6023` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `2.2334` n `205` status `ready` deltaP `14.6342` edge `0.265` maxDD `-9.4488`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
