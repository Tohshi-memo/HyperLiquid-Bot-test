# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T17:52:32.157075+00:00`
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

- `market_context_high->unknown_24h` score `7.7685` n `139` status `ready` deltaP `-21.1974` edge `1.0341` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.586` n `32` status `ready` deltaP `18.2165` edge `0.1123` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.586` n `32` status `ready` deltaP `18.2165` edge `0.1123` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.1593` n `32` status `ready` deltaP `12.3129` edge `0.0378` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1593` n `32` status `ready` deltaP `12.3129` edge `0.0378` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9829` n `32` status `ready` deltaP `11.3567` edge `0.0203` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9829` n `32` status `ready` deltaP `11.3567` edge `0.0203` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.8112` n `181` status `ready` deltaP `11.3622` edge `0.0557` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.7194` n `181` status `ready` deltaP `9.8612` edge `0.0264` maxDD `-0.5752`
- `market_context_high->commodity_24h` score `0.6771` n `139` status `ready` deltaP `9.623` edge `0.0726` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.3023` n `32` status `ready` deltaP `10.1048` edge `0.0089` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3023` n `32` status `ready` deltaP `10.1048` edge `0.0089` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1754` n `32` status `ready` deltaP `5.2021` edge `0.0027` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1754` n `32` status `ready` deltaP `5.2021` edge `0.0027` maxDD `-0.1547`
- `market_context_high->fx_24h` score `0.1257` n `139` status `ready` deltaP `11.022` edge `0.0234` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.0769` n `181` status `ready` deltaP `4.7532` edge `0.0008` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1161` n `181` status `ready` deltaP `5.9527` edge `0.0059` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.3848` n `32` status `ready` deltaP `-0.0762` edge `0.0094` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3848` n `32` status `ready` deltaP `-0.0762` edge `0.0094` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6741` n `32` status `ready` deltaP `-3.3121` edge `-0.01` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
