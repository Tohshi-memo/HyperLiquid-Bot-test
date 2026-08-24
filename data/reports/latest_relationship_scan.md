# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T05:06:44.015393+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `51.3507` n `51` status `ready` deltaP `17.0139` edge `4.1658` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3899` n `51` status `ready` deltaP `40.237` edge `1.024` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9365` n `51` status `ready` deltaP `23.4965` edge `0.926` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8132` n `51` status `ready` deltaP `48.9481` edge `0.1733` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.5143` n `51` status `ready` deltaP `15.7361` edge `0.2184` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.4661` n `51` status `ready` deltaP `25.7084` edge `0.1945` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.237` n `51` status `ready` deltaP `38.0829` edge `0.0293` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.2588` n `145` status `ready` deltaP `21.3194` edge `0.0598` maxDD `-0.0956`
- `news_risk_high->metal_24h` score `1.9321` n `51` status `ready` deltaP `35.8864` edge `-0.074` maxDD `-0.0053`
- `news_risk_high->crypto_alt_24h` score `1.4321` n `51` status `ready` deltaP `25.5208` edge `-0.0508` maxDD `0.0`
- `news_risk_high->fx_1h` score `1.2566` n `51` status `ready` deltaP `17.1451` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8961` n `51` status `ready` deltaP `17.7439` edge `0.033` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8633` n `51` status `ready` deltaP `13.0918` edge `0.0244` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2317` n `51` status `ready` deltaP `9.1229` edge `0.0042` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2051` n `51` status `ready` deltaP `8.6885` edge `-0.01` maxDD `-0.4666`
- `news_risk_high->metal_4h` score `-0.0671` n `51` status `ready` deltaP `8.2826` edge `-0.0077` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.1115` n `51` status `ready` deltaP `2.1927` edge `-0.0066` maxDD `-0.1184`
- `market_context_high->fx_24h` score `-0.1363` n `92` status `ready` deltaP `8.3862` edge `0.0075` maxDD `-1.4708`
- `market_context_high->unknown_1h` score `-0.2754` n `157` status `ready` deltaP `9.8163` edge `-0.0435` maxDD `-1.5916`
- `market_context_high->metal_1h` score `-0.3877` n `157` status `ready` deltaP `-1.067` edge `-0.0049` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
