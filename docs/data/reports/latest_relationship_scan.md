# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T11:37:27.148938+00:00`
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

- `risk_on_high->unknown_1h` score `7.1439` n `35` status `ready` deltaP `2.1899` edge `0.6202` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.1439` n `35` status `ready` deltaP `2.1899` edge `0.6202` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.5182` n `92` status `ready` deltaP `8.4466` edge `0.2912` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.2535` n `92` status `ready` deltaP `18.9236` edge `-0.0217` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1913` n `35` status `ready` deltaP `16.4373` edge `0.0038` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1913` n `35` status `ready` deltaP `16.4373` edge `0.0038` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0827` n `35` status `ready` deltaP `12.1086` edge `0.0401` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0827` n `35` status `ready` deltaP `12.1086` edge `0.0401` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.888` n `35` status `ready` deltaP `13.3576` edge `0.0393` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.888` n `35` status `ready` deltaP `13.3576` edge `0.0393` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.7914` n `35` status `ready` deltaP `13.6442` edge `0.0125` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.7914` n `35` status `ready` deltaP `13.6442` edge `0.0125` maxDD `-0.3343`
- `market_context_high->equity_24h` score `0.5268` n `92` status `ready` deltaP `13.0964` edge `-0.0225` maxDD `-0.6726`
- `market_context_high->commodity_24h` score `0.3678` n `92` status `ready` deltaP `18.3424` edge `0.1082` maxDD `-4.666`
- `risk_on_high->commodity_4h` score `0.3369` n `35` status `ready` deltaP `2.4564` edge `0.0746` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3369` n `35` status `ready` deltaP `2.4564` edge `0.0746` maxDD `-1.3651`
- `market_context_high->commodity_4h` score `0.3303` n `130` status `ready` deltaP `11.2476` edge `0.0524` maxDD `-2.4692`
- `risk_on_high->crypto_major_4h` score `0.236` n `35` status `ready` deltaP `3.0662` edge `0.081` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.236` n `35` status `ready` deltaP `3.0662` edge `0.081` maxDD `-2.0278`
- `risk_on_high->fx_1h` score `0.0866` n `35` status `ready` deltaP `4.7348` edge `0.0023` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
