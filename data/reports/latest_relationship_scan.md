# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T05:52:31.427493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4440`

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

- `market_context_high->unknown_24h` score `2228.2079` n `62` status `ready` deltaP `3.4483` edge `185.661` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.8741` n `50` status `ready` deltaP `61.2759` edge `4.3183` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.7914` n `50` status `ready` deltaP `34.7241` edge `2.292` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.3332` n `62` status `ready` deltaP `15.7787` edge `1.5516` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.393` n `50` status `ready` deltaP `43.6402` edge `1.0215` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.7217` n `62` status `ready` deltaP `38.0144` edge `1.7046` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.1915` n `50` status `ready` deltaP `21.069` edge `1.4885` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.449` n `50` status `ready` deltaP `52.6552` edge `0.3834` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.7471` n `50` status `ready` deltaP `47.069` edge `0.3318` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1319` n `50` status `ready` deltaP `45.2988` edge `0.1633` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5549` n `50` status `ready` deltaP `22.994` edge `0.2893` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5108` n `50` status `ready` deltaP `26.9939` edge `0.3395` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.2298` n `50` status `ready` deltaP `21.9085` edge `0.344` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1445` n `50` status `ready` deltaP `37.4878` edge `0.1208` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1784` n `50` status `ready` deltaP `29.8293` edge `0.101` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1778` n `50` status `ready` deltaP `24.3952` edge `0.0443` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5443` n `50` status `ready` deltaP `19.7425` edge `0.0272` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.7684` n `50` status `ready` deltaP `18.0` edge `0.1958` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7563` n `50` status `ready` deltaP `16.5449` edge `0.0846` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7149` n `50` status `ready` deltaP `18.3952` edge `0.0742` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
