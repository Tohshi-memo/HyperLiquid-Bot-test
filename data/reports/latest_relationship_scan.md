# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T14:07:28.567562+00:00`
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

- `news_risk_high->unknown_24h` score `47.4627` n `51` status `ready` deltaP `15.7986` edge `3.8499` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7683` n `51` status `ready` deltaP `40.237` edge `0.9722` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9997` n `51` status `ready` deltaP `24.1063` edge `0.9272` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5624` n `51` status `ready` deltaP `48.9481` edge `0.1524` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.9748` n `51` status `ready` deltaP `27.5377` edge `0.2247` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6617` n `51` status `ready` deltaP `16.9337` edge `0.2227` maxDD `-0.7693`
- `market_context_high->unknown_24h` score `3.3608` n `77` status `ready` deltaP `6.7077` edge `0.2748` maxDD `-0.8228`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.728` n `132` status `ready` deltaP `19.2489` edge `0.0565` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2446` n `51` status `ready` deltaP `16.9954` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.1261` n `51` status `ready` deltaP `29.6364` edge `-0.0995` maxDD `-0.0053`
- `news_risk_high->index_4h` score `1.0699` n `51` status `ready` deltaP `15.0735` edge `0.0284` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0364` n `51` status `ready` deltaP `18.9415` edge `0.043` maxDD `-0.9128`
- `news_risk_high->index_1h` score `0.2753` n `51` status `ready` deltaP `9.7217` edge `0.0058` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1236` n `51` status `ready` deltaP `7.7903` edge `-0.0108` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1059` n `132` status `ready` deltaP `11.1557` edge `-0.0149` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0453` n `132` status `ready` deltaP `11.096` edge `-0.0253` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1271` n `51` status `ready` deltaP `2.043` edge `-0.0076` maxDD `-0.1184`
- `market_context_high->fx_24h` score `-0.1412` n `77` status `ready` deltaP `14.6848` edge `-0.004` maxDD `-3.2937`
- `news_risk_high->metal_4h` score `-0.1559` n `51` status `ready` deltaP `7.3679` edge `-0.009` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
