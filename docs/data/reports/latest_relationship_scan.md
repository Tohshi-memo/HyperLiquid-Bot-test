# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T09:22:26.754270+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6505`

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

- `market_context_high->unknown_24h` score `7032.6157` n `55` status `ready` deltaP `3.6458` edge `586.027` maxDD `0.0`
- `market_context_high->unknown_4h` score `373.7427` n `55` status `ready` deltaP `5.3464` edge `31.1139` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `61.8316` n `117` status `ready` deltaP `-6.5906` edge `5.2252` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `58.3216` n `55` status `ready` deltaP `3.0131` edge `4.8511` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.4695` n `55` status `ready` deltaP `44.8832` edge `1.5135` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.8612` n `98` status `ready` deltaP `29.6379` edge `1.0098` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.1472` n `55` status `ready` deltaP `58.6806` edge `0.2044` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.6335` n `55` status `ready` deltaP `46.1364` edge `0.2763` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.6637` n `55` status `ready` deltaP `22.5305` edge `0.3512` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3603` n `55` status `ready` deltaP `29.673` edge `0.2825` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.7488` n `108` status `ready` deltaP `17.5305` edge `0.4175` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3707` n `55` status `ready` deltaP `31.5244` edge `0.0958` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.303` n `55` status `ready` deltaP `5.4379` edge `0.3092` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4564` n `55` status `ready` deltaP `10.8586` edge `0.3102` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7844` n `55` status `ready` deltaP `-5.1673` edge `0.415` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5522` n `55` status `ready` deltaP `18.3508` edge `0.0495` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.3727` n `55` status `ready` deltaP `1.5297` edge `0.1567` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.2897` n `55` status `ready` deltaP `7.4333` edge `0.1189` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.2708` n `55` status `ready` deltaP `3.4758` edge `0.1498` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.848` n `55` status `ready` deltaP `10.577` edge `0.025` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
