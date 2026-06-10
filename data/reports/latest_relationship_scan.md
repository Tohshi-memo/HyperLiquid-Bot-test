# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T15:37:32.199503+00:00`
- Price records: `672`
- Market context records: `3496`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13142`

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

- `risk_on_high->crypto_major_24h` score `54.677` n `32` status `ready` deltaP `58.3333` edge `4.1718` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `54.677` n `32` status `ready` deltaP `58.3333` edge `4.1718` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `51.7105` n `32` status `ready` deltaP `58.5069` edge `3.9343` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `51.7105` n `32` status `ready` deltaP `58.5069` edge `3.9343` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.7514` n `32` status `ready` deltaP `55.9028` edge `3.3566` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.7514` n `32` status `ready` deltaP `55.9028` edge `3.3566` maxDD `0.0`
- `risk_on_high->index_24h` score `24.5123` n `32` status `ready` deltaP `51.3889` edge `1.7001` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.5123` n `32` status `ready` deltaP `51.3889` edge `1.7001` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `19.4814` n `155` status `ready` deltaP `24.0389` edge `2.2363` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.164` n `155` status `ready` deltaP `32.677` edge `2.0204` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `17.8036` n `155` status `ready` deltaP `19.0513` edge `2.1567` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `15.9807` n `32` status `ready` deltaP `30.7292` edge `1.153` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.9807` n `32` status `ready` deltaP `30.7292` edge `1.153` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.0134` n `32` status `ready` deltaP `28.5061` edge `1.1733` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.0134` n `32` status `ready` deltaP `28.5061` edge `1.1733` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1389` n `155` status `ready` deltaP `35.905` edge `1.0772` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.3185` n `32` status `ready` deltaP `9.375` edge `0.7318` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3185` n `32` status `ready` deltaP `9.375` edge `0.7318` maxDD `-11.7537`
- `market_context_high->metal_24h` score `5.9609` n `155` status `ready` deltaP `25.205` edge `1.0502` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.0263` n `32` status `ready` deltaP `17.3018` edge `0.5143` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
