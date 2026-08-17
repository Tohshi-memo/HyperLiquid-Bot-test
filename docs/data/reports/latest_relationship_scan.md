# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T22:45:20.692415+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11835`

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

- `risk_on_high->unknown_1h` score `7.4703` n `35` status `ready` deltaP `2.1899` edge `0.6474` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.4703` n `35` status `ready` deltaP `2.1899` edge `0.6474` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `4.8697` n `77` status `ready` deltaP `19.0799` edge `0.3994` maxDD `-4.9964`
- `market_context_high->equity_24h` score `3.0616` n `77` status `ready` deltaP `16.9844` edge `0.1419` maxDD `0.0`
- `market_context_high->index_24h` score `1.3193` n `77` status `ready` deltaP `18.8908` edge `-0.016` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1365` n `35` status `ready` deltaP `15.8275` edge `0.0033` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1365` n `35` status `ready` deltaP `15.8275` edge `0.0033` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `0.9508` n `35` status `ready` deltaP `11.3601` edge `0.0341` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.9508` n `35` status `ready` deltaP `11.3601` edge `0.0341` maxDD `-1.1144`
- `risk_on_high->index_1h` score `0.8141` n `35` status `ready` deltaP `13.9436` edge `0.0124` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8141` n `35` status `ready` deltaP `13.9436` edge `0.0124` maxDD `-0.3343`
- `risk_on_high->equity_1h` score `0.6579` n `35` status `ready` deltaP `11.7108` edge `0.0311` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.6579` n `35` status `ready` deltaP `11.7108` edge `0.0311` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.5047` n `124` status `ready` deltaP `11.9689` edge `0.0473` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.1838` n `35` status `ready` deltaP `0.932` edge `0.072` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.1838` n `35` status `ready` deltaP `0.932` edge `0.072` maxDD `-1.3651`
- `risk_on_high->fx_1h` score `0.0944` n `35` status `ready` deltaP `4.8845` edge `0.0023` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0944` n `35` status `ready` deltaP `4.8845` edge `0.0023` maxDD `-0.1547`
- `market_context_high->commodity_24h` score `0.0881` n `77` status `ready` deltaP `14.853` edge `0.0956` maxDD `-4.666`
- `market_context_high->index_1h` score `0.0458` n `124` status `ready` deltaP `6.2247` edge `0.0043` maxDD `-0.3584`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
