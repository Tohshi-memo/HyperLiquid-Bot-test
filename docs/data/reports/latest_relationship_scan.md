# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T10:22:29.930209+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6537`

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

- `market_context_high->unknown_24h` score `7032.3477` n `55` status `ready` deltaP `2.9514` edge `586.0093` maxDD `0.0`
- `market_context_high->unknown_4h` score `372.2115` n `55` status `ready` deltaP `5.3464` edge `30.9863` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `59.0512` n `55` status `ready` deltaP `3.1628` edge `4.9109` maxDD `-0.2178`
- `news_risk_high->unknown_1h` score `52.2953` n `121` status `ready` deltaP `-6.5893` edge `4.4305` maxDD `-0.9571`
- `market_context_high->equity_24h` score `21.4359` n `55` status `ready` deltaP `44.8832` edge `1.5107` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.854` n `98` status `ready` deltaP `29.6379` edge `1.0092` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.0749` n `55` status `ready` deltaP `57.9861` edge `0.203` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.5685` n `55` status `ready` deltaP `45.7892` edge `0.2732` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.7193` n `55` status `ready` deltaP `22.8354` edge `0.3538` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3759` n `55` status `ready` deltaP `29.673` edge `0.2838` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.7903` n `109` status `ready` deltaP `18.0648` edge `0.4174` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3671` n `55` status `ready` deltaP `31.5244` edge `0.0955` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.315` n `55` status `ready` deltaP `5.4379` edge `0.3102` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4494` n `55` status `ready` deltaP `10.8586` edge `0.3093` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7797` n `55` status `ready` deltaP `-5.1673` edge `0.4144` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5558` n `55` status `ready` deltaP `18.3508` edge `0.0498` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.3871` n `55` status `ready` deltaP `1.6794` edge `0.1569` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3101` n `55` status `ready` deltaP `7.583` edge `0.1196` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.2816` n `55` status `ready` deltaP `3.6255` edge `0.1497` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8852` n `55` status `ready` deltaP `11.0261` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
