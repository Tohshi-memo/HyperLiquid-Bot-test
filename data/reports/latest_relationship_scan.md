# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T17:44:46.901756+00:00`
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

- `market_context_high->unknown_24h` score `7.7474` n `139` status `ready` deltaP `-21.3707` edge `1.0335` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.621` n `32` status `ready` deltaP `18.3689` edge `0.1142` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.621` n `32` status `ready` deltaP `18.3689` edge `0.1142` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.1809` n `32` status `ready` deltaP `12.4626` edge `0.0386` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1809` n `32` status `ready` deltaP `12.4626` edge `0.0386` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9963` n `32` status `ready` deltaP `11.5091` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9963` n `32` status `ready` deltaP `11.5091` edge `0.0204` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.8462` n `181` status `ready` deltaP `11.5146` edge `0.0576` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.741` n `181` status `ready` deltaP `10.0109` edge `0.0272` maxDD `-0.5752`
- `market_context_high->commodity_24h` score `0.7138` n `139` status `ready` deltaP `9.7964` edge `0.0745` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.2937` n `32` status `ready` deltaP `9.9551` edge `0.0088` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2937` n `32` status `ready` deltaP `9.9551` edge `0.0088` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1873` n `32` status `ready` deltaP `5.3518` edge `0.0027` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1873` n `32` status `ready` deltaP `5.3518` edge `0.0027` maxDD `-0.1547`
- `market_context_high->fx_24h` score `0.1151` n `139` status `ready` deltaP `10.8487` edge `0.0232` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.0691` n `181` status `ready` deltaP `4.9029` edge `0.0008` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1074` n `181` status `ready` deltaP `6.1051` edge `0.006` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.3974` n `32` status `ready` deltaP `-0.2287` edge `0.0088` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3974` n `32` status `ready` deltaP `-0.2287` edge `0.0088` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6835` n `32` status `ready` deltaP `-3.4618` edge `-0.0102` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
