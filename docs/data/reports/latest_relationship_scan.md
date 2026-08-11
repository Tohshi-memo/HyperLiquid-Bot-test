# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T14:37:37.679984+00:00`
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

- `market_context_high->unknown_24h` score `29.9324` n `132` status `ready` deltaP `-19.4882` edge `2.8697` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `3.0262` n `32` status `ready` deltaP `19.8933` edge `0.1378` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0262` n `32` status `ready` deltaP `19.8933` edge `0.1378` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.3571` n `32` status `ready` deltaP `13.6602` edge `0.0453` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3571` n `32` status `ready` deltaP `13.6602` edge `0.0453` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.1008` n `32` status `ready` deltaP `12.5762` edge `0.022` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1008` n `32` status `ready` deltaP `12.5762` edge `0.022` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `1.0327` n `182` status `ready` deltaP `12.6474` edge `0.0732` maxDD `-2.7169`
- `market_context_high->commodity_24h` score `0.9706` n `132` status `ready` deltaP `10.2411` edge `0.1013` maxDD `-3.0953`
- `market_context_high->commodity_1h` score `0.8423` n `182` status `ready` deltaP `10.8443` edge `0.0316` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.3466` n `132` status `ready` deltaP `14.52` edge `0.0284` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2652` n `32` status `ready` deltaP `6.25` edge `0.0032` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2652` n `32` status `ready` deltaP `6.25` edge `0.0032` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.212` n `32` status `ready` deltaP `8.6078` edge `0.0073` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.212` n `32` status `ready` deltaP `8.6078` edge `0.0073` maxDD `-0.3343`
- `market_context_high->fx_1h` score `-0.0352` n `182` status `ready` deltaP `5.4945` edge `0.0012` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0605` n `182` status `ready` deltaP `6.8413` edge `0.0071` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5322` n `32` status `ready` deltaP `-1.9055` edge `0.0027` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5322` n `32` status `ready` deltaP `-1.9055` edge `0.0027` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.8081` n `32` status `ready` deltaP `-4.8091` edge `-0.0172` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
