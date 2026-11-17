# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T07:07:34.456941+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4212`

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

- `market_context_high->unknown_24h` score `2403.4211` n `67` status `ready` deltaP `3.4483` edge `200.2621` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.3583` n `50` status `ready` deltaP `62.1379` edge `4.3529` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.5188` n `50` status `ready` deltaP `33.8621` edge `2.2628` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.3309` n `67` status `ready` deltaP `19.4905` edge `1.61` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.5308` n `50` status `ready` deltaP `44.4024` edge `1.0279` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.3302` n `67` status `ready` deltaP `40.0412` edge `1.7691` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.0749` n `50` status `ready` deltaP `20.2069` edge `1.4793` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.5684` n `50` status `ready` deltaP `53.5172` edge `0.3876` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.9709` n `50` status `ready` deltaP `47.931` edge `0.3447` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0688` n `50` status `ready` deltaP `44.689` edge `0.1621` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6676` n `50` status `ready` deltaP `23.5928` edge `0.2947` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4782` n `50` status `ready` deltaP `26.8415` edge `0.3378` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.1064` n `50` status `ready` deltaP `21.1463` edge `0.3388` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0973` n `50` status `ready` deltaP `37.1829` edge `0.1189` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2379` n `50` status `ready` deltaP `30.439` edge `0.1019` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2341` n `50` status `ready` deltaP `24.994` edge `0.045` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5874` n `50` status `ready` deltaP `20.1916` edge `0.0278` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8093` n `50` status `ready` deltaP `16.994` edge `0.0884` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7765` n `50` status `ready` deltaP `18.8443` edge `0.0791` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7252` n `50` status `ready` deltaP `17.4828` edge `0.1937` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
