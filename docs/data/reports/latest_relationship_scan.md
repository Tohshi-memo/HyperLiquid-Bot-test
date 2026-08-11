# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T19:37:29.013540+00:00`
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

- `risk_on_high->commodity_4h` score `2.4227` n `32` status `ready` deltaP `17.1494` edge `0.1058` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.4227` n `32` status `ready` deltaP `17.1494` edge `0.1058` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.1029` n `32` status `ready` deltaP `12.0135` edge `0.0351` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1029` n `32` status `ready` deltaP `12.0135` edge `0.0351` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9719` n `32` status `ready` deltaP `11.2043` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9719` n `32` status `ready` deltaP `11.2043` edge `0.0204` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6631` n `181` status `ready` deltaP `9.5618` edge `0.0237` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.6479` n `181` status `ready` deltaP `10.2951` edge `0.0492` maxDD `-2.1077`
- `market_context_high->commodity_24h` score `0.4051` n `145` status `ready` deltaP `8.5783` edge `0.0569` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.3334` n `32` status `ready` deltaP `10.5539` edge `0.0099` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3334` n `32` status `ready` deltaP `10.5539` edge `0.0099` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1131` n `32` status `ready` deltaP `4.4536` edge `0.0025` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1131` n `32` status `ready` deltaP `4.4536` edge `0.0025` maxDD `-0.1547`
- `market_context_high->fx_24h` score `-0.1039` n `145` status `ready` deltaP `9.556` edge `0.0204` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.1174` n `181` status `ready` deltaP `4.0047` edge `0.0006` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1232` n `181` status `ready` deltaP `5.8003` edge `0.006` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.288` n `32` status `ready` deltaP `0.9909` edge `0.0147` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.288` n `32` status `ready` deltaP `0.9909` edge `0.0147` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6593` n `32` status `ready` deltaP `-3.3121` edge `-0.0081` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6593` n `32` status `ready` deltaP `-3.3121` edge `-0.0081` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
