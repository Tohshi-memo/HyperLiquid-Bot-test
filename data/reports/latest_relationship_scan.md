# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T17:07:28.566332+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11590`

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

- `risk_on_high->crypto_alt_24h` score `26.1395` n `30` status `ready` deltaP `52.6042` edge `1.8276` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `26.1395` n `30` status `ready` deltaP `52.6042` edge `1.8276` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.7331` n `30` status `ready` deltaP `46.3542` edge `1.0854` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.7331` n `30` status `ready` deltaP `46.3542` edge `1.0854` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9647` n `59` status `ready` deltaP `25.5813` edge `0.7027` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.9647` n `59` status `ready` deltaP `25.5813` edge `0.7027` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `7.0898` n `30` status `ready` deltaP `41.4931` edge `0.3142` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.0898` n `30` status `ready` deltaP `41.4931` edge `0.3142` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.511` n `30` status `ready` deltaP `73.4375` edge `0.053` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.511` n `30` status `ready` deltaP `73.4375` edge `0.053` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.2925` n `148` status `ready` deltaP `20.9089` edge `0.432` maxDD `-1.0945`
- `risk_on_high->metal_24h` score `6.2338` n `30` status `ready` deltaP `53.4722` edge `0.163` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2338` n `30` status `ready` deltaP `53.4722` edge `0.163` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.0774` n `59` status `ready` deltaP `24.2895` edge `0.2895` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.0774` n `59` status `ready` deltaP `24.2895` edge `0.2895` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.4978` n `116` status `ready` deltaP `36.2308` edge `0.2352` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `4.0864` n `70` status `ready` deltaP `11.2361` edge `0.2859` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.0864` n `70` status `ready` deltaP `11.2361` edge `0.2859` maxDD `-0.2885`
- `risk_on_high->crypto_alt_4h` score `3.7503` n `59` status `ready` deltaP `12.407` edge `0.2781` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `3.7503` n `59` status `ready` deltaP `12.407` edge `0.2781` maxDD `-1.5298`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
