# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T15:22:36.303856+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4082`

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

- `market_context_high->unknown_24h` score `59.2347` n `30` status `ready` deltaP `3.9792` edge `4.9097` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.8972` n `50` status `ready` deltaP `58.0692` edge `4.0916` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.5008` n `50` status `ready` deltaP `42.083` edge `2.5903` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.6556` n `30` status `ready` deltaP `14.9942` edge `1.6091` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.7882` n `50` status `ready` deltaP `42.1857` edge `0.9808` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6363` n `30` status `ready` deltaP `44.083` edge `1.6532` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3507` n `50` status `ready` deltaP `25.6609` edge `1.6065` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.884` n `50` status `ready` deltaP `49.0727` edge `0.3602` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1009` n `50` status `ready` deltaP `41.1765` edge `0.2339` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.1978` n `50` status `ready` deltaP `29.4916` edge `0.3801` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.0839` n `50` status `ready` deltaP `45.2085` edge `0.1599` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.817` n `50` status `ready` deltaP `23.3394` edge `0.3834` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.2095` n `50` status `ready` deltaP `21.497` edge `0.2705` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8923` n `50` status `ready` deltaP `35.8813` edge `0.1105` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8298` n `30` status `ready` deltaP `46.9435` edge `0.2672` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.8905` n `50` status `ready` deltaP `27.0107` edge `0.0958` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2688` n `50` status `ready` deltaP `25.5928` edge `0.0439` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3634` n `50` status `ready` deltaP `17.7964` edge `0.0251` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9513` n `50` status `ready` deltaP `18.2768` edge `0.2174` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9269` n `50` status `ready` deltaP `18.6407` edge `0.0925` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
