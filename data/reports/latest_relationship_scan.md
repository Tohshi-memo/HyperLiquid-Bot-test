# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T18:37:33.653054+00:00`
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

- `news_risk_high->unknown_24h` score `45.8339` n `51` status `ready` deltaP `12.6736` edge `3.735` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0687` n `51` status `ready` deltaP `40.237` edge `0.9139` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8461` n `51` status `ready` deltaP `24.1063` edge `0.9144` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.4064` n `51` status `ready` deltaP `48.9481` edge `0.1394` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.6654` n `92` status `ready` deltaP `7.2388` edge `0.3698` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `3.9528` n `51` status `ready` deltaP `27.2328` edge `0.2249` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5802` n `51` status `ready` deltaP `16.4846` edge `0.2189` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3662` n `51` status `ready` deltaP `39.6073` edge `0.0299` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6416` n `130` status `ready` deltaP `19.144` edge `0.05` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2949` n `51` status `ready` deltaP `17.5942` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0139` n `51` status `ready` deltaP `14.4637` edge `0.0278` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.9919` n `51` status `ready` deltaP `18.4924` edge `0.0403` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.5792` n `51` status `ready` deltaP `26.685` edge `-0.1254` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.2794` n `51` status `ready` deltaP `9.1376` edge `-0.0068` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2146` n `51` status `ready` deltaP `8.6738` edge `0.005` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1485` n `130` status `ready` deltaP `11.0202` edge `-0.0152` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0372` n `130` status `ready` deltaP `11.0548` edge `-0.0257` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1029` n `51` status `ready` deltaP `2.3424` edge `-0.0065` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2775` n `51` status `ready` deltaP `6.1484` edge `-0.011` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3991` n `130` status `ready` deltaP `3.1598` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
