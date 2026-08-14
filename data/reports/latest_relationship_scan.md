# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T04:07:30.373344+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `90.4699` n `150` status `ready` deltaP `-29.625` edge `8.0279` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.2647` n `32` status `ready` deltaP `-43.75` edge `4.6314` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.2647` n `32` status `ready` deltaP `-43.75` edge `4.6314` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.8602` n `36` status `ready` deltaP `10.0694` edge `0.7925` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.8814` n `36` status `ready` deltaP `37.0427` edge `0.3265` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7625` n `32` status `ready` deltaP `32.2917` edge `0.1816` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7625` n `32` status `ready` deltaP `32.2917` edge `0.1816` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.993` n `32` status `ready` deltaP `21.1128` edge `0.1269` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.993` n `32` status `ready` deltaP `21.1128` edge `0.1269` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.8354` n `150` status `ready` deltaP `22.2917` edge `0.168` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.2923` n `36` status `ready` deltaP `14.5833` edge `0.0938` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.6314` n `150` status `ready` deltaP `17.6545` edge `0.0821` maxDD `-2.1077`
- `news_risk_high->index_4h` score `1.6241` n `36` status `ready` deltaP `19.3089` edge `0.0198` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.5152` n `36` status `ready` deltaP `7.3853` edge `0.1089` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3474` n `32` status `ready` deltaP `14.259` edge `0.0405` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3474` n `32` status `ready` deltaP `14.259` edge `0.0405` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2962` n `32` status `ready` deltaP `15.2778` edge `0.0246` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2962` n `32` status `ready` deltaP `15.2778` edge `0.0246` maxDD `-0.1418`
- `risk_on_high->fx_4h` score `1.0462` n `32` status `ready` deltaP `12.1189` edge `0.0205` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0462` n `32` status `ready` deltaP `12.1189` edge `0.0205` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
