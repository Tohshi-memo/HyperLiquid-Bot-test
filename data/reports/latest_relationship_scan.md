# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T13:37:29.134677+00:00`
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

- `news_risk_high->unknown_24h` score `47.6513` n `51` status `ready` deltaP `16.1458` edge `3.8633` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7551` n `51` status `ready` deltaP `40.237` edge `0.9711` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0213` n `51` status `ready` deltaP `24.1063` edge `0.929` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5684` n `51` status `ready` deltaP `48.9481` edge `0.1529` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.8724` n `51` status `ready` deltaP `27.2328` edge `0.2182` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6713` n `51` status `ready` deltaP `16.9337` edge `0.2235` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `2.7582` n `77` status `ready` deltaP `5.7562` edge `0.2372` maxDD `-0.991`
- `market_context_high->unknown_4h` score `1.7177` n `133` status `ready` deltaP `19.3002` edge `0.0553` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2566` n `51` status `ready` deltaP `17.1451` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.1767` n `51` status `ready` deltaP `29.9836` edge `-0.0976` maxDD `-0.0053`
- `news_risk_high->index_4h` score `1.0493` n `51` status `ready` deltaP `14.9211` edge `0.0277` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.9763` n `51` status `ready` deltaP `18.6421` edge `0.0373` maxDD `-0.9128`
- `news_risk_high->index_1h` score `0.2535` n `51` status `ready` deltaP `9.4223` edge `0.005` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1212` n `51` status `ready` deltaP `7.7903` edge `-0.011` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1206` n `133` status `ready` deltaP `11.3779` edge `-0.0145` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.0127` n `133` status `ready` deltaP `10.5206` edge `-0.0263` maxDD `-1.5916`
- `market_context_high->fx_24h` score `-0.091` n `77` status `ready` deltaP `14.6848` edge `-0.0032` maxDD `-3.1759`
- `news_risk_high->metal_1h` score `-0.1466` n `51` status `ready` deltaP `1.7436` edge `-0.0081` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1535` n `51` status `ready` deltaP `7.3679` edge `-0.0088` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
