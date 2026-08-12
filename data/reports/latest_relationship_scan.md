# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T01:37:23.920606+00:00`
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

- `risk_on_high->commodity_4h` score `2.2077` n `32` status `ready` deltaP `15.1677` edge `0.1011` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2077` n `32` status `ready` deltaP `15.1677` edge `0.1011` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0538` n `32` status `ready` deltaP `11.5644` edge `0.034` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0538` n `32` status `ready` deltaP `11.5644` edge `0.034` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0532` n `32` status `ready` deltaP `11.9665` edge `0.0221` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0532` n `32` status `ready` deltaP `11.9665` edge `0.0221` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.647` n `180` status `ready` deltaP `9.4811` edge `0.0229` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.4742` n `180` status `ready` deltaP `8.7094` edge `0.0453` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3934` n `32` status `ready` deltaP `11.4521` edge `0.0116` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3934` n `32` status `ready` deltaP `11.4521` edge `0.0116` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.2041` n `32` status `ready` deltaP `5.5015` edge `0.0031` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2041` n `32` status `ready` deltaP `5.5015` edge `0.0031` maxDD `-0.1547`
- `market_context_high->commodity_24h` score `-0.0293` n `161` status `ready` deltaP `7.3781` edge `0.0287` maxDD `-2.4263`
- `market_context_high->fx_1h` score `-0.0718` n `180` status `ready` deltaP `4.8071` edge `0.0011` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0849` n `180` status `ready` deltaP `6.3415` edge `0.0073` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.29` n `32` status `ready` deltaP `0.3811` edge `0.0185` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.29` n `32` status `ready` deltaP `0.3811` edge `0.0185` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.639` n `32` status `ready` deltaP `-3.3121` edge `-0.0055` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.639` n `32` status `ready` deltaP `-3.3121` edge `-0.0055` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.7636` n `180` status `ready` deltaP `-6.0479` edge `0.0001` maxDD `-0.948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
