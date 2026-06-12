# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T05:37:26.432973+00:00`
- Price records: `672`
- Market context records: `3657`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13201`

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

- `risk_on_high->crypto_major_24h` score `35.3276` n `32` status `ready` deltaP `40.625` edge `2.6774` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `35.3276` n `32` status `ready` deltaP `40.625` edge `2.6774` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `31.2039` n `32` status `ready` deltaP `42.7083` edge `2.3156` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `31.2039` n `32` status `ready` deltaP `42.7083` edge `2.3156` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `27.3541` n `32` status `ready` deltaP `39.7569` edge `2.0296` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `27.3541` n `32` status `ready` deltaP `39.7569` edge `2.0296` maxDD `-0.8779`
- `risk_on_high->index_24h` score `17.6847` n `32` status `ready` deltaP `42.7083` edge `1.189` maxDD `0.0`
- `risk_on_and_context->index_24h` score `17.6847` n `32` status `ready` deltaP `42.7083` edge `1.189` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.1947` n `32` status `ready` deltaP `19.8171` edge `0.913` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.1947` n `32` status `ready` deltaP `19.8171` edge `0.913` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `9.3891` n `32` status `ready` deltaP `28.2986` edge `0.6199` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `9.3891` n `32` status `ready` deltaP `28.2986` edge `0.6199` maxDD `-0.7574`
- `market_context_high->index_24h` score `7.2886` n `157` status `ready` deltaP `28.0586` edge `0.5919` maxDD `-11.3924`
- `market_context_high->equity_24h` score `6.9159` n `157` status `ready` deltaP `19.7784` edge `1.0109` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.4672` n `32` status `ready` deltaP `0.2287` edge `0.3885` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.4672` n `32` status `ready` deltaP `0.2287` edge `0.3885` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.4542` n `32` status `ready` deltaP `9.2226` edge `0.3666` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4542` n `32` status `ready` deltaP `9.2226` edge `0.3666` maxDD `-5.7426`
- `market_context_high->metal_24h` score `2.322` n `157` status `ready` deltaP `22.6059` edge `0.5422` maxDD `-21.6171`
- `market_context_high->crypto_major_24h` score `1.3226` n `157` status `ready` deltaP `6.8073` edge `0.7715` maxDD `-49.5335`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
