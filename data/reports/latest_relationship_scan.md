# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T04:22:26.935832+00:00`
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

- `news_risk_high->unknown_24h` score `44.2542` n `51` status `ready` deltaP `5.9028` edge `3.6485` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9405` n `51` status `ready` deltaP `24.716` edge `0.9182` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.5795` n `51` status `ready` deltaP `40.237` edge `0.7898` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.1184` n `51` status `ready` deltaP `48.9481` edge `0.1154` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3918` n `51` status `ready` deltaP `16.3349` edge `0.2042` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.3721` n `51` status `ready` deltaP `26.3182` edge `0.1826` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.2762` n `51` status `ready` deltaP `38.6926` edge `0.0285` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.9502` n `125` status `ready` deltaP `19.4768` edge `0.0735` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1943` n `51` status `ready` deltaP `16.3966` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8641` n `51` status `ready` deltaP `17.7439` edge `0.0289` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.7789` n `51` status `ready` deltaP `12.7869` edge `0.0194` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.313` n `51` status `ready` deltaP `9.437` edge `-0.006` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1134` n `51` status `ready` deltaP `7.0271` edge `0.003` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.0515` n `125` status `ready` deltaP `10.5293` edge `-0.0177` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0044` n `133` status `ready` deltaP `10.6737` edge `-0.0259` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1847` n `51` status `ready` deltaP `0.8454` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3185` n `51` status `ready` deltaP `5.996` edge `-0.0134` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4569` n `133` status `ready` deltaP `2.1994` edge `0.0` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.4932` n `51` status `ready` deltaP `21.6503` edge `-0.1812` maxDD `-0.0053`
- `market_context_high->index_1h` score `-0.9879` n `133` status `ready` deltaP `-3.6761` edge `-0.004` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
