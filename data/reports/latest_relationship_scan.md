# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T07:22:30.826062+00:00`
- Price records: `672`
- Market context records: `3870`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13656`

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

- `risk_on_high->unknown_4h` score `48.4162` n `72` status `ready` deltaP `7.5711` edge `6.3709` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.4162` n `72` status `ready` deltaP `7.5711` edge `6.3709` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.2514` n `32` status `ready` deltaP `34.0278` edge `2.6317` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.2514` n `32` status `ready` deltaP `34.0278` edge `2.6317` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8655` n `32` status `ready` deltaP `42.0139` edge `1.9587` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8655` n `32` status `ready` deltaP `42.0139` edge `1.9587` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2955` n `32` status `ready` deltaP `31.25` edge `1.7481` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2955` n `32` status `ready` deltaP `31.25` edge `1.7481` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.152` n `32` status `ready` deltaP `30.0347` edge `0.7291` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.152` n `32` status `ready` deltaP `30.0347` edge `0.7291` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.7435` n `206` status `ready` deltaP `-0.2768` edge `1.5355` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.5788` n `138` status `ready` deltaP `16.6516` edge `0.7402` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.6104` n `72` status `ready` deltaP `19.6138` edge `0.449` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.6104` n `72` status `ready` deltaP `19.6138` edge `0.449` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.516` n `138` status `ready` deltaP `24.9622` edge `0.4072` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.4232` n `138` status `ready` deltaP `20.8258` edge `0.2896` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6167` n `72` status `ready` deltaP `25.7113` edge `0.1601` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6167` n `72` status `ready` deltaP `25.7113` edge `0.1601` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3108` n `138` status `ready` deltaP `3.0948` edge `0.6183` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.9488` n `206` status `ready` deltaP `13.3436` edge `0.2635` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
