# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T12:37:26.394408+00:00`
- Price records: `672`
- Market context records: `3383`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `55.7222` n `32` status `ready` deltaP `58.3333` edge `4.2589` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.7222` n `32` status `ready` deltaP `58.3333` edge `4.2589` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.5817` n `32` status `ready` deltaP `54.6875` edge `4.1157` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.5817` n `32` status `ready` deltaP `54.6875` edge `4.1157` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.5589` n `32` status `ready` deltaP `56.7708` edge `3.4181` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.5589` n `32` status `ready` deltaP `56.7708` edge `3.4181` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1278` n `32` status `ready` deltaP `50.8681` edge `1.5882` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1278` n `32` status `ready` deltaP `50.8681` edge `1.5882` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.9692` n `155` status `ready` deltaP `19.1028` edge `2.5019` maxDD `-56.8787`
- `risk_on_high->crypto_major_4h` score `15.2578` n `32` status `ready` deltaP `28.2012` edge `1.1957` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.2578` n `32` status `ready` deltaP `28.2012` edge `1.1957` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `14.9895` n `155` status `ready` deltaP `24.0389` edge `2.28` maxDD `-88.2905`
- `risk_on_high->metal_24h` score `14.1307` n `32` status `ready` deltaP `30.2083` edge `1.0023` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.1307` n `32` status `ready` deltaP `30.2083` edge `1.0023` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.8013` n `155` status `ready` deltaP `35.3842` edge `1.003` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.9973` n `155` status `ready` deltaP `30.3192` edge `2.0494` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.1328` n `32` status `ready` deltaP `8.6128` edge `0.7214` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.1328` n `32` status `ready` deltaP `8.6128` edge `0.7214` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5629` n `32` status `ready` deltaP `14.4055` edge `0.4742` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5629` n `32` status `ready` deltaP `14.4055` edge `0.4742` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
