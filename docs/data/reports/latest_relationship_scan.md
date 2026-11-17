# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T10:22:27.586777+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4096`

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

- `market_context_high->unknown_24h` score `2000.2271` n `80` status `ready` deltaP `3.4483` edge `166.6626` maxDD `0.0`
- `news_risk_high->equity_24h` score `57.74` n `50` status `ready` deltaP `64.3793` edge `4.4531` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.811` n `50` status `ready` deltaP `31.6207` edge `2.187` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6859` n `50` status `ready` deltaP `44.7073` edge `1.0388` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.191` n `80` status `ready` deltaP `43.6207` edge `1.8556` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.0048` n `80` status `ready` deltaP `26.4655` edge `1.7032` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.8833` n `50` status `ready` deltaP `55.7586` edge `0.3989` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.6238` n `50` status `ready` deltaP `17.9655` edge `1.4364` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.4946` n `50` status `ready` deltaP `50.1724` edge `0.3734` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0388` n `50` status `ready` deltaP `44.689` edge `0.1596` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.7108` n `50` status `ready` deltaP `23.5928` edge `0.2983` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4864` n `50` status `ready` deltaP `26.689` edge `0.3395` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0294` n `50` status `ready` deltaP `20.9939` edge `0.3334` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.8707` n `50` status `ready` deltaP `35.5061` edge `0.1112` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2183` n `50` status `ready` deltaP `30.1341` edge `0.1023` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2293` n `50` status `ready` deltaP `24.994` edge `0.0446` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5658` n `50` status `ready` deltaP `19.8922` edge `0.028` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8249` n `50` status `ready` deltaP `16.994` edge `0.0904` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7679` n `50` status `ready` deltaP `18.8443` edge `0.078` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7599` n `50` status `ready` deltaP `18.0` edge `0.1947` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
