# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T13:07:29.721382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4108`

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

- `market_context_high->unknown_24h` score `1782.8703` n `87` status `ready` deltaP `3.4542` edge `148.5495` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.7287` n `50` status `ready` deltaP `66.2383` edge `4.5231` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.3257` n `50` status `ready` deltaP `29.848` edge `2.1366` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.3418` n `50` status `ready` deltaP `43.9451` edge `1.0152` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.3219` n `87` status `ready` deltaP `44.2618` edge `1.8681` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.4046` n `87` status `ready` deltaP `28.5152` edge `1.7408` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.1172` n `50` status `ready` deltaP `57.6028` edge `0.4061` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.9529` n `50` status `ready` deltaP `51.9862` edge `0.3995` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.2422` n `50` status `ready` deltaP `16.1934` edge `1.3993` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.9466` n `50` status `ready` deltaP `43.9268` edge `0.157` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.4542` n `50` status `ready` deltaP `22.5449` edge `0.2839` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4512` n `50` status `ready` deltaP `26.3841` edge `0.3386` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `3.8182` n `50` status `ready` deltaP `20.0793` edge `0.3219` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.6912` n `50` status `ready` deltaP `33.9817` edge `0.1064` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1236` n `50` status `ready` deltaP `29.2195` edge `0.1005` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1515` n `50` status `ready` deltaP `24.2455` edge `0.0431` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4688` n `50` status `ready` deltaP `18.8443` edge `0.0269` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9033` n `50` status `ready` deltaP `19.6926` edge `0.2018` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7149` n `50` status `ready` deltaP `16.2455` edge `0.0813` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6705` n `50` status `ready` deltaP `18.2455` edge `0.0695` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
