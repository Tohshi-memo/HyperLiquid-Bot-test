# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T15:37:32.895029+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3992`

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

- `market_context_high->unknown_24h` score `1542.0116` n `96` status `ready` deltaP `3.4602` edge `128.4779` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.8505` n `50` status `ready` deltaP `67.9308` edge `4.6053` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `16.9271` n `50` status `ready` deltaP `28.2422` edge `2.0962` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `15.0397` n `96` status `ready` deltaP `45.2422` edge `1.9536` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.2431` n `96` status `ready` deltaP `31.0049` edge `1.8317` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `13.9804` n `50` status `ready` deltaP `42.878` edge `0.9922` maxDD `-7.0416`
- `news_risk_high->index_24h` score `9.351` n `50` status `ready` deltaP `59.2803` edge `0.4144` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.3223` n `50` status `ready` deltaP `53.6332` edge `0.4193` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.9622` n `50` status `ready` deltaP `14.5882` edge `1.3741` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.8414` n `50` status `ready` deltaP `43.3171` edge `0.1523` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5309` n `50` status `ready` deltaP `22.8443` edge `0.2883` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `3.9563` n `50` status `ready` deltaP `25.0122` edge `0.3065` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.6774` n `50` status `ready` deltaP `33.5244` edge `0.1083` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1253` n `50` status `ready` deltaP `18.7073` edge `0.2733` maxDD `-9.0062`
- `news_risk_high->index_4h` score `3.0154` n `50` status `ready` deltaP `28.1524` edge `0.0986` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1071` n `50` status `ready` deltaP `23.7964` edge `0.0424` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4976` n `50` status `ready` deltaP `19.1437` edge `0.0273` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0251` n `50` status `ready` deltaP `21.045` edge `0.2084` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7812` n `50` status `ready` deltaP `16.8443` edge `0.0858` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6339` n `50` status `ready` deltaP `17.7964` edge `0.0678` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
