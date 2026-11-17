# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T01:37:29.835989+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4392`

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

- `market_context_high->unknown_24h` score `1891.1123` n `54` status `ready` deltaP `3.4483` edge `157.5697` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.643` n `50` status `ready` deltaP `59.2069` edge `4.2295` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.6298` n `50` status `ready` deltaP `37.1379` edge `2.3834` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.8463` n `54` status `ready` deltaP `13.2886` edge `1.5158` maxDD `-12.3757`
- `news_risk_high->equity_4h` score `14.5994` n `50` status `ready` deltaP `44.5549` edge `1.0326` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.7053` n `54` status `ready` deltaP `40.249` edge `1.6876` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3639` n `50` status `ready` deltaP `22.1034` edge `1.5037` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1323` n `50` status `ready` deltaP `50.2414` edge `0.3731` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.0638` n `50` status `ready` deltaP `44.1379` edge `0.2944` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3551` n `50` status `ready` deltaP `47.128` edge `0.1697` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5909` n `50` status `ready` deltaP `22.8443` edge `0.2933` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4752` n `50` status `ready` deltaP `26.3841` edge `0.3406` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.2968` n `50` status `ready` deltaP `21.7561` edge `0.3506` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1057` n `50` status `ready` deltaP `37.1829` edge `0.1196` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1674` n `50` status `ready` deltaP `29.6768` edge `0.1011` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2809` n `50` status `ready` deltaP `25.4431` edge `0.0459` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5467` n `50` status `ready` deltaP `19.7425` edge `0.0274` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8605` n `50` status `ready` deltaP `18.3448` edge `0.2053` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8544` n `50` status `ready` deltaP `17.5928` edge `0.0902` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8147` n `50` status `ready` deltaP `19.1437` edge `0.082` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
