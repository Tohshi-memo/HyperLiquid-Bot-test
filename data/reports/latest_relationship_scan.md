# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T09:22:26.172387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9714`

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

- `market_context_high->unknown_24h` score `465.3593` n `75` status `ready` deltaP `2.1944` edge `38.7794` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.7839` n `53` status `ready` deltaP `36.7925` edge `2.974` maxDD `-3.6503`
- `market_context_high->equity_24h` score `29.5502` n `75` status `ready` deltaP `31.3333` edge `2.4078` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.7826` n `75` status `ready` deltaP `47.5834` edge `1.3328` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.7874` n `53` status `ready` deltaP `42.0434` edge `1.9403` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2692` n `53` status `ready` deltaP `36.3926` edge `0.8095` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.7483` n `53` status `ready` deltaP `45.8333` edge `0.2568` maxDD `0.0`
- `market_context_high->index_24h` score `6.038` n `75` status `ready` deltaP `36.1528` edge `0.2713` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.357` n `53` status `ready` deltaP `34.1653` edge `0.249` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `4.9733` n `53` status `ready` deltaP `47.0059` edge `0.1387` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3555` n `75` status `ready` deltaP `41.3334` edge `0.372` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.1474` n `53` status `ready` deltaP `21.5054` edge `0.351` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.602` n `53` status `ready` deltaP `18.9131` edge `0.2371` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1249` n `53` status `ready` deltaP `28.3882` edge `0.0965` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2074` n `53` status `ready` deltaP `25.74` edge `0.0378` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1675` n `53` status `ready` deltaP `22.118` edge `0.0768` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1003` n `53` status `ready` deltaP `26.1936` edge `0.2585` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7028` n `53` status `ready` deltaP `14.4261` edge `0.5727` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2753` n `53` status `ready` deltaP `17.176` edge `0.0219` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7793` n `53` status `ready` deltaP `18.4922` edge `0.0818` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
