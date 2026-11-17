# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T05:37:30.662584+00:00`
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

- `market_context_high->unknown_24h` score `2178.4163` n `61` status `ready` deltaP `3.4483` edge `181.5117` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.7751` n `50` status `ready` deltaP `61.1034` edge `4.3112` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.8456` n `50` status `ready` deltaP `34.8966` edge `2.2978` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.0392` n `61` status `ready` deltaP `14.7739` edge `1.5338` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.364` n `50` status `ready` deltaP `43.4878` edge `1.0201` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.5292` n `61` status `ready` deltaP `37.5523` edge `1.683` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.2048` n `50` status `ready` deltaP `21.069` edge `1.4902` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.4244` n `50` status `ready` deltaP `52.4828` edge `0.3825` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.7021` n `50` status `ready` deltaP `46.8966` edge `0.3292` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1477` n `50` status `ready` deltaP `45.4512` edge `0.1636` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5285` n `50` status `ready` deltaP `22.8443` edge `0.2881` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5192` n `50` status `ready` deltaP `26.9939` edge `0.3402` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.2357` n `50` status `ready` deltaP `21.9085` edge `0.3445` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1457` n `50` status `ready` deltaP `37.4878` edge `0.1209` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1626` n `50` status `ready` deltaP `29.6768` edge `0.1007` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1778` n `50` status `ready` deltaP `24.3952` edge `0.0443` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5299` n `50` status `ready` deltaP `19.5928` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.7813` n `50` status `ready` deltaP `18.1724` edge `0.1963` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7446` n `50` status `ready` deltaP `16.3952` edge `0.0841` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7017` n `50` status `ready` deltaP `18.2455` edge `0.0735` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
