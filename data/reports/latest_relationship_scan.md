# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T12:22:25.426179+00:00`
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

- `market_context_high->unknown_24h` score `1787.0283` n `87` status `ready` deltaP `3.4542` edge `148.896` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.4677` n `50` status `ready` deltaP `65.7202` edge `4.5048` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.4915` n `50` status `ready` deltaP `30.3661` edge `2.1544` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.4876` n `87` status `ready` deltaP `44.7799` edge `1.8859` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.408` n `50` status `ready` deltaP `44.0976` edge `1.0197` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `13.5447` n `87` status `ready` deltaP `29.0334` edge `1.7553` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.0518` n `50` status `ready` deltaP `57.0846` edge `0.4041` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.8382` n `50` status `ready` deltaP `51.468` edge `0.3934` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.3823` n `50` status `ready` deltaP `16.7116` edge `1.4138` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.9818` n `50` status `ready` deltaP `44.2317` edge `0.1579` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.4961` n `50` status `ready` deltaP `22.8443` edge `0.2854` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.444` n `50` status `ready` deltaP `26.3841` edge `0.338` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `3.9038` n `50` status `ready` deltaP `20.3841` edge `0.327` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.7458` n `50` status `ready` deltaP `34.439` edge `0.1079` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1394` n `50` status `ready` deltaP `29.372` edge `0.1008` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1251` n `50` status `ready` deltaP `23.9461` edge `0.0429` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4688` n `50` status `ready` deltaP `18.8443` edge `0.0269` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8584` n `50` status `ready` deltaP `19.1744` edge `0.1995` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7204` n `50` status `ready` deltaP `16.2455` edge `0.082` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6791` n `50` status `ready` deltaP `18.2455` edge `0.0706` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
