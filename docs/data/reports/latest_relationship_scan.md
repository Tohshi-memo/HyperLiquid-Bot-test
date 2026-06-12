# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T16:52:28.980700+00:00`
- Price records: `672`
- Market context records: `3704`
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

- `risk_on_high->crypto_major_24h` score `30.2902` n `32` status `ready` deltaP `32.8125` edge `2.3097` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.2902` n `32` status `ready` deltaP `32.8125` edge `2.3097` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.1504` n `32` status `ready` deltaP `35.0694` edge `1.6954` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.1504` n `32` status `ready` deltaP `35.0694` edge `1.6954` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.2603` n `32` status `ready` deltaP `31.9444` edge `1.6572` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.2603` n `32` status `ready` deltaP `31.9444` edge `1.6572` maxDD `-0.8779`
- `risk_on_high->index_24h` score `12.3833` n `32` status `ready` deltaP `34.8958` edge `0.7993` maxDD `0.0`
- `risk_on_and_context->index_24h` score `12.3833` n `32` status `ready` deltaP `34.8958` edge `0.7993` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.8939` n `32` status `ready` deltaP `17.0732` edge `0.8229` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.8939` n `32` status `ready` deltaP `17.0732` edge `0.8229` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.1493` n `161` status `ready` deltaP `22.4734` edge `0.3099` maxDD `-7.1159`
- `risk_on_high->metal_24h` score `2.8565` n `32` status `ready` deltaP `20.4861` edge `0.1276` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.8565` n `32` status `ready` deltaP `20.4861` edge `0.1276` maxDD `-0.7574`
- `market_context_high->equity_24h` score `2.6985` n `161` status `ready` deltaP `14.5725` edge `0.5349` maxDD `-23.5737`
- `risk_on_high->equity_4h` score `1.6543` n `32` status `ready` deltaP `8.7652` edge `0.2671` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.6543` n `32` status `ready` deltaP `8.7652` edge `0.2671` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.3977` n `32` status `ready` deltaP `-1.9055` edge `0.3136` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3977` n `32` status `ready` deltaP `-1.9055` edge `0.3136` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.0835` n `32` status `ready` deltaP `2.2268` edge `0.231` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.0835` n `32` status `ready` deltaP `2.2268` edge `0.231` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
