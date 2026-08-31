# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T00:37:25.881408+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `risk_on_high->crypto_alt_24h` score `20.7262` n `55` status `ready` deltaP `44.9747` edge `1.4754` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `20.7262` n `55` status `ready` deltaP `44.9747` edge `1.4754` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `9.4315` n `87` status `ready` deltaP `31.0362` edge `0.6219` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.4315` n `87` status `ready` deltaP `31.0362` edge `0.6219` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `7.7246` n `55` status `ready` deltaP `25.7418` edge `0.6139` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `7.7246` n `55` status `ready` deltaP `25.7418` edge `0.6139` maxDD `-9.0103`
- `risk_on_high->fx_24h` score `6.0919` n `55` status `ready` deltaP `68.2292` edge `0.0528` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.0919` n `55` status `ready` deltaP `68.2292` edge `0.0528` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.8013` n `149` status `ready` deltaP `21.054` edge `0.3901` maxDD `-1.0945`
- `market_context_high->crypto_major_24h` score `4.7543` n `114` status `ready` deltaP `19.3622` edge `0.5162` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `4.3732` n `92` status `ready` deltaP `11.8915` edge `0.3096` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.3732` n `92` status `ready` deltaP `11.8915` edge `0.3096` maxDD `-0.2885`
- `market_context_high->crypto_alt_24h` score `4.3725` n `114` status `ready` deltaP `20.5409` edge `0.8426` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.121` n `55` status `ready` deltaP `39.0183` edge `0.1305` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.121` n `55` status `ready` deltaP `39.0183` edge `0.1305` maxDD `-0.7767`
- `market_context_high->metal_24h` score `3.8718` n `114` status `ready` deltaP `30.8205` edge `0.2191` maxDD `-3.1535`
- `market_context_high->unknown_1h` score `3.1564` n `161` status `ready` deltaP `9.8728` edge `0.2381` maxDD `-0.9372`
- `risk_on_high->equity_24h` score `1.0163` n `55` status `ready` deltaP `18.7153` edge `0.0407` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `1.0163` n `55` status `ready` deltaP `18.7153` edge `0.0407` maxDD `-3.7955`
- `risk_on_high->commodity_24h` score `0.9472` n `55` status `ready` deltaP `10.5208` edge `0.1501` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
