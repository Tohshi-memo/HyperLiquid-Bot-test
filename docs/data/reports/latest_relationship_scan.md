# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T16:37:32.034689+00:00`
- Price records: `672`
- Market context records: `3703`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `30.3964` n `32` status `ready` deltaP `32.9861` edge `2.3174` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.3964` n `32` status `ready` deltaP `32.9861` edge `2.3174` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.2674` n `32` status `ready` deltaP `35.2431` edge `1.704` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.2674` n `32` status `ready` deltaP `35.2431` edge `1.704` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.345` n `32` status `ready` deltaP `32.1181` edge `1.6631` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.345` n `32` status `ready` deltaP `32.1181` edge `1.6631` maxDD `-0.8779`
- `risk_on_high->index_24h` score `12.4644` n `32` status `ready` deltaP `35.0694` edge `0.8049` maxDD `0.0`
- `risk_on_and_context->index_24h` score `12.4644` n `32` status `ready` deltaP `35.0694` edge `0.8049` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.8951` n `32` status `ready` deltaP `17.0732` edge `0.823` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.8951` n `32` status `ready` deltaP `17.0732` edge `0.823` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.1114` n `160` status `ready` deltaP `22.5694` edge `0.3061` maxDD `-7.1159`
- `risk_on_high->metal_24h` score `2.9616` n `32` status `ready` deltaP `20.6597` edge `0.1352` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.9616` n `32` status `ready` deltaP `20.6597` edge `0.1352` maxDD `-0.7574`
- `market_context_high->equity_24h` score `2.6794` n `160` status `ready` deltaP `14.6181` edge `0.533` maxDD `-23.5737`
- `risk_on_high->equity_4h` score `1.6801` n `32` status `ready` deltaP `8.9177` edge `0.2694` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.6801` n `32` status `ready` deltaP `8.9177` edge `0.2694` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.3687` n `32` status `ready` deltaP `-2.0579` edge `0.3122` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3687` n `32` status `ready` deltaP `-2.0579` edge `0.3122` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.0835` n `32` status `ready` deltaP `2.2268` edge `0.231` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.0835` n `32` status `ready` deltaP `2.2268` edge `0.231` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
