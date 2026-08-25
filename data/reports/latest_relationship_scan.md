# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T07:22:23.597231+00:00`
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

- `news_risk_high->unknown_24h` score `43.8896` n `51` status `ready` deltaP `3.8194` edge `3.632` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8905` n `51` status `ready` deltaP `25.0209` edge `0.912` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.6205` n `51` status `ready` deltaP `38.6745` edge `0.7203` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.9012` n `51` status `ready` deltaP `47.7328` edge `0.1054` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3533` n `51` status `ready` deltaP `16.6343` edge `0.199` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.1848` n `51` status `ready` deltaP `37.6255` edge `0.028` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.8093` n `51` status `ready` deltaP `24.4889` edge `0.1479` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.8963` n `133` status `ready` deltaP `19.4629` edge `0.0691` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1559` n `51` status `ready` deltaP `15.9475` edge `0.007` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7542` n `51` status `ready` deltaP `16.696` edge `0.0218` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.5678` n `51` status `ready` deltaP `10.9576` edge `0.014` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3753` n `51` status `ready` deltaP `10.0358` edge `-0.0048` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0402` n `51` status `ready` deltaP `5.8295` edge `0.0016` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0341` n `133` status `ready` deltaP `10.9731` edge `-0.0311` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.2127` n `51` status `ready` deltaP `0.3963` edge `-0.0076` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3457` n `51` status `ready` deltaP `5.3862` edge `-0.0116` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4818` n `133` status `ready` deltaP `1.7503` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6108` n `51` status `ready` deltaP `21.6503` edge `-0.191` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7335` n `133` status `ready` deltaP `5.6368` edge `-0.035` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1005` n `133` status `ready` deltaP `-4.8737` edge `-0.0054` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
