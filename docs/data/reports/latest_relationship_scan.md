# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T13:37:25.739343+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3868`

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

- `market_context_high->unknown_24h` score `1752.3716` n `88` status `ready` deltaP `3.4602` edge `146.0079` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.913` n `50` status `ready` deltaP `66.5467` edge `4.5364` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.2697` n `50` status `ready` deltaP `29.6263` edge `2.1309` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.4881` n `88` status `ready` deltaP `44.3536` edge `1.8888` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.2322` n `50` status `ready` deltaP `43.6402` edge `1.0081` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `13.6124` n `88` status `ready` deltaP `28.7905` edge `1.7656` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.1563` n `50` status `ready` deltaP `57.8962` edge `0.4074` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.0111` n `50` status `ready` deltaP `52.2491` edge `0.4026` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.2058` n `50` status `ready` deltaP `15.9723` edge `1.3961` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.9418` n `50` status `ready` deltaP `43.9268` edge `0.1566` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.459` n `50` status `ready` deltaP `22.5449` edge `0.2843` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.3536` n `50` status `ready` deltaP `26.0793` edge `0.3325` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `3.6726` n `50` status `ready` deltaP `19.7744` edge `0.3118` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.6524` n `50` status `ready` deltaP `33.6768` edge `0.1052` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.092` n `50` status `ready` deltaP `28.9146` edge `0.0999` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1682` n `50` status `ready` deltaP `24.3952` edge `0.0435` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.47` n `50` status `ready` deltaP `18.8443` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9336` n `50` status `ready` deltaP `20.0069` edge `0.2036` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7227` n `50` status `ready` deltaP `16.3952` edge `0.0813` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6448` n `50` status `ready` deltaP `17.9461` edge `0.0682` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
