# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T22:22:28.936300+00:00`
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

- `news_risk_high->unknown_24h` score `45.0568` n `51` status `ready` deltaP `10.0694` edge `3.6876` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8807` n `51` status `ready` deltaP `23.9538` edge `0.9183` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.5575` n `51` status `ready` deltaP `40.237` edge `0.8713` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.2996` n `51` status `ready` deltaP `48.9481` edge `0.1305` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.9978` n `51` status `ready` deltaP `27.6901` edge `0.2256` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5885` n `51` status `ready` deltaP `16.6343` edge `0.2186` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3358` n `51` status `ready` deltaP `39.3024` edge `0.0294` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `1.7112` n `107` status `ready` deltaP `5.3965` edge `0.1359` maxDD `-0.6752`
- `market_context_high->unknown_4h` score `1.6762` n `130` status `ready` deltaP `18.9915` edge `0.0539` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.3188` n `51` status `ready` deltaP `17.8936` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0005` n `51` status `ready` deltaP `18.4924` edge `0.0414` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9823` n `51` status `ready` deltaP `14.1589` edge `0.0272` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3261` n `51` status `ready` deltaP `9.5867` edge `-0.0059` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.2409` n `130` status `ready` deltaP `11.9348` edge `-0.0136` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2084` n `51` status `ready` deltaP `8.5241` edge `0.0052` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `0.1081` n `51` status `ready` deltaP `24.0809` edge `-0.1473` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `0.0456` n `130` status `ready` deltaP `11.2045` edge `-0.026` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1715` n `51` status `ready` deltaP `1.1448` edge `-0.0073` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1851` n `51` status `ready` deltaP `7.063` edge `-0.0094` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3835` n `130` status `ready` deltaP `3.4592` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
