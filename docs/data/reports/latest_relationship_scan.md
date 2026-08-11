# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T18:07:38.354403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11856`

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

- `market_context_high->unknown_24h` score `4.7591` n `140` status `ready` deltaP `-21.6291` edge `0.7862` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.5606` n `32` status `ready` deltaP `18.064` edge `0.1112` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.5606` n `32` status `ready` deltaP `18.064` edge `0.1112` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.1593` n `32` status `ready` deltaP `12.3129` edge `0.0378` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1593` n `32` status `ready` deltaP `12.3129` edge `0.0378` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9707` n `32` status `ready` deltaP `11.2043` edge `0.0203` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9707` n `32` status `ready` deltaP `11.2043` edge `0.0203` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.7858` n `181` status `ready` deltaP `11.2097` edge `0.0546` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.7194` n `181` status `ready` deltaP `9.8612` edge `0.0264` maxDD `-0.5752`
- `market_context_high->commodity_24h` score `0.6451` n `140` status `ready` deltaP `9.5679` edge `0.0703` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.2937` n `32` status `ready` deltaP `9.9551` edge `0.0088` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2937` n `32` status `ready` deltaP `9.9551` edge `0.0088` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1622` n `32` status `ready` deltaP `5.0524` edge `0.0026` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1622` n `32` status `ready` deltaP `5.0524` edge `0.0026` maxDD `-0.1547`
- `market_context_high->fx_24h` score `0.106` n `140` status `ready` deltaP `10.7328` edge `0.0228` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.0855` n `181` status `ready` deltaP `4.6035` edge `0.0007` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.124` n `181` status `ready` deltaP `5.8003` edge `0.0059` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.3714` n `32` status `ready` deltaP `0.0762` edge `0.0101` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3714` n `32` status `ready` deltaP `0.0762` edge `0.0101` maxDD `-0.6579`
- `risk_on_high->crypto_major_4h` score `-0.6757` n `32` status `ready` deltaP `-0.4573` edge `-0.0109` maxDD `-2.1479`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
