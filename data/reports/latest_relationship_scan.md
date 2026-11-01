# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T22:22:44.593507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6927`

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

- `market_context_high->unknown_24h` score `7498.7359` n `55` status `ready` deltaP `1.3889` edge `624.8854` maxDD `0.0`
- `market_context_high->unknown_4h` score `341.489` n `55` status `ready` deltaP `7.1757` edge `28.4139` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `43.3142` n `55` status `ready` deltaP `4.3604` edge `3.5915` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.2476` n `55` status `ready` deltaP `42.7999` edge `1.5089` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2882` n `94` status `ready` deltaP `31.1355` edge `1.0354` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.2747` n `55` status `ready` deltaP `50.1736` edge `0.1884` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2542` n `55` status `ready` deltaP `24.5122` edge `0.3872` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.9247` n `55` status `ready` deltaP `41.1017` edge `0.2508` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.6817` n `55` status `ready` deltaP `31.3498` edge `0.2981` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.4361` n `55` status `ready` deltaP `6.3525` edge `0.3142` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.1214` n `55` status `ready` deltaP `29.8476` edge `0.0862` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.5763` n `126` status `ready` deltaP `10.3852` edge `0.2841` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4209` n `55` status `ready` deltaP `10.685` edge `0.3068` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9477` n `55` status `ready` deltaP `-4.1256` edge `0.429` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7821` n `55` status `ready` deltaP `20.7899` edge `0.0524` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5992` n `55` status `ready` deltaP `3.6255` edge `0.1616` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4539` n `55` status `ready` deltaP `8.3315` edge `0.1266` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.4447` n `55` status `ready` deltaP `3.9249` edge `0.1613` maxDD `-2.3659`
- `market_context_high->metal_1h` score `1.0325` n `55` status `ready` deltaP `12.6728` edge `0.0264` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5724` n `55` status `ready` deltaP `13.7861` edge `-0.0001` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
