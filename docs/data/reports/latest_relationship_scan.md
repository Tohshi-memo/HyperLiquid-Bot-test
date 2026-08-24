# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T06:37:24.023099+00:00`
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

- `news_risk_high->unknown_24h` score `50.6439` n `51` status `ready` deltaP `17.0139` edge `4.1069` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3419` n `51` status `ready` deltaP `40.237` edge `1.02` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9267` n `51` status `ready` deltaP `23.3441` edge `0.9262` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7808` n `51` status `ready` deltaP `48.9481` edge `0.1706` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.6844` n `51` status `ready` deltaP `26.623` edge `0.2066` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5826` n `51` status `ready` deltaP `16.3349` edge `0.2201` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2516` n `51` status `ready` deltaP `38.2353` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.2952` n `145` status `ready` deltaP `21.8566` edge `0.0594` maxDD `-0.4407`
- `news_risk_high->metal_24h` score `1.7996` n `51` status `ready` deltaP `34.8448` edge `-0.0781` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2566` n `51` status `ready` deltaP `17.1451` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9693` n `51` status `ready` deltaP `18.6421` edge `0.0364` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9423` n `51` status `ready` deltaP `13.854` edge `0.0259` maxDD `-0.1788`
- `news_risk_high->crypto_alt_24h` score `0.6491` n `51` status `ready` deltaP `24.4792` edge `-0.1091` maxDD `0.0`
- `news_risk_high->index_1h` score `0.2761` n `51` status `ready` deltaP `9.8714` edge `0.0049` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1775` n `51` status `ready` deltaP `8.3891` edge `-0.0103` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `-0.1224` n `51` status `ready` deltaP `2.043` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1401` n `51` status `ready` deltaP `7.5204` edge `-0.0087` maxDD `-0.249`
- `market_context_high->metal_4h` score `-0.232` n `145` status `ready` deltaP `6.3709` edge `-0.018` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.2688` n `151` status `ready` deltaP `9.4787` edge `-0.0407` maxDD `-1.5916`
- `market_context_high->metal_1h` score `-0.4032` n `151` status `ready` deltaP `-1.2293` edge `-0.0058` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
