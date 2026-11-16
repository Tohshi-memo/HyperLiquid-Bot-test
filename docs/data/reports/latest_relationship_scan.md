# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T11:07:38.784754+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4058`

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

- `market_context_high->unknown_24h` score `102.9614` n `30` status `ready` deltaP `3.9931` edge `8.5535` maxDD `0.0`
- `news_risk_high->equity_24h` score `51.1925` n `50` status `ready` deltaP `55.3611` edge `3.9676` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.3735` n `50` status `ready` deltaP `41.8542` edge `2.5755` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.1536` n `30` status `ready` deltaP `13.7152` edge `1.5758` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.509` n `30` status `ready` deltaP `43.8542` edge `1.6384` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.4921` n `50` status `ready` deltaP `39.8293` edge `0.8885` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `10.0245` n `50` status `ready` deltaP `24.3819` edge `1.5732` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.5053` n `50` status `ready` deltaP `46.3333` edge `0.3469` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0258` n `50` status `ready` deltaP `40.9722` edge `0.229` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1009` n `50` status `ready` deltaP `45.4512` edge `0.1597` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7484` n `50` status `ready` deltaP `27.9085` edge `0.3532` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.4324` n `50` status `ready` deltaP `21.7561` edge `0.3619` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9613` n `50` status `ready` deltaP `20.4491` edge `0.2568` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.932` n `30` status `ready` deltaP `48.2639` edge `0.2715` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.6506` n `50` status `ready` deltaP `34.1341` edge `0.102` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5935` n `50` status `ready` deltaP `24.7988` edge `0.0858` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1958` n `50` status `ready` deltaP `24.8443` edge `0.0428` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2855` n `50` status `ready` deltaP `17.0479` edge `0.0236` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0535` n `50` status `ready` deltaP `19.5972` edge `0.2217` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8325` n `50` status `ready` deltaP `18.0419` edge `0.0844` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
