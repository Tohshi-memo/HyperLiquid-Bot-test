# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T03:11:52.370453+00:00`
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

- `news_risk_high->unknown_24h` score `44.4017` n `51` status `ready` deltaP `6.7708` edge `3.655` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9861` n `51` status `ready` deltaP `24.716` edge `0.922` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.8291` n `51` status `ready` deltaP `40.237` edge `0.8106` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.1604` n `51` status `ready` deltaP `48.9481` edge `0.1189` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.5166` n `51` status `ready` deltaP `26.7755` edge `0.1916` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.4793` n `51` status `ready` deltaP `16.6343` edge `0.2095` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2908` n `51` status `ready` deltaP `38.8451` edge `0.0287` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8229` n `129` status `ready` deltaP `19.7001` edge `0.0614` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.205` n `51` status `ready` deltaP `16.5463` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8875` n `51` status `ready` deltaP `18.0433` edge `0.0299` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8603` n `51` status `ready` deltaP `13.5491` edge `0.0211` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2722` n `51` status `ready` deltaP `8.9879` edge `-0.0064` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1313` n `51` status `ready` deltaP `7.3265` edge `0.0033` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.0149` n `129` status `ready` deltaP `10.1898` edge `-0.0208` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.0506` n `136` status `ready` deltaP `10.752` edge `-0.031` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.187` n `51` status `ready` deltaP `0.8454` edge `-0.0073` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3911` n `51` status `ready` deltaP `5.5387` edge `-0.0164` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3944` n `136` status `ready` deltaP `3.311` edge `0.0006` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.4584` n `51` status `ready` deltaP `21.6503` edge `-0.1783` maxDD `-0.0053`
- `market_context_high->index_1h` score `-0.9758` n `136` status `ready` deltaP `-2.9676` edge `-0.0034` maxDD `-1.3175`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
