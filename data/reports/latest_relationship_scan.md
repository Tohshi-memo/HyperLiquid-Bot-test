# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T22:07:24.743896+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10308`

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

- `market_context_high->unknown_24h` score `370.0409` n `75` status `ready` deltaP `2.1944` edge `30.8362` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.7094` n `53` status `ready` deltaP `34.3619` edge `2.734` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.4757` n `75` status `ready` deltaP `28.9027` edge `2.1678` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9062` n `75` status `ready` deltaP `47.5834` edge `1.3431` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.6026` n `53` status `ready` deltaP `42.0434` edge `1.7884` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8502` n `53` status `ready` deltaP `34.4109` edge `0.7878` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.9129` n `53` status `ready` deltaP `38.5417` edge `0.2358` maxDD `0.0`
- `market_context_high->index_24h` score `5.1334` n `75` status `ready` deltaP `28.3403` edge `0.248` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.9541` n `53` status `ready` deltaP `47.0059` edge `0.1371` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.4524` n `53` status `ready` deltaP `26.3528` edge `0.2257` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.086` n `75` status `ready` deltaP `41.1598` edge `0.3386` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5001` n `53` status `ready` deltaP `18.1646` edge `0.2336` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2537` n `53` status `ready` deltaP `29.6077` edge `0.0991` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1707` n `53` status `ready` deltaP `19.6762` edge `0.2818` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2781` n `53` status `ready` deltaP `26.6382` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.8996` n `53` status `ready` deltaP `19.0693` edge `0.0748` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.7832` n `53` status `ready` deltaP `14.4261` edge `0.583` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.7268` n `53` status `ready` deltaP `25.4314` edge `0.2157` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1747` n `53` status `ready` deltaP `15.9784` edge `0.0215` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6385` n `53` status `ready` deltaP `16.9952` edge `0.0665` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
