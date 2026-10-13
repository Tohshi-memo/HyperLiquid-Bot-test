# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T10:07:26.698656+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9798`

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

- `market_context_high->crypto_alt_4h` score `7.8016` n `117` status `ready` deltaP `20.1181` edge `0.6609` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.9433` n `117` status `ready` deltaP `24.0163` edge `0.5744` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.3905` n `54` status `ready` deltaP `22.3973` edge `0.428` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.3905` n `54` status `ready` deltaP `22.3973` edge `0.428` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.5531` n `48` status `ready` deltaP `30.6087` edge `0.2587` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5531` n `48` status `ready` deltaP `30.6087` edge `0.2587` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.0529` n `54` status `ready` deltaP `37.1217` edge `0.4856` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.0529` n `54` status `ready` deltaP `37.1217` edge `0.4856` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.6526` n `117` status `ready` deltaP `-3.467` edge `0.3088` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.029` n `117` status `ready` deltaP `14.4647` edge `0.1794` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5403` n `117` status `ready` deltaP `7.7576` edge `0.1572` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0814` n `117` status `ready` deltaP `12.3932` edge `0.0287` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1552` n `54` status `ready` deltaP `3.1992` edge `0.031` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1552` n `54` status `ready` deltaP `3.1992` edge `0.031` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2675` n `117` status `ready` deltaP `1.9982` edge `0.0024` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.4144` n `54` status `ready` deltaP `4.2083` edge `0.0214` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4144` n `54` status `ready` deltaP `4.2083` edge `0.0214` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4979` n `117` status `ready` deltaP `6.0674` edge `0.005` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.538` n `54` status `ready` deltaP `0.6543` edge `-0.0002` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.538` n `54` status `ready` deltaP `0.6543` edge `-0.0002` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
