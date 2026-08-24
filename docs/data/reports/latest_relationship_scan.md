# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T23:07:26.079419+00:00`
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

- `news_risk_high->unknown_24h` score `44.9395` n `51` status `ready` deltaP `9.5486` edge `3.6813` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9217` n `51` status `ready` deltaP `24.1063` edge `0.9207` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.4423` n `51` status `ready` deltaP `40.237` edge `0.8617` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.2744` n `51` status `ready` deltaP `48.9481` edge `0.1284` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.9342` n `51` status `ready` deltaP `27.6901` edge `0.2203` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5658` n `51` status `ready` deltaP `16.4846` edge `0.2177` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3322` n `51` status `ready` deltaP `39.3024` edge `0.0291` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.7172` n `130` status `ready` deltaP `19.144` edge `0.0563` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2937` n `51` status `ready` deltaP `17.5942` edge `0.0075` maxDD `-0.0257`
- `market_context_high->unknown_24h` score `1.0402` n `110` status `ready` deltaP `5.0031` edge `0.0826` maxDD `-0.6752`
- `news_risk_high->equity_1h` score `1.0099` n `51` status `ready` deltaP `18.6421` edge `0.0416` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9703` n `51` status `ready` deltaP `14.1589` edge `0.0262` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.313` n `51` status `ready` deltaP `9.437` edge `-0.006` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.192` n `51` status `ready` deltaP `8.2247` edge `0.0051` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1851` n `130` status `ready` deltaP `11.4775` edge `-0.0152` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0228` n `130` status `ready` deltaP `11.0548` edge `-0.0269` maxDD `-1.5916`
- `news_risk_high->metal_24h` score `0.0016` n `51` status `ready` deltaP `23.56` edge `-0.1527` maxDD `-0.0053`
- `news_risk_high->metal_1h` score `-0.1722` n `51` status `ready` deltaP `1.1448` edge `-0.0074` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2409` n `51` status `ready` deltaP `6.6057` edge `-0.011` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3999` n `130` status `ready` deltaP `3.1598` edge `0.0009` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
