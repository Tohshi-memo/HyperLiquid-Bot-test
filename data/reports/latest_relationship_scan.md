# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T11:07:25.299592+00:00`
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

- `risk_on_high->unknown_1h` score `7.2255` n `35` status `ready` deltaP `2.4893` edge `0.625` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2255` n `35` status `ready` deltaP `2.4893` edge `0.625` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.6024` n `92` status `ready` deltaP `8.7938` edge `0.2959` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.2559` n `92` status `ready` deltaP `18.9236` edge `-0.0215` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1767` n `35` status `ready` deltaP `16.2848` edge `0.0036` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1767` n `35` status `ready` deltaP `16.2848` edge `0.0036` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0827` n `35` status `ready` deltaP `12.1086` edge `0.0401` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0827` n `35` status `ready` deltaP `12.1086` edge `0.0401` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.8856` n `35` status `ready` deltaP `13.3576` edge `0.0391` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.8856` n `35` status `ready` deltaP `13.3576` edge `0.0391` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8046` n `35` status `ready` deltaP `13.7939` edge `0.0126` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8046` n `35` status `ready` deltaP `13.7939` edge `0.0126` maxDD `-0.3343`
- `market_context_high->equity_24h` score `0.635` n `92` status `ready` deltaP `13.4436` edge `-0.0158` maxDD `-0.6726`
- `market_context_high->commodity_24h` score `0.3311` n `92` status `ready` deltaP `17.9952` edge `0.1058` maxDD `-4.666`
- `risk_on_high->commodity_4h` score `0.3297` n `35` status `ready` deltaP `2.4564` edge `0.074` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3297` n `35` status `ready` deltaP `2.4564` edge `0.074` maxDD `-1.3651`
- `market_context_high->commodity_4h` score `0.2801` n `128` status `ready` deltaP `10.6707` edge `0.0498` maxDD `-2.4692`
- `risk_on_high->crypto_major_4h` score `0.262` n `35` status `ready` deltaP `3.3711` edge `0.0823` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.262` n `35` status `ready` deltaP `3.3711` edge `0.0823` maxDD `-2.0278`
- `risk_on_high->fx_1h` score `0.0788` n `35` status `ready` deltaP `4.5851` edge `0.0023` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
