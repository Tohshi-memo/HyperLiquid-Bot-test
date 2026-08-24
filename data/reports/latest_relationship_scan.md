# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T07:07:23.400186+00:00`
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

- `news_risk_high->unknown_24h` score `50.4171` n `51` status `ready` deltaP `17.0139` edge `4.088` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3215` n `51` status `ready` deltaP `40.237` edge `1.0183` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9267` n `51` status `ready` deltaP `23.3441` edge `0.9262` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7676` n `51` status `ready` deltaP `48.9481` edge `0.1695` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7352` n `51` status `ready` deltaP `26.9279` edge `0.2088` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6077` n `51` status `ready` deltaP `16.6343` edge `0.2202` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2382` n `51` status `ready` deltaP `38.0829` edge `0.0294` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.1928` n `145` status `ready` deltaP `21.8566` edge `0.0592` maxDD `-0.4407`
- `news_risk_high->metal_24h` score `1.755` n `51` status `ready` deltaP `34.4975` edge `-0.0795` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2566` n `51` status `ready` deltaP `17.1451` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9787` n `51` status `ready` deltaP `18.7918` edge `0.0366` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9459` n `51` status `ready` deltaP `13.854` edge `0.0262` maxDD `-0.1788`
- `news_risk_high->crypto_alt_24h` score `0.4186` n `51` status `ready` deltaP `24.1319` edge `-0.126` maxDD `0.0`
- `news_risk_high->index_1h` score `0.2761` n `51` status `ready` deltaP `9.8714` edge `0.0049` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1919` n `51` status `ready` deltaP `8.5388` edge `-0.0101` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `-0.1224` n `51` status `ready` deltaP `2.043` edge `-0.007` maxDD `-0.1184`
- `market_context_high->metal_4h` score `-0.1614` n `145` status `ready` deltaP `7.4454` edge `-0.0161` maxDD `-1.3378`
- `news_risk_high->metal_4h` score `-0.1705` n `51` status `ready` deltaP `7.2155` edge `-0.0092` maxDD `-0.249`
- `market_context_high->unknown_1h` score `-0.2388` n `149` status `ready` deltaP `9.4492` edge `-0.038` maxDD `-1.5916`
- `market_context_high->unknown_24h` score `-0.4398` n `92` status `ready` deltaP `5.0574` edge `-0.0197` maxDD `-1.0533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
