# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T05:37:41.438248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `44.0984` n `51` status `ready` deltaP `5.0347` edge `3.6413` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8697` n `51` status `ready` deltaP `24.716` edge `0.9123` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.223` n `51` status `ready` deltaP `39.8897` edge `0.7624` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.0692` n `51` status `ready` deltaP `48.9481` edge `0.1113` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.2628` n `51` status `ready` deltaP `38.5402` edge `0.0284` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.2611` n `51` status `ready` deltaP `15.7361` edge `0.1973` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.1335` n `51` status `ready` deltaP `25.556` edge `0.1678` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9964` n `130` status `ready` deltaP `19.7537` edge `0.0755` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1955` n `51` status `ready` deltaP `16.3966` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8049` n `51` status `ready` deltaP `17.1451` edge `0.0253` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.688` n `51` status `ready` deltaP `12.0247` edge `0.0169` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3561` n `51` status `ready` deltaP `9.8861` edge `-0.0054` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0682` n `51` status `ready` deltaP `6.2786` edge `0.0022` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.1263` n `133` status `ready` deltaP `10.0749` edge `-0.0328` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1839` n `51` status `ready` deltaP `0.8454` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2897` n `51` status `ready` deltaP `5.996` edge `-0.011` maxDD `-0.249`
- `market_context_high->metal_4h` score `-0.395` n `130` status `ready` deltaP `7.7908` edge `-0.031` maxDD `-1.9754`
- `market_context_high->fx_1h` score `-0.4561` n `133` status `ready` deltaP `2.1994` edge `0.0001` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.5436` n `51` status `ready` deltaP `21.6503` edge `-0.1854` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.0574` n `133` status `ready` deltaP `-4.4246` edge `-0.0048` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
