# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T17:52:26.062328+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `370.5982` n `75` status `ready` deltaP `3.2361` edge `30.8757` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.5011` n `53` status `ready` deltaP `32.2786` edge `2.6472` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.2675` n `75` status `ready` deltaP `26.8194` edge `2.081` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.4848` n `75` status `ready` deltaP `49.1459` edge `1.3809` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.3593` n `53` status `ready` deltaP `42.0434` edge `1.7572` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.7744` n `53` status `ready` deltaP `34.2585` edge `0.7825` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.6052` n `53` status `ready` deltaP `36.2847` edge `0.2252` maxDD `0.0`
- `market_context_high->index_24h` score `4.82` n `75` status `ready` deltaP `25.5625` edge `0.2404` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.7172` n `53` status `ready` deltaP `44.7193` edge `0.1326` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.139` n `53` status `ready` deltaP `23.575` edge `0.2181` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.9279` n `75` status `ready` deltaP `39.4236` edge `0.3299` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3647` n `53` status `ready` deltaP `17.2664` edge `0.2283` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1337` n `53` status `ready` deltaP `28.6931` edge `0.0952` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0933` n `53` status `ready` deltaP `19.2189` edge `0.2784` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1667` n `53` status `ready` deltaP `25.4406` edge `0.0364` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `2.1593` n `53` status `ready` deltaP `15.9886` edge `0.6208` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.9836` n `53` status `ready` deltaP `19.9839` edge `0.0757` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7599` n `53` status `ready` deltaP `25.8887` edge `0.2169` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1867` n `53` status `ready` deltaP `16.1281` edge `0.0215` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6291` n `53` status `ready` deltaP `17.1449` edge `0.0643` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
