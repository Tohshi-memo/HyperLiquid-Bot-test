# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T13:22:33.265636+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `30.0272` n `41` status `ready` deltaP `38.6898` edge `2.2784` maxDD `-1.7253`
- `market_context_high->crypto_major_24h` score `28.1922` n `41` status `ready` deltaP `50.3218` edge `2.0437` maxDD `-1.3864`
- `risk_on_high->crypto_alt_4h` score `3.9564` n `48` status `ready` deltaP `18.1911` edge `0.2532` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.9564` n `48` status `ready` deltaP `18.1911` edge `0.2532` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.556` n `48` status `ready` deltaP `33.1301` edge `0.3203` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.556` n `48` status `ready` deltaP `33.1301` edge `0.3203` maxDD `-4.1548`
- `market_context_high->metal_24h` score `3.4605` n `41` status `ready` deltaP `29.8188` edge `0.1013` maxDD `-0.2709`
- `market_context_high->crypto_alt_4h` score `2.6475` n `102` status `ready` deltaP `11.9411` edge `0.3063` maxDD `-10.8892`
- `market_context_high->crypto_major_4h` score `2.5555` n `102` status `ready` deltaP `15.7281` edge `0.2859` maxDD `-8.5569`
- `market_context_high->crypto_alt_1h` score `1.6006` n `102` status `ready` deltaP `12.6101` edge `0.1444` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9215` n `48` status `ready` deltaP `6.2375` edge `0.0949` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9215` n `48` status `ready` deltaP `6.2375` edge `0.0949` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.6213` n `102` status `ready` deltaP `4.1388` edge `0.1005` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4062` n `48` status `ready` deltaP `5.3643` edge `0.0816` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4062` n `48` status `ready` deltaP `5.3643` edge `0.0816` maxDD `-3.2233`
- `market_context_high->index_24h` score `0.2131` n `41` status `ready` deltaP `9.7264` edge `0.0554` maxDD `-1.4333`
- `market_context_high->index_1h` score `-0.0131` n `102` status `ready` deltaP `4.3032` edge `0.0027` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.0455` n `102` status `ready` deltaP `7.0946` edge `0.005` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.2992` n `48` status `ready` deltaP `3.4182` edge `0.0042` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.2992` n `48` status `ready` deltaP `3.4182` edge `0.0042` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
