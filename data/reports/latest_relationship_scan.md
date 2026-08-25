# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T01:22:25.876436+00:00`
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

- `news_risk_high->unknown_24h` score `44.6069` n `51` status `ready` deltaP `7.9861` edge `3.664` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0669` n `51` status `ready` deltaP `25.0209` edge `0.9267` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.0703` n `51` status `ready` deltaP `40.237` edge `0.8307` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.2084` n `51` status `ready` deltaP `48.9481` edge `0.1229` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.6808` n `51` status `ready` deltaP `27.5377` edge `0.2002` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5117` n `51` status `ready` deltaP `16.784` edge `0.2112` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3176` n `51` status `ready` deltaP `39.1499` edge `0.0289` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8624` n `130` status `ready` deltaP `20.0586` edge `0.0623` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2422` n `51` status `ready` deltaP `16.9954` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9841` n `51` status `ready` deltaP `18.7918` edge `0.0373` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9331` n `51` status `ready` deltaP `14.1589` edge `0.0231` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3022` n `51` status `ready` deltaP `9.2873` edge `-0.0059` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1897` n `51` status `ready` deltaP `8.2247` edge `0.0048` maxDD `-0.1583`
- `market_context_high->metal_4h` score `-0.0026` n `130` status `ready` deltaP `10.1056` edge `-0.0217` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.0312` n `130` status `ready` deltaP `11.3542` edge `-0.0334` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1979` n `51` status `ready` deltaP `0.8454` edge `-0.0087` maxDD `-0.1184`
- `news_risk_high->metal_24h` score `-0.3418` n `51` status `ready` deltaP `21.9975` edge `-0.1709` maxDD `-0.0053`
- `news_risk_high->metal_4h` score `-0.4286` n `51` status `ready` deltaP `5.2338` edge `-0.0175` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4334` n `130` status `ready` deltaP `2.561` edge `0.0006` maxDD `-0.8587`
- `market_context_high->metal_1h` score `-0.5116` n `130` status `ready` deltaP `-2.865` edge `-0.0088` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
