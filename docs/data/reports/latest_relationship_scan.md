# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T13:07:27.874408+00:00`
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

- `market_context_high->unknown_24h` score `7031.5934` n `55` status `ready` deltaP `1.5625` edge `585.9557` maxDD `0.0`
- `market_context_high->unknown_4h` score `378.4451` n `55` status `ready` deltaP `5.0416` edge `31.5078` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `67.4332` n `55` status `ready` deltaP `3.1628` edge `5.6094` maxDD `-0.2178`
- `news_risk_high->unknown_1h` score `29.2124` n `128` status `ready` deltaP `-6.2406` edge `2.5046` maxDD `-0.9571`
- `market_context_high->equity_24h` score `21.2253` n `55` status `ready` deltaP `43.8415` edge `1.5001` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.7808` n `98` status `ready` deltaP `29.6379` edge `1.0031` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.8717` n `55` status `ready` deltaP `56.0764` edge `0.1988` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.4869` n `55` status `ready` deltaP `45.7892` edge `0.2664` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.9245` n `55` status `ready` deltaP `23.75` edge `0.3648` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4883` n `55` status `ready` deltaP `30.2827` edge `0.2891` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.1444` n `116` status `ready` deltaP `15.3017` edge `0.382` maxDD `-7.4246`
- `market_context_high->equity_4h` score `3.3582` n `55` status `ready` deltaP `5.4379` edge `0.3138` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3551` n `55` status `ready` deltaP `31.5244` edge `0.0945` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4561` n `55` status `ready` deltaP `11.0322` edge `0.309` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7688` n `55` status `ready` deltaP `-5.1673` edge `0.413` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5642` n `55` status `ready` deltaP `18.3508` edge `0.0505` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4925` n `55` status `ready` deltaP `2.7273` edge `0.1587` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.394` n `55` status `ready` deltaP `8.1818` edge `0.1226` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3379` n `55` status `ready` deltaP `3.7752` edge `0.1534` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9103` n `55` status `ready` deltaP `11.3255` edge `0.0252` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
