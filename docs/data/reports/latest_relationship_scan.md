# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T13:52:26.768226+00:00`
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

- `news_risk_high->unknown_24h` score `47.5582` n `51` status `ready` deltaP `15.9722` edge `3.8567` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7719` n `51` status `ready` deltaP `40.237` edge `0.9725` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0105` n `51` status `ready` deltaP `24.1063` edge `0.9281` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5672` n `51` status `ready` deltaP `48.9481` edge `0.1528` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.9266` n `51` status `ready` deltaP `27.3852` edge `0.2217` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6617` n `51` status `ready` deltaP `16.9337` edge `0.2227` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `2.6652` n `77` status `ready` deltaP `5.5826` edge `0.2306` maxDD `-0.991`
- `market_context_high->unknown_4h` score `1.7069` n `133` status `ready` deltaP `19.3002` edge `0.0544` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2446` n `51` status `ready` deltaP `16.9954` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.1544` n `51` status `ready` deltaP `29.81` edge `-0.0983` maxDD `-0.0053`
- `news_risk_high->index_4h` score `1.0663` n `51` status `ready` deltaP `15.0735` edge `0.0281` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0083` n `51` status `ready` deltaP `18.7918` edge `0.0404` maxDD `-0.9128`
- `news_risk_high->index_1h` score `0.2644` n `51` status `ready` deltaP `9.572` edge `0.0054` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1224` n `51` status `ready` deltaP `7.7903` edge `-0.0109` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1206` n `133` status `ready` deltaP `11.3779` edge `-0.0145` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.0223` n `133` status `ready` deltaP `10.5206` edge `-0.0271` maxDD `-1.5916`
- `market_context_high->fx_24h` score `-0.0902` n `77` status `ready` deltaP `14.6848` edge `-0.0031` maxDD `-3.1759`
- `news_risk_high->metal_1h` score `-0.1364` n `51` status `ready` deltaP `1.8933` edge `-0.0078` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1535` n `51` status `ready` deltaP `7.3679` edge `-0.0088` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
