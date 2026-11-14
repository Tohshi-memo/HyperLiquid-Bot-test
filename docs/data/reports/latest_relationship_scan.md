# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T05:07:26.559548+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10392`

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

- `market_context_high->unknown_24h` score `429.0953` n `75` status `ready` deltaP `2.1944` edge `35.7574` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.7841` n `53` status `ready` deltaP `35.23` edge `2.9011` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.5504` n `75` status `ready` deltaP `29.7708` edge `2.3349` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.7046` n `75` status `ready` deltaP `47.5834` edge `1.3263` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.353` n `53` status `ready` deltaP `42.0434` edge `1.8846` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2632` n `53` status `ready` deltaP `36.3926` edge `0.809` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.4102` n `53` status `ready` deltaP `42.8819` edge `0.2483` maxDD `0.0`
- `market_context_high->index_24h` score `5.7191` n `75` status `ready` deltaP `33.2014` edge `0.2644` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0733` n `53` status `ready` deltaP `48.2254` edge `0.1389` maxDD `-1.0104`
- `news_risk_high->index_24h` score `5.0381` n `53` status `ready` deltaP `31.2139` edge `0.2421` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.2721` n `75` status `ready` deltaP `41.3334` edge `0.3613` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.0288` n `53` status `ready` deltaP `21.6579` edge `0.3401` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6403` n `53` status `ready` deltaP `19.3622` edge `0.2373` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0081` n `53` status `ready` deltaP `27.1687` edge `0.0949` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3308` n `53` status `ready` deltaP `27.237` edge `0.0381` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1419` n `53` status `ready` deltaP `21.8132` edge `0.0767` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0762` n `53` status `ready` deltaP `26.346` edge `0.2544` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6521` n `53` status `ready` deltaP `14.4261` edge `0.5662` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2622` n `53` status `ready` deltaP `17.0263` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7325` n `53` status `ready` deltaP `17.8934` edge `0.0798` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
