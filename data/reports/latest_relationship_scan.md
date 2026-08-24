# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T14:37:32.011670+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `47.2717` n `51` status `ready` deltaP `15.4514` edge `3.8363` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7443` n `51` status `ready` deltaP `40.237` edge `0.9702` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9529` n `51` status `ready` deltaP `24.1063` edge `0.9233` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5516` n `51` status `ready` deltaP `48.9481` edge `0.1515` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.1224` n `78` status `ready` deltaP `7.7591` edge `0.326` maxDD `-0.7354`
- `news_risk_high->equity_4h` score `4.0508` n `51` status `ready` deltaP `27.8426` edge `0.229` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6449` n `51` status `ready` deltaP `16.9337` edge `0.2213` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.7118` n `131` status `ready` deltaP `19.1969` edge `0.0555` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2194` n `51` status `ready` deltaP `16.696` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0759` n `51` status `ready` deltaP `15.0735` edge `0.0289` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0699` n `51` status `ready` deltaP `19.0912` edge `0.0463` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `1.0695` n `51` status `ready` deltaP `29.2892` edge `-0.1019` maxDD `-0.0053`
- `news_risk_high->index_1h` score `0.2956` n `51` status `ready` deltaP `10.0211` edge `0.0064` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1272` n `51` status `ready` deltaP `7.7903` edge `-0.0105` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1236` n `131` status `ready` deltaP `11.5412` edge `-0.0152` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0346` n `131` status `ready` deltaP `10.9167` edge `-0.025` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1247` n `51` status `ready` deltaP `2.043` edge `-0.0073` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1753` n `51` status `ready` deltaP `7.2155` edge `-0.0096` maxDD `-0.249`
- `market_context_high->fx_24h` score `-0.2798` n `78` status `ready` deltaP `13.9022` edge `-0.0057` maxDD `-3.4953`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
