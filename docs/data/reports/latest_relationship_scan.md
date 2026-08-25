# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T05:52:25.221299+00:00`
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

- `news_risk_high->unknown_24h` score `44.0665` n `51` status `ready` deltaP `4.8611` edge `3.6398` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8395` n `51` status `ready` deltaP `24.5636` edge `0.9108` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.1371` n `51` status `ready` deltaP `39.7161` edge `0.7564` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.0446` n `51` status `ready` deltaP `48.7745` edge `0.1104` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2611` n `51` status `ready` deltaP `15.7361` edge `0.1973` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2506` n `51` status `ready` deltaP `38.3877` edge `0.0284` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `3.0841` n `51` status `ready` deltaP `25.4035` edge `0.1647` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0088` n `131` status `ready` deltaP `19.6542` edge `0.0772` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1943` n `51` status `ready` deltaP `16.3966` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8018` n `51` status `ready` deltaP `17.1451` edge `0.0249` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.671` n `51` status `ready` deltaP `11.8723` edge `0.0165` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3729` n `51` status `ready` deltaP `10.0358` edge `-0.005` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0674` n `51` status `ready` deltaP `6.2786` edge `0.0021` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.1263` n `133` status `ready` deltaP `10.0749` edge `-0.0328` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1839` n `51` status `ready` deltaP `0.8454` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2849` n `51` status `ready` deltaP `5.996` edge `-0.0106` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4569` n `133` status `ready` deltaP `2.1994` edge `0.0` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.5089` n `131` status `ready` deltaP `7.2682` edge `-0.033` maxDD `-2.2954`
- `news_risk_high->metal_24h` score `-0.5532` n `51` status `ready` deltaP `21.6503` edge `-0.1862` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.0586` n `133` status `ready` deltaP `-4.4246` edge `-0.0049` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
