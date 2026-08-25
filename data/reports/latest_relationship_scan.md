# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T08:22:25.520707+00:00`
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

- `news_risk_high->unknown_24h` score `43.7704` n `51` status `ready` deltaP `3.125` edge `3.6267` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9037` n `51` status `ready` deltaP `25.0209` edge `0.9131` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.4042` n `51` status `ready` deltaP `37.98` edge `0.7069` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.8241` n `51` status `ready` deltaP `47.0384` edge `0.1036` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3845` n `51` status `ready` deltaP `16.9337` edge `0.1996` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.1301` n `51` status `ready` deltaP `37.0158` edge `0.0275` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7297` n `51` status `ready` deltaP `24.184` edge `0.1433` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9095` n `133` status `ready` deltaP `19.4629` edge `0.0702` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1428` n `51` status `ready` deltaP `15.7978` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7425` n `51` status `ready` deltaP `16.696` edge `0.0203` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.5362` n `51` status `ready` deltaP `10.6528` edge `0.0134` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3345` n `51` status `ready` deltaP `9.5867` edge `-0.0052` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0316` n `51` status `ready` deltaP `5.6798` edge `0.0015` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0029` n `133` status `ready` deltaP `11.2725` edge `-0.0305` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.2104` n `51` status `ready` deltaP `0.3963` edge `-0.0073` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3177` n `51` status `ready` deltaP `5.6911` edge `-0.0113` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4903` n `133` status `ready` deltaP `1.6006` edge `-0.0003` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6336` n `51` status `ready` deltaP `21.6503` edge `-0.1929` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7055` n `133` status `ready` deltaP `5.9417` edge `-0.0347` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1137` n `133` status `ready` deltaP `-5.0234` edge `-0.0055` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
