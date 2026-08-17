# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T04:54:23.897116+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.4017` n `72` status `ready` deltaP `31.7708` edge `0.1253` maxDD `-0.957`
- `market_context_high->crypto_major_24h` score `1.7099` n `72` status `ready` deltaP `3.4723` edge `0.257` maxDD `-5.6792`
- `risk_on_high->crypto_major_1h` score `1.548` n `31` status `ready` deltaP `16.5443` edge `0.0493` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.548` n `31` status `ready` deltaP `16.5443` edge `0.0493` maxDD `-1.1144`
- `market_context_high->equity_24h` score `1.4817` n `72` status `ready` deltaP `15.9723` edge `0.0379` maxDD `-0.6726`
- `market_context_high->index_24h` score `1.4673` n `72` status `ready` deltaP `21.7014` edge `-0.0224` maxDD `0.0`
- `market_context_high->commodity_4h` score `0.7103` n `104` status `ready` deltaP `12.5352` edge `0.0562` maxDD `-0.8962`
- `risk_on_high->equity_1h` score `0.4482` n `31` status `ready` deltaP `11.3869` edge `0.0359` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.4482` n `31` status `ready` deltaP `11.3869` edge `0.0359` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.3741` n `31` status `ready` deltaP `10.8557` edge `0.0131` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3741` n `31` status `ready` deltaP `10.8557` edge `0.0131` maxDD `-0.3343`
- `risk_on_high->commodity_1h` score `0.0978` n `31` status `ready` deltaP `2.8926` edge `0.0183` maxDD `-0.3372`
- `risk_on_and_context->commodity_1h` score `0.0978` n `31` status `ready` deltaP `2.8926` edge `0.0183` maxDD `-0.3372`
- `risk_on_high->fx_1h` score `0.0569` n `31` status `ready` deltaP `4.2399` edge `0.0018` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0569` n `31` status `ready` deltaP `4.2399` edge `0.0018` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.1911` n `104` status `ready` deltaP `16.3345` edge `0.0159` maxDD `-4.5909`
- `risk_on_high->crypto_alt_1h` score `-0.2921` n `31` status `ready` deltaP `0.565` edge `0.0316` maxDD `-1.7766`
- `risk_on_and_context->crypto_alt_1h` score `-0.2921` n `31` status `ready` deltaP `0.565` edge `0.0316` maxDD `-1.7766`
- `market_context_high->fx_1h` score `-0.3536` n `115` status `ready` deltaP `-1.0336` edge `-0.0014` maxDD `-0.2968`
- `market_context_high->commodity_1h` score `-0.383` n `115` status `ready` deltaP `-1.5113` edge `0.0079` maxDD `-1.087`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
