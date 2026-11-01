# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T11:37:25.859073+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6569`

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

- `market_context_high->unknown_24h` score `7031.9039` n `55` status `ready` deltaP `2.0833` edge `585.9781` maxDD `0.0`
- `market_context_high->unknown_4h` score `372.2847` n `55` status `ready` deltaP `5.3464` edge `30.9924` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `59.1616` n `55` status `ready` deltaP `3.0131` edge `4.9211` maxDD `-0.2178`
- `news_risk_high->unknown_1h` score `40.6501` n `126` status `ready` deltaP `-5.9191` edge `3.4556` maxDD `-0.9571`
- `market_context_high->equity_24h` score `21.2836` n `55` status `ready` deltaP `44.0151` edge `1.5038` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.8336` n `98` status `ready` deltaP `29.6379` edge `1.0075` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.979` n `55` status `ready` deltaP `57.1181` edge `0.2008` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.5277` n `55` status `ready` deltaP `45.7892` edge `0.2698` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.7771` n `55` status `ready` deltaP `22.9878` edge `0.3576` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3915` n `55` status `ready` deltaP `29.673` edge `0.2851` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.6848` n `114` status `ready` deltaP `18.4264` edge `0.4062` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3611` n `55` status `ready` deltaP `31.5244` edge `0.095` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3294` n `55` status `ready` deltaP `5.4379` edge `0.3114` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4393` n `55` status `ready` deltaP `10.8586` edge `0.308` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7664` n `55` status `ready` deltaP `-5.1673` edge `0.4127` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5606` n `55` status `ready` deltaP `18.3508` edge `0.0502` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4326` n `55` status `ready` deltaP `2.1285` edge `0.1577` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3712` n `55` status `ready` deltaP `8.0321` edge `0.1217` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3223` n `55` status `ready` deltaP `3.7752` edge `0.1521` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8852` n `55` status `ready` deltaP `11.0261` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
