# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T03:52:23.387778+00:00`
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

- `news_risk_high->unknown_24h` score `44.3132` n `51` status `ready` deltaP `6.25` edge `3.6511` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9561` n `51` status `ready` deltaP `24.716` edge `0.9195` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.6923` n `51` status `ready` deltaP `40.237` edge `0.7992` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.1376` n `51` status `ready` deltaP `48.9481` edge `0.117` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.4684` n `51` status `ready` deltaP `26.623` edge `0.1886` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.4302` n `51` status `ready` deltaP `16.4846` edge `0.2064` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2896` n `51` status `ready` deltaP `38.8451` edge `0.0286` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.9224` n `126` status `ready` deltaP `19.5339` edge `0.0708` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2062` n `51` status `ready` deltaP `16.5463` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.889` n `51` status `ready` deltaP `18.0433` edge `0.0301` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8165` n `51` status `ready` deltaP `13.0918` edge `0.0205` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2998` n `51` status `ready` deltaP `9.2873` edge `-0.0061` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1305` n `51` status `ready` deltaP `7.3265` edge `0.0032` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0363` n `134` status `ready` deltaP `10.9974` edge `-0.0254` maxDD `-1.5916`
- `market_context_high->metal_4h` score `0.0097` n `126` status `ready` deltaP `9.9642` edge `-0.0193` maxDD `-1.3378`
- `news_risk_high->metal_1h` score `-0.1855` n `51` status `ready` deltaP `0.8454` edge `-0.0071` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3317` n `51` status `ready` deltaP `5.996` edge `-0.0145` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4314` n `134` status `ready` deltaP `2.6745` edge `0.0001` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.4776` n `51` status `ready` deltaP `21.6503` edge `-0.1799` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.0421` n `134` status `ready` deltaP `-3.7358` edge `-0.0038` maxDD `-1.3175`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
