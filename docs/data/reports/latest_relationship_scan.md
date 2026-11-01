# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T12:07:23.125359+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6597`

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

- `market_context_high->unknown_24h` score `7031.7573` n `55` status `ready` deltaP `1.7361` edge `585.9682` maxDD `0.0`
- `market_context_high->unknown_4h` score `376.1713` n `55` status `ready` deltaP `5.194` edge `31.3173` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `64.1908` n `55` status `ready` deltaP `3.1628` edge `5.3392` maxDD `-0.2178`
- `news_risk_high->unknown_1h` score `42.8888` n `128` status `ready` deltaP `-6.2406` edge `3.6443` maxDD `-0.9571`
- `market_context_high->equity_24h` score `21.2457` n `55` status `ready` deltaP `43.8415` edge `1.5018` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.8276` n `98` status `ready` deltaP `29.6379` edge `1.007` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.9417` n `55` status `ready` deltaP `56.7708` edge `0.2` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.5145` n `55` status `ready` deltaP `45.7892` edge `0.2687` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.8375` n `55` status `ready` deltaP `23.2927` edge `0.3606` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4011` n `55` status `ready` deltaP `29.673` edge `0.2859` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.5452` n `116` status `ready` deltaP `17.4306` edge `0.4012` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3587` n `55` status `ready` deltaP `31.5244` edge `0.0948` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3354` n `55` status `ready` deltaP `5.4379` edge `0.3119` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4346` n `55` status `ready` deltaP `10.8586` edge `0.3074` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7625` n `55` status `ready` deltaP `-5.1673` edge `0.4122` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5606` n `55` status `ready` deltaP `18.3508` edge `0.0502` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.435` n `55` status `ready` deltaP `2.1285` edge `0.1579` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3712` n `55` status `ready` deltaP `8.0321` edge `0.1217` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3451` n `55` status `ready` deltaP `3.9249` edge `0.153` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8732` n `55` status `ready` deltaP `10.8764` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
