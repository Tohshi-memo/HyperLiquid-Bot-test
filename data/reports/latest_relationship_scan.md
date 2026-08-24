# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T05:37:25.349453+00:00`
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

- `news_risk_high->unknown_24h` score `51.1095` n `51` status `ready` deltaP `17.0139` edge `4.1457` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3827` n `51` status `ready` deltaP `40.237` edge `1.0234` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9303` n `51` status `ready` deltaP `23.3441` edge `0.9265` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8048` n `51` status `ready` deltaP `48.9481` edge `0.1726` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.5541` n `51` status `ready` deltaP `26.0133` edge `0.1998` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5107` n `51` status `ready` deltaP `15.7361` edge `0.2181` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2382` n `51` status `ready` deltaP `38.0829` edge `0.0294` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.232` n `145` status `ready` deltaP `21.8566` edge `0.0583` maxDD `-0.4407`
- `news_risk_high->metal_24h` score `1.8923` n `51` status `ready` deltaP `35.5392` edge `-0.075` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2709` n `51` status `ready` deltaP `17.2948` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->crypto_alt_24h` score `1.1703` n `51` status `ready` deltaP `25.1736` edge `-0.0703` maxDD `0.0`
- `news_risk_high->equity_1h` score `0.921` n `51` status `ready` deltaP `18.0433` edge `0.0342` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8949` n `51` status `ready` deltaP `13.3967` edge `0.025` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2411` n `51` status `ready` deltaP `9.2726` edge `0.0044` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1895` n `51` status `ready` deltaP `8.5388` edge `-0.0103` maxDD `-0.4666`
- `news_risk_high->metal_4h` score `-0.0939` n `51` status `ready` deltaP `7.9777` edge `-0.0079` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.0944` n `51` status `ready` deltaP `2.4921` edge `-0.0064` maxDD `-0.1184`
- `market_context_high->fx_24h` score `-0.2449` n `92` status `ready` deltaP `7.4728` edge `0.0036` maxDD `-1.7854`
- `market_context_high->unknown_1h` score `-0.277` n `155` status `ready` deltaP `9.5122` edge `-0.0416` maxDD `-1.5916`
- `market_context_high->metal_4h` score `-0.3529` n `145` status `ready` deltaP `4.7593` edge `-0.0206` maxDD `-1.5093`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
