# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T02:22:27.732042+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `44.4865` n `51` status `ready` deltaP `7.2917` edge `3.6586` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0077` n `51` status `ready` deltaP `24.716` edge `0.9238` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.9311` n `51` status `ready` deltaP `40.237` edge `0.8191` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.1796` n `51` status `ready` deltaP `48.9481` edge `0.1205` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.5468` n `51` status `ready` deltaP `26.9279` edge `0.1931` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5393` n `51` status `ready` deltaP `16.9337` edge `0.2125` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2908` n `51` status `ready` deltaP `38.8451` edge `0.0287` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8032` n `130` status `ready` deltaP `19.7537` edge `0.0594` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1919` n `51` status `ready` deltaP `16.3966` edge `0.007` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8999` n `51` status `ready` deltaP `18.193` edge `0.0305` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8907` n `51` status `ready` deltaP `13.854` edge `0.0216` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.271` n `51` status `ready` deltaP `8.9879` edge `-0.0065` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1492` n `51` status `ready` deltaP `7.6259` edge `0.0036` maxDD `-0.1583`
- `market_context_high->metal_4h` score `-0.0208` n `130` status `ready` deltaP `9.9531` edge `-0.0222` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.1363` n `134` status `ready` deltaP `10.7002` edge `-0.0378` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.194` n `51` status `ready` deltaP `0.8454` edge `-0.0082` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.3957` n `134` status `ready` deltaP `3.2711` edge `0.0007` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.432` n `51` status `ready` deltaP `21.6503` edge `-0.1761` maxDD `-0.0053`
- `news_risk_high->metal_4h` score `-0.4468` n `51` status `ready` deltaP `5.0813` edge `-0.018` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.9905` n `134` status `ready` deltaP `-4.3346` edge `-0.0136` maxDD `-0.8704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
