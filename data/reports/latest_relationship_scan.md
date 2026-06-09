# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T21:52:22.262373+00:00`
- Price records: `672`
- Market context records: `3422`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13116`

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

- `risk_on_high->crypto_alt_24h` score `56.0589` n `32` status `ready` deltaP `59.0278` edge `4.2932` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.0589` n `32` status `ready` deltaP `59.0278` edge `4.2932` maxDD `-0.8779`
- `risk_on_high->crypto_major_24h` score `55.9958` n `32` status `ready` deltaP `58.3333` edge `4.2817` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.9958` n `32` status `ready` deltaP `58.3333` edge `4.2817` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `45.6617` n `32` status `ready` deltaP `56.0764` edge `3.4313` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.6617` n `32` status `ready` deltaP `56.0764` edge `3.4313` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9399` n `32` status `ready` deltaP `51.3889` edge `1.6524` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9399` n `32` status `ready` deltaP `51.3889` edge `1.6524` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.2847` n `154` status `ready` deltaP `19.945` edge `2.52` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.1183` n `154` status `ready` deltaP `24.4453` edge `2.37` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.4429` n `154` status `ready` deltaP `33.3491` edge `2.1225` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `14.66` n `32` status `ready` deltaP `26.2195` edge `1.1591` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.66` n `32` status `ready` deltaP `26.2195` edge `1.1591` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.371` n `32` status `ready` deltaP `28.9931` edge `0.9471` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.371` n `32` status `ready` deltaP `28.9931` edge `0.9471` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.7472` n `154` status `ready` deltaP `36.4538` edge `1.0409` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.3078` n `32` status `ready` deltaP `6.3262` edge `0.6679` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.3078` n `32` status `ready` deltaP `6.3262` edge `0.6679` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.4303` n `154` status `ready` deltaP `23.8795` edge `0.8628` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.2932` n `32` status `ready` deltaP `16.5396` edge `0.5536` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
