# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T03:22:27.707085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10432`

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

- `risk_on_high->commodity_24h` score `6.6988` n `55` status `ready` deltaP `37.5546` edge `0.3134` maxDD `-0.1088`
- `risk_on_and_context->commodity_24h` score `6.6988` n `55` status `ready` deltaP `37.5546` edge `0.3134` maxDD `-0.1088`
- `market_context_high->crypto_major_4h` score `1.4772` n `163` status `ready` deltaP `15.1569` edge `0.3625` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `0.8835` n `116` status `ready` deltaP `15.2349` edge `0.1458` maxDD `-7.2326`
- `market_context_high->crypto_major_1h` score `0.4763` n `163` status `ready` deltaP `4.0171` edge `0.1018` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.3352` n `163` status `ready` deltaP `8.0737` edge `0.1241` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.2213` n `91` status `ready` deltaP `13.7614` edge `0.1847` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.2213` n `91` status `ready` deltaP `13.7614` edge `0.1847` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0124` n `91` status `ready` deltaP `4.7058` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0124` n `91` status `ready` deltaP `4.7058` edge `0.006` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1566` n `163` status `ready` deltaP `7.4025` edge `0.0054` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2492` n `91` status `ready` deltaP `1.3481` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2492` n `91` status `ready` deltaP `1.3481` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3375` n `163` status `ready` deltaP `5.2762` edge `0.0085` maxDD `-0.9556`
- `market_context_high->metal_4h` score `-0.3944` n `163` status `ready` deltaP `8.7208` edge `0.0427` maxDD `-1.6961`
- `risk_on_high->equity_1h` score `-0.4188` n `91` status `ready` deltaP `9.5585` edge `0.031` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4188` n `91` status `ready` deltaP `9.5585` edge `0.031` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.486` n `91` status `ready` deltaP `0.9952` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.486` n `91` status `ready` deltaP `0.9952` edge `0.0042` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5479` n `163` status `ready` deltaP `-2.4475` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
