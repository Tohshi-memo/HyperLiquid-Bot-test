# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T04:07:38.905358+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4410`

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

- `market_context_high->unknown_24h` score `2118.4367` n `59` status `ready` deltaP `3.4483` edge `176.5134` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.258` n `50` status `ready` deltaP `60.069` edge `4.275` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.1576` n `50` status `ready` deltaP `35.931` edge `2.3309` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.5414` n `59` status `ready` deltaP `13.007` edge `1.5041` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.427` n `50` status `ready` deltaP `43.9451` edge `1.0223` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.3724` n `59` status `ready` deltaP `37.253` edge `1.6649` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.2687` n `50` status `ready` deltaP `21.4138` edge `1.4961` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.2901` n `50` status `ready` deltaP `51.4483` edge `0.3782` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.437` n `50` status `ready` deltaP `45.8621` edge `0.314` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2411` n `50` status `ready` deltaP `46.2134` edge `0.1663` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5588` n `50` status `ready` deltaP `26.9939` edge `0.3435` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.4998` n `50` status `ready` deltaP `22.5449` edge `0.2877` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.3065` n `50` status `ready` deltaP `21.9085` edge `0.3504` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1349` n `50` status `ready` deltaP `37.4878` edge `0.12` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1078` n `50` status `ready` deltaP `29.0671` edge `0.1002` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2054` n `50` status `ready` deltaP `24.6946` edge `0.0446` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5179` n `50` status `ready` deltaP `19.4431` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8082` n `50` status `ready` deltaP `18.3448` edge `0.1986` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.743` n `50` status `ready` deltaP `16.5449` edge `0.0829` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7282` n `50` status `ready` deltaP `18.5449` edge `0.0749` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
