# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T22:11:09.089358+00:00`
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

- `news_risk_high->unknown_24h` score `45.0922` n `51` status `ready` deltaP `10.2431` edge `3.6894` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8735` n `51` status `ready` deltaP `23.9538` edge `0.9177` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.5947` n `51` status `ready` deltaP `40.237` edge `0.8744` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.308` n `51` status `ready` deltaP `48.9481` edge `0.1312` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `4.0134` n `51` status `ready` deltaP `27.6901` edge `0.2269` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5885` n `51` status `ready` deltaP `16.6343` edge `0.2186` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3492` n `51` status `ready` deltaP `39.4548` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `1.9604` n `106` status `ready` deltaP `5.5261` edge `0.1558` maxDD `-0.6752`
- `market_context_high->unknown_4h` score `1.669` n `130` status `ready` deltaP `18.9915` edge `0.0533` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.332` n `51` status `ready` deltaP `18.0433` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0013` n `51` status `ready` deltaP `18.4924` edge `0.0415` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9835` n `51` status `ready` deltaP `14.1589` edge `0.0273` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3273` n `51` status `ready` deltaP `9.5867` edge `-0.0058` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.2579` n `130` status `ready` deltaP `12.0873` edge `-0.0132` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2084` n `51` status `ready` deltaP `8.5241` edge `0.0052` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `0.1424` n `51` status `ready` deltaP `24.2545` edge `-0.1456` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `0.0456` n `130` status `ready` deltaP `11.2045` edge `-0.026` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.1681` n `51` status `ready` deltaP `7.2155` edge `-0.009` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.1715` n `51` status `ready` deltaP `1.1448` edge `-0.0073` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.375` n `130` status `ready` deltaP `3.6089` edge `0.0011` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
