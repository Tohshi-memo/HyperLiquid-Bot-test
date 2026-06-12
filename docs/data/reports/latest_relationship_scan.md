# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T03:52:25.697280+00:00`
- Price records: `672`
- Market context records: `3650`
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

- `risk_on_high->crypto_major_24h` score `36.6932` n `32` status `ready` deltaP `41.8403` edge `2.7831` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `36.6932` n `32` status `ready` deltaP `41.8403` edge `2.7831` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `32.8527` n `32` status `ready` deltaP `43.9236` edge `2.4449` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `32.8527` n `32` status `ready` deltaP `43.9236` edge `2.4449` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `28.8541` n `32` status `ready` deltaP `40.9722` edge `2.1465` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `28.8541` n `32` status `ready` deltaP `40.9722` edge `2.1465` maxDD `-0.8779`
- `risk_on_high->index_24h` score `18.6771` n `32` status `ready` deltaP `43.9236` edge `1.2636` maxDD `0.0`
- `risk_on_and_context->index_24h` score `18.6771` n `32` status `ready` deltaP `43.9236` edge `1.2636` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.479` n `32` status `ready` deltaP `20.7317` edge `0.9306` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.479` n `32` status `ready` deltaP `20.7317` edge `0.9306` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `10.5483` n `32` status `ready` deltaP `29.5139` edge `0.7084` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `10.5483` n `32` status `ready` deltaP `29.5139` edge `0.7084` maxDD `-0.7574`
- `market_context_high->equity_24h` score `8.5647` n `157` status `ready` deltaP `20.9937` edge `1.1402` maxDD `-35.3144`
- `market_context_high->index_24h` score `8.2811` n `157` status `ready` deltaP `29.2739` edge `0.6665` maxDD `-11.3924`
- `market_context_high->metal_24h` score `3.0755` n `157` status `ready` deltaP `23.8212` edge `0.6307` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `2.8484` n `32` status `ready` deltaP `0.8384` edge `0.4162` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.8484` n `32` status `ready` deltaP `0.8384` edge `0.4162` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `2.6882` n `157` status `ready` deltaP `8.0226` edge `0.8772` maxDD `-49.5335`
- `risk_on_high->equity_4h` score `2.451` n `32` status `ready` deltaP `9.2226` edge `0.3662` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.451` n `32` status `ready` deltaP `9.2226` edge `0.3662` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
