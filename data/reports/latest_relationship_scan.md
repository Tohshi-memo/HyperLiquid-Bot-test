# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T21:22:21.933476+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `risk_on_high->crypto_alt_24h` score `24.9064` n `45` status `ready` deltaP `50.0` edge `1.7422` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `24.9064` n `45` status `ready` deltaP `50.0` edge `1.7422` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `14.2971` n `45` status `ready` deltaP `39.8264` edge `0.9398` maxDD `-0.4441`
- `risk_on_and_context->crypto_major_24h` score `14.2971` n `45` status `ready` deltaP `39.8264` edge `0.9398` maxDD `-0.4441`
- `risk_on_high->unknown_4h` score `8.9136` n `75` status `ready` deltaP `29.1972` edge `0.591` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.9136` n `75` status `ready` deltaP `29.1972` edge `0.591` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.2701` n `45` status `ready` deltaP `70.4861` edge `0.0526` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2701` n `45` status `ready` deltaP `70.4861` edge `0.0526` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.1455` n `45` status `ready` deltaP `53.2986` edge `0.1568` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.1455` n `45` status `ready` deltaP `53.2986` edge `0.1568` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.1815` n `45` status `ready` deltaP `34.4445` edge `0.2106` maxDD `-0.0086`
- `risk_on_and_context->equity_24h` score `5.1815` n `45` status `ready` deltaP `34.4445` edge `0.2106` maxDD `-0.0086`
- `market_context_high->unknown_4h` score `5.0501` n `149` status `ready` deltaP `21.054` edge `0.3275` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5569` n `117` status `ready` deltaP `37.0593` edge `0.2346` maxDD `-3.1535`
- `market_context_high->crypto_major_24h` score `3.6762` n `117` status `ready` deltaP `16.0657` edge `0.4775` maxDD `-17.2607`
- `risk_on_high->crypto_major_4h` score `3.5212` n `75` status `ready` deltaP `23.4472` edge `0.2181` maxDD `-4.8121`
- `risk_on_and_context->crypto_major_4h` score `3.5212` n `75` status `ready` deltaP `23.4472` edge `0.2181` maxDD `-4.8121`
- `risk_on_high->crypto_alt_4h` score `3.4224` n `75` status `ready` deltaP `15.1809` edge `0.2527` maxDD `-3.1634`
- `risk_on_and_context->crypto_alt_4h` score `3.4224` n `75` status `ready` deltaP `15.1809` edge `0.2527` maxDD `-3.1634`
- `risk_on_high->unknown_1h` score `3.1243` n `87` status `ready` deltaP `10.2296` edge `0.2166` maxDD `-0.2885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
