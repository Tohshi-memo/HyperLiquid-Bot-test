# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T08:37:25.081000+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11803`

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

- `risk_on_high->unknown_1h` score `7.2867` n `35` status `ready` deltaP `2.3396` edge `0.6311` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2867` n `35` status `ready` deltaP `2.3396` edge `0.6311` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.7854` n `87` status `ready` deltaP `8.5309` edge `0.3129` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4037` n `87` status `ready` deltaP `20.4861` edge `-0.0196` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.3307` n `34` status `ready` deltaP `18.1492` edge `0.004` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.3307` n `34` status `ready` deltaP `18.1492` edge `0.004` maxDD `-0.1285`
- `market_context_high->equity_24h` score `1.1387` n `87` status `ready` deltaP `14.8048` edge `0.0171` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.1175` n `35` status `ready` deltaP `12.2583` edge `0.042` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.1175` n `35` status `ready` deltaP `12.2583` edge `0.042` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.9731` n `35` status `ready` deltaP `14.1061` edge `0.0414` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.9731` n `35` status `ready` deltaP `14.1061` edge `0.0414` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8561` n `35` status `ready` deltaP `14.3927` edge `0.0129` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8561` n `35` status `ready` deltaP `14.3927` edge `0.0129` maxDD `-0.3343`
- `market_context_high->commodity_24h` score `0.5758` n `87` status `ready` deltaP `20.0072` edge `0.0961` maxDD `-4.12`
- `risk_on_high->crypto_major_4h` score `0.4412` n `34` status `ready` deltaP `5.2726` edge `0.0926` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.4412` n `34` status `ready` deltaP `5.2726` edge `0.0926` maxDD `-2.0278`
- `risk_on_high->commodity_4h` score `0.2174` n `34` status `ready` deltaP `1.1119` edge `0.0736` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.2174` n `34` status `ready` deltaP `1.1119` edge `0.0736` maxDD `-1.3651`
- `risk_on_high->fx_1h` score `0.0944` n `35` status `ready` deltaP `4.8845` edge `0.0023` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0944` n `35` status `ready` deltaP `4.8845` edge `0.0023` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
