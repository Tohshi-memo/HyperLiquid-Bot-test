# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T02:22:27.119229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10302`

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

- `market_context_high->unknown_24h` score `406.0937` n `75` status `ready` deltaP `2.1944` edge `33.8406` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.0989` n `53` status `ready` deltaP `35.23` edge `2.844` maxDD `-3.6503`
- `market_context_high->equity_24h` score `27.8652` n `75` status `ready` deltaP `29.7708` edge `2.2778` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9326` n `75` status `ready` deltaP `47.5834` edge `1.3453` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.1174` n `53` status `ready` deltaP `42.0434` edge `1.8544` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.215` n `53` status `ready` deltaP `36.2402` edge `0.806` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.2022` n `53` status `ready` deltaP `40.9722` edge `0.2437` maxDD `0.0`
- `market_context_high->index_24h` score `5.4931` n `75` status `ready` deltaP `31.2917` edge `0.2583` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0637` n `53` status `ready` deltaP `48.2254` edge `0.1381` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.8122` n `53` status `ready` deltaP `29.3042` edge `0.236` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1863` n `75` status `ready` deltaP `41.3334` edge `0.3503` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `3.5982` n `53` status `ready` deltaP `20.8957` edge `0.3093` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5804` n `53` status `ready` deltaP `18.7634` edge `0.2363` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0555` n `53` status `ready` deltaP `27.626` edge `0.0958` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2901` n `53` status `ready` deltaP `26.7879` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0056` n `53` status `ready` deltaP `20.2888` edge `0.0755` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8767` n `53` status `ready` deltaP `25.5838` edge `0.2339` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.8003` n `53` status `ready` deltaP `14.4261` edge `0.5852` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1999` n `53` status `ready` deltaP `16.2778` edge `0.0216` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7001` n `53` status `ready` deltaP `17.594` edge `0.0704` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
