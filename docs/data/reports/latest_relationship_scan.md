# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T23:07:25.033792+00:00`
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

- `risk_on_high->commodity_4h` score `2.3183` n `32` status `ready` deltaP `16.2348` edge `0.1032` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3183` n `32` status `ready` deltaP `16.2348` edge `0.1032` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0993` n `32` status `ready` deltaP `12.0135` edge `0.0348` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0993` n `32` status `ready` deltaP `12.0135` edge `0.0348` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0107` n `32` status `ready` deltaP `11.5091` edge `0.0216` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0107` n `32` status `ready` deltaP `11.5091` edge `0.0216` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6925` n `180` status `ready` deltaP `9.9302` edge `0.0237` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5848` n `180` status `ready` deltaP `9.7765` edge `0.0474` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3918` n `32` status `ready` deltaP `11.4521` edge `0.0114` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3918` n `32` status `ready` deltaP `11.4521` edge `0.0114` maxDD `-0.3343`
- `market_context_high->commodity_24h` score `0.1962` n `151` status `ready` deltaP `7.9918` edge `0.0434` maxDD `-2.4263`
- `risk_on_high->fx_1h` score `0.1646` n `32` status `ready` deltaP `5.0524` edge `0.0028` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1646` n `32` status `ready` deltaP `5.0524` edge `0.0028` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0975` n `180` status `ready` deltaP `4.358` edge `0.0008` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1126` n `180` status `ready` deltaP `5.8841` edge `0.0068` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.2291` n `32` status `ready` deltaP `1.4482` edge `0.0192` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.2291` n `32` status `ready` deltaP `1.4482` edge `0.0192` maxDD `-0.6579`
- `market_context_high->fx_24h` score `-0.401` n `151` status `ready` deltaP `8.6804` edge `0.0179` maxDD `-1.508`
- `risk_on_high->equity_1h` score `-0.6118` n `32` status `ready` deltaP `-3.0127` edge `-0.004` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6118` n `32` status `ready` deltaP `-3.0127` edge `-0.004` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
