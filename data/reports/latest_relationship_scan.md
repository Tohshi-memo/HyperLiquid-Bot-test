# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T16:07:27.869026+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `17.0085` n `136` status `ready` deltaP `-20.3423` edge `1.7984` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.8212` n `32` status `ready` deltaP `19.1311` edge `0.1258` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8212` n `32` status `ready` deltaP `19.1311` edge `0.1258` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.2888` n `32` status `ready` deltaP `13.0614` edge `0.0436` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2888` n `32` status `ready` deltaP `13.0614` edge `0.0436` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0266` n `32` status `ready` deltaP `11.814` edge `0.0209` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0266` n `32` status `ready` deltaP `11.814` edge `0.0209` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.8277` n `182` status `ready` deltaP `11.8852` edge `0.0612` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.774` n `182` status `ready` deltaP `10.2455` edge `0.0299` maxDD `-0.6965`
- `market_context_high->commodity_24h` score `0.689` n `136` status `ready` deltaP `9.7359` edge `0.0812` maxDD `-3.0953`
- `risk_on_high->index_1h` score `0.2384` n `32` status `ready` deltaP `9.0569` edge `0.0077` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2384` n `32` status `ready` deltaP `9.0569` edge `0.0077` maxDD `-0.3343`
- `market_context_high->fx_24h` score `0.2275` n `136` status `ready` deltaP `12.6657` edge `0.0255` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2161` n `32` status `ready` deltaP `5.6512` edge `0.0031` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2161` n `32` status `ready` deltaP `5.6512` edge `0.0031` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0672` n `182` status `ready` deltaP `4.8957` edge `0.0011` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1087` n `182` status `ready` deltaP `6.0791` edge `0.006` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.4754` n `32` status `ready` deltaP `-1.1433` edge `0.0049` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.4754` n `32` status `ready` deltaP `-1.1433` edge `0.0049` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7684` n `32` status `ready` deltaP `-4.36` edge `-0.0151` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
