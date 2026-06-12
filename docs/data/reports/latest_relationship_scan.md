# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T12:37:28.235377+00:00`
- Price records: `672`
- Market context records: `3686`
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

- `risk_on_high->crypto_major_24h` score `32.1055` n `32` status `ready` deltaP `35.7639` edge `2.4413` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.1055` n `32` status `ready` deltaP `35.7639` edge `2.4413` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.6125` n `32` status `ready` deltaP `38.0208` edge `1.8809` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.6125` n `32` status `ready` deltaP `38.0208` edge `1.8809` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.8392` n `32` status `ready` deltaP `34.8958` edge `1.7691` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.8392` n `32` status `ready` deltaP `34.8958` edge `1.7691` maxDD `-0.8779`
- `risk_on_high->index_24h` score `14.0474` n `32` status `ready` deltaP `37.8472` edge `0.9183` maxDD `0.0`
- `risk_on_and_context->index_24h` score `14.0474` n `32` status `ready` deltaP `37.8472` edge `0.9183` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.7411` n `32` status `ready` deltaP `18.9024` edge `0.8813` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.7411` n `32` status `ready` deltaP `18.9024` edge `0.8813` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `4.8386` n `32` status `ready` deltaP `23.4375` edge `0.2731` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `4.8386` n `32` status `ready` deltaP `23.4375` edge `0.2731` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.6513` n `157` status `ready` deltaP `23.1975` edge `0.3212` maxDD `-11.3924`
- `risk_on_high->equity_4h` score `2.0974` n `32` status `ready` deltaP `8.9177` edge `0.3229` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.0974` n `32` status `ready` deltaP `8.9177` edge `0.3229` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.8873` n `32` status `ready` deltaP `-0.9909` edge `0.3483` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.8873` n `32` status `ready` deltaP `-0.9909` edge `0.3483` maxDD `-11.7537`
- `market_context_high->equity_24h` score `1.3245` n `157` status `ready` deltaP `15.0909` edge `0.5762` maxDD `-35.3144`
- `risk_on_high->crypto_major_1h` score `1.2106` n `32` status `ready` deltaP `2.5262` edge `0.2453` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2106` n `32` status `ready` deltaP `2.5262` edge `0.2453` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
