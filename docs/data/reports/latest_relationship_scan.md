# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T20:38:39.094192+00:00`
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

- `news_risk_high->unknown_24h` score `45.328` n `51` status `ready` deltaP `11.2847` edge `3.7021` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8423` n `51` status `ready` deltaP `23.9538` edge `0.9151` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.7963` n `51` status `ready` deltaP `40.237` edge `0.8912` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.35` n `51` status `ready` deltaP `48.9481` edge `0.1347` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.9768` n `51` status `ready` deltaP `27.2328` edge `0.2269` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6065` n `51` status `ready` deltaP `16.784` edge `0.2191` maxDD `-0.7693`
- `market_context_high->unknown_24h` score `3.4551` n `100` status `ready` deltaP `6.2847` edge `0.2753` maxDD `-0.6752`
- `news_risk_high->fx_4h` score `3.3662` n `51` status `ready` deltaP `39.6073` edge `0.0299` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6378` n `130` status `ready` deltaP `18.9915` edge `0.0507` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2829` n `51` status `ready` deltaP `17.4445` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0083` n `51` status `ready` deltaP `18.6421` edge `0.0414` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9871` n `51` status `ready` deltaP `14.1589` edge `0.0276` maxDD `-0.1788`
- `news_risk_high->metal_24h` score `0.3349` n `51` status `ready` deltaP `25.2961` edge `-0.1365` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.3249` n `51` status `ready` deltaP `9.5867` edge `-0.006` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.2615` n `130` status `ready` deltaP `12.0873` edge `-0.0129` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2076` n `51` status `ready` deltaP `8.5241` edge `0.0051` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0636` n `130` status `ready` deltaP `11.3542` edge `-0.0255` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1535` n `51` status `ready` deltaP `1.4442` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1645` n `51` status `ready` deltaP `7.2155` edge `-0.0087` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4069` n `130` status `ready` deltaP `3.0101` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
