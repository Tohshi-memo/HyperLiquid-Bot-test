# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T02:37:26.100968+00:00`
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

- `news_risk_high->unknown_24h` score `44.4594` n `51` status `ready` deltaP `7.1181` edge `3.6575` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0017` n `51` status `ready` deltaP `24.716` edge `0.9233` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.8975` n `51` status `ready` deltaP `40.237` edge `0.8163` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.1724` n `51` status `ready` deltaP `48.9481` edge `0.1199` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.5405` n `51` status `ready` deltaP `16.9337` edge `0.2126` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.525` n `51` status `ready` deltaP `26.7755` edge `0.1923` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.2908` n `51` status `ready` deltaP `38.8451` edge `0.0287` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.7972` n `130` status `ready` deltaP `19.7537` edge `0.0589` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2038` n `51` status `ready` deltaP `16.5463` edge `0.007` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8859` n `51` status `ready` deltaP `18.0433` edge `0.0297` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8761` n `51` status `ready` deltaP `13.7015` edge `0.0214` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2579` n `51` status `ready` deltaP `8.8382` edge `-0.0066` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1406` n `51` status `ready` deltaP `7.4762` edge `0.0035` maxDD `-0.1583`
- `market_context_high->metal_4h` score `-0.0038` n `130` status `ready` deltaP `10.1056` edge `-0.0218` maxDD `-1.3378`
- `news_risk_high->metal_1h` score `-0.1909` n `51` status `ready` deltaP `0.8454` edge `-0.0078` maxDD `-0.1184`
- `market_context_high->unknown_1h` score `-0.203` n `135` status `ready` deltaP `10.1364` edge `-0.0396` maxDD `-1.5916`
- `market_context_high->fx_1h` score `-0.41` n `135` status `ready` deltaP `2.9951` edge `0.0007` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.4298` n `51` status `ready` deltaP `5.2338` edge `-0.0176` maxDD `-0.249`
- `news_risk_high->metal_24h` score `-0.4404` n `51` status `ready` deltaP `21.6503` edge `-0.1768` maxDD `-0.0053`
- `market_context_high->index_1h` score `-0.998` n `135` status `ready` deltaP `-3.1992` edge `-0.0037` maxDD `-1.3175`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
