# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T14:22:31.490707+00:00`
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

- `news_risk_high->unknown_24h` score `47.3684` n `51` status `ready` deltaP `15.625` edge `3.8432` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7647` n `51` status `ready` deltaP `40.237` edge `0.9719` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9661` n `51` status `ready` deltaP `24.1063` edge `0.9244` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5576` n `51` status `ready` deltaP `48.9481` edge `0.152` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `4.0158` n `51` status `ready` deltaP `27.6901` edge `0.2271` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6317` n `51` status `ready` deltaP `16.784` edge `0.2212` maxDD `-0.7693`
- `market_context_high->unknown_24h` score `3.4378` n `78` status `ready` deltaP `6.6506` edge `0.2816` maxDD `-0.8228`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6944` n `132` status `ready` deltaP `19.2489` edge `0.0537` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2314` n `51` status `ready` deltaP `16.8457` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.1002` n `51` status `ready` deltaP `29.4628` edge `-0.1005` maxDD `-0.0053`
- `news_risk_high->index_4h` score `1.0735` n `51` status `ready` deltaP `15.0735` edge `0.0287` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0644` n `51` status `ready` deltaP `19.0912` edge `0.0456` maxDD `-0.9128`
- `news_risk_high->index_1h` score `0.2862` n `51` status `ready` deltaP `9.8714` edge `0.0062` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.126` n `51` status `ready` deltaP `7.7903` edge `-0.0106` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1044` n `132` status `ready` deltaP `11.1557` edge `-0.0151` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0154` n `132` status `ready` deltaP `10.9463` edge `-0.0268` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1255` n `51` status `ready` deltaP `2.043` edge `-0.0074` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1583` n `51` status `ready` deltaP `7.3679` edge `-0.0092` maxDD `-0.249`
- `market_context_high->fx_24h` score `-0.2308` n `78` status `ready` deltaP `13.9022` edge `-0.0049` maxDD `-3.39`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
