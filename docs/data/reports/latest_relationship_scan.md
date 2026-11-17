# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T15:07:43.866856+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3998`

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

- `market_context_high->unknown_24h` score `1591.088` n `94` status `ready` deltaP `3.4602` edge `132.5676` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.5792` n `50` status `ready` deltaP `67.5848` edge `4.585` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.0145` n `50` status `ready` deltaP `28.5882` edge `2.1051` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.8468` n `94` status `ready` deltaP `45.0563` edge `1.9301` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.0418` n `94` status `ready` deltaP `30.5088` edge `1.8092` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `13.9612` n `50` status `ready` deltaP `42.878` edge `0.9906` maxDD `-7.0416`
- `news_risk_high->index_24h` score `9.2994` n `50` status `ready` deltaP `58.9343` edge `0.4124` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.2382` n `50` status `ready` deltaP `53.2872` edge `0.4146` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0254` n `50` status `ready` deltaP `14.9343` edge `1.3799` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.8522` n `50` status `ready` deltaP `43.3171` edge `0.1532` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.4314` n `50` status `ready` deltaP `22.5449` edge `0.282` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.0224` n `50` status `ready` deltaP `25.1646` edge `0.311` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.657` n `50` status `ready` deltaP `33.5244` edge `0.1066` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.2203` n `50` status `ready` deltaP `18.8598` edge `0.2802` maxDD `-9.0062`
- `news_risk_high->index_4h` score `3.0142` n `50` status `ready` deltaP `28.1524` edge `0.0985` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1239` n `50` status `ready` deltaP `23.9461` edge `0.0428` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4688` n `50` status `ready` deltaP `18.8443` edge `0.0269` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.018` n `50` status `ready` deltaP `21.045` edge `0.2075` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.743` n `50` status `ready` deltaP `16.5449` edge `0.0829` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6222` n `50` status `ready` deltaP `17.7964` edge `0.0663` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
