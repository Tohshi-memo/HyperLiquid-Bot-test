# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T14:52:32.950152+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3988`

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

- `market_context_high->unknown_24h` score `1616.4104` n `93` status `ready` deltaP `3.4602` edge `134.6778` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.4634` n `50` status `ready` deltaP `67.4118` edge `4.5765` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.0508` n `50` status `ready` deltaP `28.7612` edge `2.1086` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.815` n `93` status `ready` deltaP `44.9547` edge `1.9267` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.9915` n `93` status `ready` deltaP `30.2471` edge `1.8045` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `13.9816` n `50` status `ready` deltaP `42.878` edge `0.9923` maxDD `-7.0416`
- `news_risk_high->index_24h` score `9.2759` n `50` status `ready` deltaP `58.7612` edge `0.4116` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.2015` n `50` status `ready` deltaP `53.1142` edge `0.4127` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0516` n `50` status `ready` deltaP `15.1073` edge `1.3821` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.8582` n `50` status `ready` deltaP `43.3171` edge `0.1537` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.429` n `50` status `ready` deltaP `22.5449` edge `0.2818` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.067` n `50` status `ready` deltaP `25.3171` edge `0.3137` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.6522` n `50` status `ready` deltaP `33.5244` edge `0.1062` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.2792` n `50` status `ready` deltaP `19.0122` edge `0.2841` maxDD `-9.0062`
- `news_risk_high->index_4h` score `3.0166` n `50` status `ready` deltaP `28.1524` edge `0.0987` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1251` n `50` status `ready` deltaP `23.9461` edge `0.0429` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4688` n `50` status `ready` deltaP `18.8443` edge `0.0269` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0044` n `50` status `ready` deltaP `20.872` edge `0.2069` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7375` n `50` status `ready` deltaP `16.5449` edge `0.0822` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6237` n `50` status `ready` deltaP `17.7964` edge `0.0665` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
