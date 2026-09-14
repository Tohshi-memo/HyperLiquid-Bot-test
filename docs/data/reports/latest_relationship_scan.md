# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T11:52:26.855854+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_4h` score `739.7853` n `82` status `ready` deltaP `-20.5793` edge `61.8753` maxDD `-4.1464`
- `news_risk_high->unknown_1h` score `442.749` n `82` status `ready` deltaP `-6.5978` edge `36.9819` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.4209` n `82` status `ready` deltaP `41.781` edge `1.472` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `16.8691` n `82` status `ready` deltaP `33.4223` edge `1.33` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.1986` n `82` status `ready` deltaP `35.4844` edge `0.958` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2656` n `82` status `ready` deltaP `59.3199` edge `0.311` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `7.1431` n `94` status `ready` deltaP `40.1042` edge `0.3279` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1963` n `41` status `ready` deltaP `40.1042` edge `0.249` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1963` n `41` status `ready` deltaP `40.1042` edge `0.249` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.0029` n `82` status `ready` deltaP `36.2043` edge `0.3043` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.001` n `41` status `ready` deltaP `56.0679` edge `0.0472` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.001` n `41` status `ready` deltaP `56.0679` edge `0.0472` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.5386` n `94` status `ready` deltaP `52.1239` edge `0.0523` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0007` n `52` status `ready` deltaP `26.5947` edge `0.0244` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0007` n `52` status `ready` deltaP `26.5947` edge `0.0244` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.801` n `137` status `ready` deltaP `22.0046` edge `0.0452` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7634` n `137` status `ready` deltaP `12.812` edge `0.0159` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.678` n `82` status `ready` deltaP `16.4634` edge `0.04` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3428` n `137` status `ready` deltaP `12.293` edge `0.0096` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.248` n `52` status `ready` deltaP `7.1972` edge `0.0079` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
