# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T20:07:29.952958+00:00`
- Price records: `672`
- Market context records: `3719`
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

- `risk_on_high->crypto_major_24h` score `29.6084` n `32` status `ready` deltaP `31.25` edge `2.2633` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.6084` n `32` status `ready` deltaP `31.25` edge `2.2633` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.3515` n `32` status `ready` deltaP `33.3333` edge `1.6404` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3515` n `32` status `ready` deltaP `33.3333` edge `1.6404` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.8056` n `32` status `ready` deltaP `31.0764` edge `1.6251` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.8056` n `32` status `ready` deltaP `31.0764` edge `1.6251` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.7378` n `32` status `ready` deltaP `32.8125` edge `0.7594` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.7378` n `32` status `ready` deltaP `32.8125` edge `0.7594` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.1945` n `32` status `ready` deltaP `17.5305` edge `0.8449` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.1945` n `32` status `ready` deltaP `17.5305` edge `0.8449` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.69` n `159` status `ready` deltaP `16.9811` edge `0.6161` maxDD `-13.7449`
- `market_context_high->index_24h` score `4.806` n `159` status `ready` deltaP `24.0075` edge `0.3544` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.414` n `159` status `ready` deltaP `19.2905` edge `0.2699` maxDD `-9.1203`
- `risk_on_high->metal_24h` score `2.0711` n `32` status `ready` deltaP `18.2292` edge `0.0772` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.0711` n `32` status `ready` deltaP `18.2292` edge `0.0772` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.9033` n `32` status `ready` deltaP `-0.686` edge `0.3476` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.9033` n `32` status `ready` deltaP `-0.686` edge `0.3476` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.5446` n `32` status `ready` deltaP `8.1555` edge `0.2571` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5446` n `32` status `ready` deltaP `8.1555` edge `0.2571` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.0632` n `32` status `ready` deltaP `2.2268` edge `0.2284` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
