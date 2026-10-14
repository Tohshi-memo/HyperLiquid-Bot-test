# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T04:22:30.887081+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9843`

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

- `market_context_high->crypto_alt_4h` score `6.4598` n `117` status `ready` deltaP `16.1547` edge `0.5755` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.4144` n `54` status `ready` deltaP `32.0` edge `0.3212` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.4144` n `54` status `ready` deltaP `32.0` edge `0.3212` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.9984` n `117` status `ready` deltaP `20.8151` edge `0.517` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.0486` n `54` status `ready` deltaP `18.4339` edge `0.3426` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0486` n `54` status `ready` deltaP `18.4339` edge `0.3426` maxDD `-1.9151`
- `market_context_high->unknown_4h` score `4.5162` n `117` status `ready` deltaP `-3.467` edge `0.4641` maxDD `-1.8373`
- `risk_on_high->crypto_major_4h` score `4.4387` n `54` status `ready` deltaP `33.9205` edge `0.4282` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4387` n `54` status `ready` deltaP `33.9205` edge `0.4282` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6739` n `117` status `ready` deltaP `13.5665` edge `0.1558` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2465` n `117` status `ready` deltaP `6.7097` edge `0.1397` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2122` n `117` status `ready` deltaP `13.3078` edge `0.0335` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.3179` n `117` status `ready` deltaP `1.3976` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3462` n `54` status `ready` deltaP `2.1513` edge `0.0135` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3462` n `54` status `ready` deltaP `2.1513` edge `0.0135` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3877` n `117` status `ready` deltaP `7.265` edge `0.0062` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4664` n `54` status `ready` deltaP `1.8519` edge `0.001` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4664` n `54` status `ready` deltaP `1.8519` edge `0.001` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.6125` n `117` status `ready` deltaP `-0.1271` edge `-0.0029` maxDD `-1.3154`
- `risk_on_high->metal_4h` score `-0.643` n `54` status `ready` deltaP `0.9146` edge `0.016` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
