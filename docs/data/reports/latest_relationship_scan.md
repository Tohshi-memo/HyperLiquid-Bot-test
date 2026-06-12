# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T00:22:33.296471+00:00`
- Price records: `672`
- Market context records: `3635`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13161`

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

- `risk_on_high->crypto_major_24h` score `39.2948` n `32` status `ready` deltaP `44.2708` edge `2.9837` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `39.2948` n `32` status `ready` deltaP `44.2708` edge `2.9837` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `36.0495` n `32` status `ready` deltaP `46.3542` edge `2.6951` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `36.0495` n `32` status `ready` deltaP `46.3542` edge `2.6951` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `31.6609` n `32` status `ready` deltaP `43.4028` edge `2.3642` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `31.6609` n `32` status `ready` deltaP `43.4028` edge `2.3642` maxDD `-0.8779`
- `risk_on_high->index_24h` score `20.6259` n `32` status `ready` deltaP `46.3542` edge `1.4098` maxDD `0.0`
- `risk_on_and_context->index_24h` score `20.6259` n `32` status `ready` deltaP `46.3542` edge `1.4098` maxDD `0.0`
- `risk_on_high->metal_24h` score `12.8463` n `32` status `ready` deltaP `31.9444` edge `0.8837` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `12.8463` n `32` status `ready` deltaP `31.9444` edge `0.8837` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.1536` n `32` status `ready` deltaP `21.7988` edge `0.9797` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.1536` n `32` status `ready` deltaP `21.7988` edge `0.9797` maxDD `-5.9781`
- `market_context_high->equity_24h` score `11.7616` n `157` status `ready` deltaP `23.4243` edge `1.3904` maxDD `-35.3144`
- `market_context_high->index_24h` score `10.2299` n `157` status `ready` deltaP `31.7045` edge `0.8127` maxDD `-11.3924`
- `market_context_high->crypto_major_24h` score `5.2898` n `157` status `ready` deltaP `10.4531` edge `1.0778` maxDD `-49.5335`
- `market_context_high->metal_24h` score `4.5692` n `157` status `ready` deltaP `26.2517` edge `0.806` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `3.629` n `32` status `ready` deltaP `2.2104` edge `0.4721` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.629` n `32` status `ready` deltaP `2.2104` edge `0.4721` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.6301` n `32` status `ready` deltaP `10.747` edge `0.379` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6301` n `32` status `ready` deltaP `10.747` edge `0.379` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
