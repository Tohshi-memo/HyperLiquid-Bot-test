# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T15:07:34.843569+00:00`
- Price records: `672`
- Market context records: `3697`
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

- `risk_on_high->crypto_major_24h` score `30.9586` n `32` status `ready` deltaP `34.0278` edge `2.3573` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.9586` n `32` status `ready` deltaP `34.0278` edge `2.3573` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.9916` n `32` status `ready` deltaP `36.2847` edge `1.7574` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.9916` n `32` status `ready` deltaP `36.2847` edge `1.7574` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.7859` n `32` status `ready` deltaP `33.1597` edge `1.6929` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.7859` n `32` status `ready` deltaP `33.1597` edge `1.6929` maxDD `-0.8779`
- `risk_on_high->index_24h` score `13.0049` n `32` status `ready` deltaP `36.1111` edge `0.843` maxDD `0.0`
- `risk_on_and_context->index_24h` score `13.0049` n `32` status `ready` deltaP `36.1111` edge `0.843` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.1987` n `32` status `ready` deltaP `17.9878` edge `0.8422` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.1987` n `32` status `ready` deltaP `17.9878` edge `0.8422` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.0322` n `157` status `ready` deltaP `22.7353` edge `0.2984` maxDD `-7.1159`
- `risk_on_high->metal_24h` score `3.5741` n `32` status `ready` deltaP `21.7014` edge `0.1793` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `3.5741` n `32` status `ready` deltaP `21.7014` edge `0.1793` maxDD `-0.7574`
- `market_context_high->equity_24h` score `2.116` n `157` status `ready` deltaP `14.6286` edge `0.5377` maxDD `-27.3777`
- `risk_on_high->equity_4h` score `1.7847` n `32` status `ready` deltaP `8.9177` edge `0.2828` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.7847` n `32` status `ready` deltaP `8.9177` edge `0.2828` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.5395` n `32` status `ready` deltaP `-1.753` edge `0.3244` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.5395` n `32` status `ready` deltaP `-1.753` edge `0.3244` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.025` n `32` status `ready` deltaP `1.7777` edge `0.2265` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.025` n `32` status `ready` deltaP `1.7777` edge `0.2265` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
