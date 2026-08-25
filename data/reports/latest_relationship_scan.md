# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T08:07:28.194726+00:00`
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

- `news_risk_high->unknown_24h` score `43.8035` n `51` status `ready` deltaP `3.2986` edge `3.6283` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9001` n `51` status `ready` deltaP `25.0209` edge `0.9128` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.4505` n `51` status `ready` deltaP `38.1536` edge `0.7096` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.8416` n `51` status `ready` deltaP `47.212` edge `0.1039` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3701` n `51` status `ready` deltaP `16.784` edge `0.1994` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.1447` n `51` status `ready` deltaP `37.1682` edge `0.0277` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7369` n `51` status `ready` deltaP `24.184` edge `0.1439` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9059` n `133` status `ready` deltaP `19.4629` edge `0.0699` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1559` n `51` status `ready` deltaP `15.9475` edge `0.007` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7441` n `51` status `ready` deltaP `16.696` edge `0.0205` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.5374` n `51` status `ready` deltaP `10.6528` edge `0.0135` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3477` n `51` status `ready` deltaP `9.7364` edge `-0.0051` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0394` n `51` status `ready` deltaP `5.8295` edge `0.0015` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0173` n `133` status `ready` deltaP `11.1228` edge `-0.0307` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.2119` n `51` status `ready` deltaP `0.3963` edge `-0.0075` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3323` n `51` status `ready` deltaP `5.5387` edge `-0.0115` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4818` n `133` status `ready` deltaP `1.7503` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6288` n `51` status `ready` deltaP `21.6503` edge `-0.1925` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7201` n `133` status `ready` deltaP `5.7893` edge `-0.0349` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1017` n `133` status `ready` deltaP `-4.8737` edge `-0.0055` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
