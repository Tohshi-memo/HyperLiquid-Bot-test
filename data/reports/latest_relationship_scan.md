# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T06:52:24.076296+00:00`
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

- `news_risk_high->unknown_24h` score `43.9485` n `51` status `ready` deltaP `4.1667` edge `3.6346` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8589` n `51` status `ready` deltaP `24.716` edge `0.9114` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.7743` n `51` status `ready` deltaP `39.0217` edge `0.7308` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.947` n `51` status `ready` deltaP `48.0801` edge `0.1069` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3234` n `51` status `ready` deltaP `16.3349` edge `0.1985` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2104` n `51` status `ready` deltaP `37.9304` edge `0.0281` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.8925` n `51` status `ready` deltaP `24.7938` edge `0.1528` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.8647` n `133` status `ready` deltaP `19.158` edge `0.0685` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1571` n `51` status `ready` deltaP `15.9475` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7807` n `51` status `ready` deltaP `16.8457` edge `0.0242` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.6018` n `51` status `ready` deltaP `11.2625` edge `0.0148` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3741` n `51` status `ready` deltaP `10.0358` edge `-0.0049` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0511` n `51` status `ready` deltaP `5.9792` edge `0.002` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.064` n `133` status `ready` deltaP `10.6737` edge `-0.0316` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.2096` n `51` status `ready` deltaP `0.3963` edge `-0.0072` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3153` n `51` status `ready` deltaP `5.6911` edge `-0.0111` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.481` n `133` status `ready` deltaP `1.7503` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.5916` n `51` status `ready` deltaP `21.6503` edge `-0.1894` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7031` n `133` status `ready` deltaP `5.9417` edge `-0.0345` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.0837` n `133` status `ready` deltaP `-4.724` edge `-0.005` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
