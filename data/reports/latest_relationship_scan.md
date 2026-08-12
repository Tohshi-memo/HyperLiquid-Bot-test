# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T05:37:27.307247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11888`

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

- `risk_on_high->commodity_4h` score `2.0996` n `32` status `ready` deltaP `14.1006` edge `0.0992` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.0996` n `32` status `ready` deltaP `14.1006` edge `0.0992` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0238` n `32` status `ready` deltaP `11.265` edge `0.0335` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0238` n `32` status `ready` deltaP `11.265` edge `0.0335` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8525` n `32` status `ready` deltaP `9.8323` edge `0.0196` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8525` n `32` status `ready` deltaP `9.8323` edge `0.0196` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6171` n `180` status `ready` deltaP `9.1817` edge `0.0224` maxDD `-0.5752`
- `risk_on_high->index_1h` score `0.3887` n `32` status `ready` deltaP `11.4521` edge `0.011` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3887` n `32` status `ready` deltaP `11.4521` edge `0.011` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.366` n `180` status `ready` deltaP `7.6423` edge `0.0434` maxDD `-2.1077`
- `risk_on_high->fx_1h` score `0.2017` n `32` status `ready` deltaP `5.5015` edge `0.0029` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2017` n `32` status `ready` deltaP `5.5015` edge `0.0029` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0733` n `180` status `ready` deltaP `4.8071` edge `0.0009` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.2154` n `180` status `ready` deltaP `4.2073` edge `0.0048` maxDD `-0.504`
- `market_context_high->commodity_24h` score `-0.2744` n `176` status `ready` deltaP `6.5499` edge `0.0138` maxDD `-2.4263`
- `risk_on_high->index_4h` score `-0.3302` n `32` status `ready` deltaP `-0.0762` edge `0.0164` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3302` n `32` status `ready` deltaP `-0.0762` edge `0.0164` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6508` n `32` status `ready` deltaP `-3.0127` edge `-0.009` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6508` n `32` status `ready` deltaP `-3.0127` edge `-0.009` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.7683` n `180` status `ready` deltaP `-6.0479` edge `-0.0005` maxDD `-0.948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
