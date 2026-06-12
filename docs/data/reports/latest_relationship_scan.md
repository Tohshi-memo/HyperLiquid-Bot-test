# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T17:13:32.964161+00:00`
- Price records: `672`
- Market context records: `3706`
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

- `risk_on_high->crypto_major_24h` score `30.1707` n `32` status `ready` deltaP `32.6389` edge `2.3009` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.1707` n `32` status `ready` deltaP `32.6389` edge `2.3009` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.0393` n `32` status `ready` deltaP `34.8958` edge `1.6873` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.0393` n `32` status `ready` deltaP `34.8958` edge `1.6873` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.1588` n `32` status `ready` deltaP `31.7708` edge `1.6499` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.1588` n `32` status `ready` deltaP `31.7708` edge `1.6499` maxDD `-0.8779`
- `risk_on_high->index_24h` score `12.301` n `32` status `ready` deltaP `34.7222` edge `0.7936` maxDD `0.0`
- `risk_on_and_context->index_24h` score `12.301` n `32` status `ready` deltaP `34.7222` edge `0.7936` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.8649` n `32` status `ready` deltaP `16.9207` edge `0.8215` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.8649` n `32` status `ready` deltaP `16.9207` edge `0.8215` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.3591` n `161` status `ready` deltaP `22.921` edge `0.3244` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.3354` n `161` status `ready` deltaP `15.02` edge `0.556` maxDD `-21.5879`
- `risk_on_high->metal_24h` score `2.7526` n `32` status `ready` deltaP `20.3125` edge `0.1201` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.7526` n `32` status `ready` deltaP `20.3125` edge `0.1201` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.6284` n `32` status `ready` deltaP `8.6128` edge `0.2648` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.6284` n `32` status `ready` deltaP `8.6128` edge `0.2648` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.3977` n `32` status `ready` deltaP `-1.9055` edge `0.3136` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3977` n `32` status `ready` deltaP `-1.9055` edge `0.3136` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.0577` n `32` status `ready` deltaP `2.0771` edge `0.2287` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.0577` n `32` status `ready` deltaP `2.0771` edge `0.2287` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
