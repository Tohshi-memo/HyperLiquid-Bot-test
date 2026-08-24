# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T20:52:28.151086+00:00`
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

- `news_risk_high->unknown_24h` score `45.2769` n `51` status `ready` deltaP `11.1111` edge `3.699` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8507` n `51` status `ready` deltaP `23.9538` edge `0.9158` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.7663` n `51` status `ready` deltaP `40.237` edge `0.8887` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.344` n `51` status `ready` deltaP `48.9481` edge `0.1342` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `4.001` n `51` status `ready` deltaP `27.3852` edge `0.2279` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6065` n `51` status `ready` deltaP `16.784` edge `0.2191` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3662` n `51` status `ready` deltaP `39.6073` edge `0.0299` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `3.2544` n `101` status `ready` deltaP `6.1606` edge `0.2594` maxDD `-0.6752`
- `market_context_high->unknown_4h` score `1.6462` n `130` status `ready` deltaP `18.9915` edge `0.0514` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2829` n `51` status `ready` deltaP `17.4445` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0091` n `51` status `ready` deltaP `18.6421` edge `0.0415` maxDD `-0.9128`
- `news_risk_high->index_4h` score `1.0005` n `51` status `ready` deltaP `14.3113` edge `0.0277` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3261` n `51` status `ready` deltaP `9.5867` edge `-0.0059` maxDD `-0.4666`
- `news_risk_high->metal_24h` score `0.303` n `51` status `ready` deltaP `25.1225` edge `-0.138` maxDD `-0.0053`
- `market_context_high->metal_4h` score `0.2761` n `130` status `ready` deltaP `12.2397` edge `-0.0127` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2162` n `51` status `ready` deltaP `8.6738` edge `0.0052` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0636` n `130` status `ready` deltaP `11.3542` edge `-0.0255` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1458` n `51` status `ready` deltaP `1.5939` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1499` n `51` status `ready` deltaP `7.3679` edge `-0.0085` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4069` n `130` status `ready` deltaP `3.0101` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
