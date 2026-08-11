# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T16:22:25.637947+00:00`
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

- `market_context_high->unknown_24h` score `13.8886` n `137` status `ready` deltaP `-20.6252` edge `1.5403` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.7838` n `32` status `ready` deltaP `18.9787` edge `0.1237` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7838` n `32` status `ready` deltaP `18.9787` edge `0.1237` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.2708` n `32` status `ready` deltaP `12.9117` edge `0.0431` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2708` n `32` status `ready` deltaP `12.9117` edge `0.0431` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0133` n `32` status `ready` deltaP `11.6616` edge `0.0208` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0133` n `32` status `ready` deltaP `11.6616` edge `0.0208` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.7903` n `182` status `ready` deltaP `11.7328` edge `0.0591` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.756` n `182` status `ready` deltaP `10.0958` edge `0.0294` maxDD `-0.6965`
- `market_context_high->commodity_24h` score `0.641` n `137` status `ready` deltaP `9.6915` edge `0.0775` maxDD `-3.0953`
- `risk_on_high->index_1h` score `0.2478` n `32` status `ready` deltaP `9.2066` edge `0.0079` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2478` n `32` status `ready` deltaP `9.2066` edge `0.0079` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.2029` n `32` status `ready` deltaP `5.5015` edge `0.003` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2029` n `32` status `ready` deltaP `5.5015` edge `0.003` maxDD `-0.1547`
- `market_context_high->fx_24h` score `0.1959` n `137` status `ready` deltaP `12.1773` edge `0.0247` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.0757` n `182` status `ready` deltaP `4.746` edge `0.001` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1174` n `182` status `ready` deltaP `5.9267` edge `0.0059` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.4628` n `32` status `ready` deltaP `-0.9909` edge `0.0055` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.4628` n `32` status `ready` deltaP `-0.9909` edge `0.0055` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7497` n `32` status `ready` deltaP `-4.2103` edge `-0.0137` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
