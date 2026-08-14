# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T03:07:32.148884+00:00`
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

- `market_context_high->unknown_24h` score `90.6094` n `150` status `ready` deltaP `-28.9306` edge `8.0349` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.3554` n `32` status `ready` deltaP `-43.0556` edge `4.6384` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.3554` n `32` status `ready` deltaP `-43.0556` edge `4.6384` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.7906` n `36` status `ready` deltaP `10.0694` edge `0.7867` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.7798` n `36` status `ready` deltaP `36.4329` edge `0.3221` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7493` n `32` status `ready` deltaP `32.2917` edge `0.1805` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7493` n `32` status `ready` deltaP `32.2917` edge `0.1805` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0027` n `32` status `ready` deltaP `21.2652` edge `0.1267` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0027` n `32` status `ready` deltaP `21.2652` edge `0.1267` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.8222` n `150` status `ready` deltaP `22.2917` edge `0.1669` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.2923` n `36` status `ready` deltaP `14.5833` edge `0.0938` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.6412` n `150` status `ready` deltaP `17.8069` edge `0.0819` maxDD `-2.1077`
- `news_risk_high->index_4h` score `1.5645` n `36` status `ready` deltaP `18.6992` edge `0.0189` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.5332` n `36` status `ready` deltaP `7.535` edge `0.1094` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.333` n `32` status `ready` deltaP `14.1093` edge `0.0403` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.333` n `32` status `ready` deltaP `14.1093` edge `0.0403` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.3022` n `32` status `ready` deltaP `15.2778` edge `0.0251` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.3022` n `32` status `ready` deltaP `15.2778` edge `0.0251` maxDD `-0.1418`
- `risk_on_high->fx_4h` score `1.045` n `32` status `ready` deltaP `12.1189` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.045` n `32` status `ready` deltaP `12.1189` edge `0.0204` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
