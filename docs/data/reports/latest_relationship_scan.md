# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T05:37:33.412221+00:00`
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

- `risk_on_high->unknown_1h` score `3.8601` n `34` status `ready` deltaP `3.9363` edge `0.3349` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `3.8601` n `34` status `ready` deltaP `3.9363` edge `0.3349` maxDD `-0.8243`
- `market_context_high->commodity_24h` score `2.8642` n `75` status `ready` deltaP `28.9583` edge `0.118` maxDD `-1.4563`
- `market_context_high->crypto_major_24h` score `1.9772` n `75` status `ready` deltaP `4.7291` edge `0.2709` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4661` n `75` status `ready` deltaP `21.7014` edge `-0.0225` maxDD `0.0`
- `market_context_high->equity_24h` score `1.3671` n `75` status `ready` deltaP `15.7847` edge `0.0296` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.2355` n `34` status `ready` deltaP `13.658` edge `0.0425` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.2355` n `34` status `ready` deltaP `13.658` edge `0.0425` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.8934` n `34` status `ready` deltaP `13.6492` edge `0.0378` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.8934` n `34` status `ready` deltaP `13.6492` edge `0.0378` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.6825` n `106` status `ready` deltaP `12.3792` edge `0.0547` maxDD `-0.9783`
- `risk_on_high->index_1h` score `0.5166` n `34` status `ready` deltaP `13.702` edge `0.0124` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.5166` n `34` status `ready` deltaP `13.702` edge `0.0124` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `-0.0269` n `34` status `ready` deltaP `2.6418` edge `0.0017` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `-0.0269` n `34` status `ready` deltaP `2.6418` edge `0.0017` maxDD `-0.1547`
- `risk_on_high->commodity_1h` score `-0.0762` n `34` status `ready` deltaP `0.8454` edge `0.014` maxDD `-0.4124`
- `risk_on_and_context->commodity_1h` score `-0.0762` n `34` status `ready` deltaP `0.8454` edge `0.014` maxDD `-0.4124`
- `market_context_high->metal_4h` score `-0.2041` n `106` status `ready` deltaP `16.2764` edge `0.0152` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.3587` n `118` status `ready` deltaP `-1.1469` edge `-0.0013` maxDD `-0.2968`
- `market_context_high->commodity_1h` score `-0.4293` n `118` status `ready` deltaP `-2.0958` edge `0.0068` maxDD `-1.1622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
