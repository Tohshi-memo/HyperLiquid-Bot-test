# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T00:52:19.985562+00:00`
- Price records: `672`
- Market context records: `3233`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.55` n `103` status `ready` deltaP `19.8658` edge `2.7171` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.8598` n `103` status `ready` deltaP `50.2512` edge `0.8628` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.8508` n `103` status `ready` deltaP `33.0518` edge `0.856` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.8623` n `103` status `ready` deltaP `20.6109` edge `1.584` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `3.0807` n `103` status `ready` deltaP `23.9364` edge `2.3053` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.586` n `31` status `ready` deltaP `10.677` edge `0.3673` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.586` n `31` status `ready` deltaP `10.677` edge `0.3673` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.2269` n `131` status `ready` deltaP `17.9412` edge `0.1457` maxDD `-3.0454`
- `risk_on_high->crypto_alt_1h` score `0.6677` n `31` status `ready` deltaP `3.7087` edge `0.2046` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.6677` n `31` status `ready` deltaP `3.7087` edge `0.2046` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4273` n `31` status `ready` deltaP `7.7651` edge `0.0715` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4273` n `31` status `ready` deltaP `7.7651` edge `0.0715` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3017` n `31` status `ready` deltaP `2.2117` edge `0.1143` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3017` n `31` status `ready` deltaP `2.2117` edge `0.1143` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1359` n `31` status `ready` deltaP `0.0338` edge `0.0447` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1359` n `31` status `ready` deltaP `0.0338` edge `0.0447` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.3755` n `143` status `ready` deltaP `3.596` edge `0.0188` maxDD `-2.2583`
- `market_context_high->index_1h` score `-0.4811` n `143` status `ready` deltaP `4.0943` edge `0.0173` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.6873` n `131` status `ready` deltaP `9.855` edge `0.1036` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.6998` n `143` status `ready` deltaP `4.09` edge `0.1093` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
