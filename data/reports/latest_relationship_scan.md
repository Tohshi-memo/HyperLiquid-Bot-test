# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T15:22:28.668790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11819`

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

- `risk_on_high->unknown_1h` score `7.2376` n `35` status `ready` deltaP `2.0402` edge `0.629` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2376` n `35` status `ready` deltaP `2.0402` edge `0.629` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `3.0036` n `86` status `ready` deltaP `9.4033` edge `0.3084` maxDD `-4.9964`
- `market_context_high->index_24h` score `1.2319` n `86` status `ready` deltaP `18.9236` edge `-0.0235` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2181` n `35` status `ready` deltaP `16.7421` edge `0.004` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2181` n `35` status `ready` deltaP `16.7421` edge `0.004` maxDD `-0.1285`
- `market_context_high->equity_24h` score `1.2` n `86` status `ready` deltaP `15.2091` edge `0.0082` maxDD `-0.1006`
- `risk_on_high->crypto_major_1h` score `0.9724` n `35` status `ready` deltaP `11.5098` edge `0.0349` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.9724` n `35` status `ready` deltaP `11.5098` edge `0.0349` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.7861` n `35` status `ready` deltaP `12.9085` edge `0.0338` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.7861` n `35` status `ready` deltaP `12.9085` edge `0.0338` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.7495` n `35` status `ready` deltaP `13.1951` edge `0.012` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.7495` n `35` status `ready` deltaP `13.1951` edge `0.012` maxDD `-0.3343`
- `risk_on_high->commodity_4h` score `0.4659` n `35` status `ready` deltaP `2.9137` edge `0.0823` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4659` n `35` status `ready` deltaP `2.9137` edge `0.0823` maxDD `-1.3651`
- `market_context_high->commodity_4h` score `0.3662` n `133` status `ready` deltaP `12.5378` edge `0.0484` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `0.3222` n `86` status `ready` deltaP `17.8254` edge `0.1058` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.0951` n `35` status `ready` deltaP `4.8845` edge `0.0024` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0951` n `35` status `ready` deltaP `4.8845` edge `0.0024` maxDD `-0.1547`
- `risk_on_high->crypto_major_4h` score `-0.0112` n `35` status `ready` deltaP `1.2369` edge `0.0615` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
