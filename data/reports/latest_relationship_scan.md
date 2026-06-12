# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T19:52:34.605507+00:00`
- Price records: `672`
- Market context records: `3718`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13025`

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

- `risk_on_high->crypto_major_24h` score `29.6546` n `32` status `ready` deltaP `31.4236` edge `2.266` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.6546` n `32` status `ready` deltaP `31.4236` edge `2.266` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.3707` n `32` status `ready` deltaP `33.3333` edge `1.642` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3707` n `32` status `ready` deltaP `33.3333` edge `1.642` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.8272` n `32` status `ready` deltaP `31.0764` edge `1.6269` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.8272` n `32` status `ready` deltaP `31.0764` edge `1.6269` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.7661` n `32` status `ready` deltaP `32.9861` edge `0.7606` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.7661` n `32` status `ready` deltaP `32.9861` edge `0.7606` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.1897` n `32` status `ready` deltaP `17.5305` edge `0.8445` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.1897` n `32` status `ready` deltaP `17.5305` edge `0.8445` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.2303` n `160` status `ready` deltaP `16.4583` edge `0.6016` maxDD `-15.0371`
- `market_context_high->index_24h` score `4.7227` n `160` status `ready` deltaP `23.6111` edge `0.3501` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.2286` n `160` status `ready` deltaP `19.0278` edge `0.2663` maxDD `-9.5947`
- `risk_on_high->metal_24h` score `2.1042` n `32` status `ready` deltaP `18.4028` edge `0.0788` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.1042` n `32` status `ready` deltaP `18.4028` edge `0.0788` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.8803` n `32` status `ready` deltaP `-0.8384` edge `0.3467` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.8803` n `32` status `ready` deltaP `-0.8384` edge `0.3467` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.5665` n `32` status `ready` deltaP `8.3079` edge `0.2589` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5665` n `32` status `ready` deltaP `8.3079` edge `0.2589` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.0375` n `32` status `ready` deltaP `2.0771` edge `0.2261` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
