# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T04:07:57.902270+00:00`
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

- `news_risk_high->unknown_24h` score `44.2837` n `51` status `ready` deltaP `6.0764` edge `3.6498` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9501` n `51` status `ready` deltaP `24.716` edge `0.919` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.6347` n `51` status `ready` deltaP `40.237` edge `0.7944` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.128` n `51` status `ready` deltaP `48.9481` edge `0.1162` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.4226` n `51` status `ready` deltaP `26.4706` edge `0.1858` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.4194` n `51` status `ready` deltaP `16.4846` edge `0.2055` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2762` n `51` status `ready` deltaP `38.6926` edge `0.0285` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.9598` n `125` status `ready` deltaP `19.4768` edge `0.0743` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2062` n `51` status `ready` deltaP `16.5463` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8766` n `51` status `ready` deltaP `17.8936` edge `0.0295` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.7983` n `51` status `ready` deltaP `12.9394` edge `0.02` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2998` n `51` status `ready` deltaP `9.2873` edge `-0.0061` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1219` n `51` status `ready` deltaP `7.1768` edge `0.0031` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.0476` n `125` status `ready` deltaP `10.5293` edge `-0.0182` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0319` n `133` status `ready` deltaP `10.8234` edge `-0.0246` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1847` n `51` status `ready` deltaP `0.8454` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3245` n `51` status `ready` deltaP `5.996` edge `-0.0139` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4491` n `133` status `ready` deltaP `2.3491` edge `0.0` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.486` n `51` status `ready` deltaP `21.6503` edge `-0.1806` maxDD `-0.0053`
- `market_context_high->index_1h` score `-0.9747` n `133` status `ready` deltaP `-3.5264` edge `-0.0039` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
