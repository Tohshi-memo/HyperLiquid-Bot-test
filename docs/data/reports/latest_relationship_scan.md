# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T03:22:26.098890+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11872`

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

- `risk_on_high->commodity_4h` score `2.158` n `32` status `ready` deltaP `14.7104` edge `0.1` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.158` n `32` status `ready` deltaP `14.7104` edge `0.1` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0358` n `32` status `ready` deltaP `11.4147` edge `0.0335` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0358` n `32` status `ready` deltaP `11.4147` edge `0.0335` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9815` n `32` status `ready` deltaP `11.2043` edge `0.0212` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9815` n `32` status `ready` deltaP `11.2043` edge `0.0212` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.629` n `180` status `ready` deltaP `9.3314` edge `0.0224` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.4244` n `180` status `ready` deltaP `8.2521` edge `0.0442` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3537` n `32` status `ready` deltaP `10.8533` edge `0.0105` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3537` n `32` status `ready` deltaP `10.8533` edge `0.0105` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1766` n `32` status `ready` deltaP `5.2021` edge `0.0028` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1766` n `32` status `ready` deltaP `5.2021` edge `0.0028` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0897` n `180` status `ready` deltaP `4.5077` edge `0.0008` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1316` n `180` status `ready` deltaP `5.5793` edge `0.0064` maxDD `-0.504`
- `market_context_high->commodity_24h` score `-0.1633` n `168` status `ready` deltaP `6.9334` edge `0.0205` maxDD `-2.4263`
- `risk_on_high->index_4h` score `-0.3216` n `32` status `ready` deltaP `-0.0762` edge `0.0175` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3216` n `32` status `ready` deltaP `-0.0762` edge `0.0175` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7076` n `32` status `ready` deltaP `-3.7612` edge `-0.0113` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.7076` n `32` status `ready` deltaP `-3.7612` edge `-0.0113` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.8034` n `180` status `ready` deltaP `-6.6467` edge `-0.001` maxDD `-0.948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
