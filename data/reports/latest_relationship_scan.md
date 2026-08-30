# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T19:37:30.940203+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11722`

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

- `risk_on_high->crypto_alt_24h` score `26.0884` n `38` status `ready` deltaP `51.2153` edge `1.8326` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `26.0884` n `38` status `ready` deltaP `51.2153` edge `1.8326` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.4163` n `38` status `ready` deltaP `45.1389` edge `1.0671` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.4163` n `38` status `ready` deltaP `45.1389` edge `1.0671` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.453` n `68` status `ready` deltaP `27.8246` edge `0.6451` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.453` n `68` status `ready` deltaP `27.8246` edge `0.6451` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `6.531` n `38` status `ready` deltaP `39.7569` edge `0.2792` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.531` n `38` status `ready` deltaP `39.7569` edge `0.2792` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.3673` n `38` status `ready` deltaP `71.7014` edge `0.0526` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3673` n `38` status `ready` deltaP `71.7014` edge `0.0526` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2379` n `38` status `ready` deltaP `53.2986` edge `0.1645` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2379` n `38` status `ready` deltaP `53.2986` edge `0.1645` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.4005` n `149` status `ready` deltaP `21.054` edge `0.3567` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `5.3982` n `68` status `ready` deltaP `27.4301` edge `0.2953` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.3982` n `68` status `ready` deltaP `27.4301` edge `0.2953` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.5761` n `117` status `ready` deltaP `37.0593` edge `0.2362` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `4.4595` n `68` status `ready` deltaP `17.3422` edge `0.3043` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `4.4595` n `68` status `ready` deltaP `17.3422` edge `0.3043` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `3.6993` n `68` status `ready` deltaP `33.8146` edge `0.1015` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.6993` n `68` status `ready` deltaP `33.8146` edge `0.1015` maxDD `-0.1594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
