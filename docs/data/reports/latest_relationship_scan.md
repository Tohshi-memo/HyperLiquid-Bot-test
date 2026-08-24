# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T21:07:33.619833+00:00`
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

- `news_risk_high->unknown_24h` score `45.2342` n `51` status `ready` deltaP `10.9375` edge `3.6966` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8483` n `51` status `ready` deltaP `23.9538` edge `0.9156` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.7339` n `51` status `ready` deltaP `40.237` edge `0.886` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.3368` n `51` status `ready` deltaP `48.9481` edge `0.1336` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `4.0228` n `51` status `ready` deltaP `27.5377` edge `0.2287` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5837` n `51` status `ready` deltaP `16.6343` edge `0.2182` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.365` n `51` status `ready` deltaP `39.6073` edge `0.0298` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `3.008` n `102` status `ready` deltaP `6.0355` edge `0.2397` maxDD `-0.6752`
- `market_context_high->unknown_4h` score `1.6438` n `130` status `ready` deltaP `18.9915` edge `0.0512` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2949` n `51` status `ready` deltaP `17.5942` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0139` n `51` status `ready` deltaP `14.4637` edge `0.0278` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0107` n `51` status `ready` deltaP `18.6421` edge `0.0417` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3273` n `51` status `ready` deltaP `9.5867` edge `-0.0058` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.2907` n `130` status `ready` deltaP `12.3922` edge `-0.0125` maxDD `-1.3378`
- `news_risk_high->metal_24h` score `0.2711` n `51` status `ready` deltaP `24.9489` edge `-0.1395` maxDD `-0.0053`
- `news_risk_high->index_1h` score `0.2162` n `51` status `ready` deltaP `8.6738` edge `0.0052` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0408` n `130` status `ready` deltaP `11.2045` edge `-0.0264` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.1353` n `51` status `ready` deltaP `7.5204` edge `-0.0083` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.1458` n `51` status `ready` deltaP `1.5939` edge `-0.007` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.3991` n `130` status `ready` deltaP `3.1598` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
