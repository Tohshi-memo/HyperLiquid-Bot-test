# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T00:37:27.684140+00:00`
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

- `news_risk_high->unknown_24h` score `49.0301` n `50` status `ready` deltaP `11.5717` edge `4.0087` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.7075` n `50` status `ready` deltaP `36.5872` edge `0.9425` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.3079` n `50` status `ready` deltaP `25.7073` edge `0.8642` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `6.7709` n `50` status `ready` deltaP `30.6321` edge `0.4538` maxDD `-4.8351`
- `news_risk_high->fx_4h` score `3.7096` n `50` status `ready` deltaP `43.5244` edge `0.028` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.701` n `50` status `ready` deltaP `37.3955` edge `0.0743` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.1626` n `137` status `ready` deltaP `24.408` edge `0.1415` maxDD `-0.5871`
- `news_risk_high->unknown_1h` score `2.7062` n `50` status `ready` deltaP `15.479` edge `0.1579` maxDD `-0.8463`
- `news_risk_high->metal_24h` score `2.6705` n `50` status `ready` deltaP `35.9965` edge `-0.0132` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.3994` n `50` status `ready` deltaP `19.006` edge `0.0069` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3396` n `137` status `ready` deltaP `12.8513` edge `0.0709` maxDD `-1.5954`
- `news_risk_high->equity_1h` score `1.2992` n `50` status `ready` deltaP `17.4132` edge `0.0201` maxDD `-0.2338`
- `news_risk_high->equity_4h` score `1.2058` n `50` status `ready` deltaP `19.2927` edge `0.0486` maxDD `-2.1389`
- `market_context_high->unknown_24h` score `0.5456` n `133` status `ready` deltaP `5.5567` edge `0.0815` maxDD `-3.1794`
- `news_risk_high->commodity_1h` score `0.5261` n `50` status `ready` deltaP `14.4491` edge `0.0024` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1123` n `50` status `ready` deltaP `7.0599` edge `0.0013` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0712` n `50` status `ready` deltaP `6.4756` edge `0.0025` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0438` n `50` status `ready` deltaP `4.503` edge `-0.0018` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1739` n `50` status `ready` deltaP `7.1585` edge `-0.0091` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3694` n `137` status `ready` deltaP `3.9403` edge `-0.0004` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
