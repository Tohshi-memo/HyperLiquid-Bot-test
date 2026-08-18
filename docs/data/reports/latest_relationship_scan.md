# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T00:37:29.593810+00:00`
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

- `risk_on_high->unknown_1h` score `7.5123` n `35` status `ready` deltaP `2.3396` edge `0.6499` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.5123` n `35` status `ready` deltaP `2.3396` edge `0.6499` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `5.3097` n `75` status `ready` deltaP `18.595` edge `0.4393` maxDD `-4.9964`
- `market_context_high->equity_24h` score `2.7652` n `75` status `ready` deltaP `16.9844` edge `0.1172` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1353` n `35` status `ready` deltaP `15.8275` edge `0.0032` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1353` n `35` status `ready` deltaP `15.8275` edge `0.0032` maxDD `-0.1285`
- `market_context_high->index_24h` score `1.1059` n `75` status `ready` deltaP `17.7308` edge `-0.0217` maxDD `-0.0141`
- `risk_on_high->crypto_major_1h` score `0.8765` n `35` status `ready` deltaP `10.7613` edge `0.0319` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.8765` n `35` status `ready` deltaP `10.7613` edge `0.0319` maxDD `-1.1144`
- `risk_on_high->index_1h` score `0.8261` n `35` status `ready` deltaP `14.0933` edge `0.0124` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8261` n `35` status `ready` deltaP `14.0933` edge `0.0124` maxDD `-0.3343`
- `risk_on_high->equity_1h` score `0.6567` n `35` status `ready` deltaP `11.7108` edge `0.031` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.6567` n `35` status `ready` deltaP `11.7108` edge `0.031` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.3642` n `117` status `ready` deltaP `10.0467` edge `0.0484` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `0.2825` n `75` status `ready` deltaP `13.7794` edge `0.115` maxDD `-4.666`
- `market_context_high->index_1h` score `0.2392` n `117` status `ready` deltaP `8.4767` edge `0.0054` maxDD `-0.3584`
- `risk_on_high->commodity_4h` score `0.1912` n `35` status `ready` deltaP `1.0845` edge `0.0716` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.1912` n `35` status `ready` deltaP `1.0845` edge `0.0716` maxDD `-1.3651`
- `risk_on_high->fx_1h` score `0.1185` n `35` status `ready` deltaP `5.3336` edge `0.0024` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1185` n `35` status `ready` deltaP `5.3336` edge `0.0024` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
