# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T08:52:24.009023+00:00`
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
- `market_context_high->crypto_major_24h` score `2.7821` n `88` status `ready` deltaP `8.7753` edge `0.311` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.391` n `88` status `ready` deltaP `20.3125` edge `-0.0195` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1633` n `35` status `ready` deltaP `16.1324` edge `0.0035` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1633` n `35` status `ready` deltaP `16.1324` edge `0.0035` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.1211` n `35` status `ready` deltaP `12.2583` edge `0.0423` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.1211` n `35` status `ready` deltaP `12.2583` edge `0.0423` maxDD `-1.1144`
- `market_context_high->equity_24h` score `1.1155` n `88` status `ready` deltaP `14.7096` edge `0.0158` maxDD `-0.6726`
- `risk_on_high->equity_1h` score `0.9587` n `35` status `ready` deltaP `13.9564` edge `0.0412` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.9587` n `35` status `ready` deltaP `13.9564` edge `0.0412` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8561` n `35` status `ready` deltaP `14.3927` edge `0.0129` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8561` n `35` status `ready` deltaP `14.3927` edge `0.0129` maxDD `-0.3343`
- `market_context_high->commodity_24h` score `0.492` n `88` status `ready` deltaP `19.3971` edge `0.0957` maxDD `-4.2878`
- `risk_on_high->crypto_major_4h` score `0.3013` n `35` status `ready` deltaP `3.6759` edge `0.0853` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.3013` n `35` status `ready` deltaP `3.6759` edge `0.0853` maxDD `-2.0278`
- `risk_on_high->commodity_4h` score `0.3009` n `35` status `ready` deltaP `2.4564` edge `0.0716` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3009` n `35` status `ready` deltaP `2.4564` edge `0.0716` maxDD `-1.3651`
- `risk_on_high->fx_1h` score `0.1029` n `35` status `ready` deltaP `5.0342` edge `0.0024` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1029` n `35` status `ready` deltaP `5.0342` edge `0.0024` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
