# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T00:22:26.527088+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9338`

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

- `risk_on_high->crypto_alt_4h` score `5.0841` n `48` status `ready` deltaP `20.7826` edge `0.3299` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0841` n `48` status `ready` deltaP `20.7826` edge `0.3299` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `4.3823` n `100` status `ready` deltaP `15.8659` edge `0.4043` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `4.3102` n `31` status `ready` deltaP `30.087` edge `0.1586` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.3102` n `31` status `ready` deltaP `30.087` edge `0.1586` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.1211` n `48` status `ready` deltaP `35.4167` edge `0.3775` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.1211` n `48` status `ready` deltaP `35.4167` edge `0.3775` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.9496` n `100` status `ready` deltaP `19.25` edge `0.3567` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.7212` n `101` status `ready` deltaP `12.9172` edge `0.1524` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.8596` n `49` status `ready` deltaP `6.6938` edge `0.0867` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8596` n `49` status `ready` deltaP `6.6938` edge `0.0867` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.7758` n `101` status `ready` deltaP `5.3195` edge `0.1055` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.3462` n `49` status `ready` deltaP `5.9055` edge `0.0703` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3462` n `49` status `ready` deltaP `5.9055` edge `0.0703` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `0.1599` n `100` status `ready` deltaP `-4.5366` edge `0.1082` maxDD `-1.8373`
- `market_context_high->index_1h` score `0.0125` n `101` status `ready` deltaP `4.9668` edge `0.0032` maxDD `-0.4438`
- `market_context_high->metal_1h` score `-0.2059` n `101` status `ready` deltaP `5.5374` edge `0.0033` maxDD `-0.5899`
- `market_context_high->metal_4h` score `-0.342` n `100` status `ready` deltaP `8.6098` edge `0.0094` maxDD `-1.624`
- `market_context_high->fx_1h` score `-0.3692` n `101` status `ready` deltaP `-1.2176` edge `-0.0012` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.495` n `49` status `ready` deltaP `2.163` edge `0.0017` maxDD `-0.5899`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
