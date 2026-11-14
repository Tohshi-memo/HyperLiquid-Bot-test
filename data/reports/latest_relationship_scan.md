# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T02:07:24.474348+00:00`
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

- `market_context_high->unknown_24h` score `404.0741` n `75` status `ready` deltaP `2.1944` edge `33.6723` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.0173` n `53` status `ready` deltaP `35.23` edge `2.8372` maxDD `-3.6503`
- `market_context_high->equity_24h` score `27.7836` n `75` status `ready` deltaP `29.7708` edge `2.271` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9194` n `75` status `ready` deltaP `47.5834` edge `1.3442` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.0784` n `53` status `ready` deltaP `42.0434` edge `1.8494` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.1932` n `53` status `ready` deltaP `36.0877` edge `0.8052` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.1835` n `53` status `ready` deltaP `40.7986` edge `0.2433` maxDD `0.0`
- `market_context_high->index_24h` score `5.4709` n `75` status `ready` deltaP `31.1181` edge `0.2576` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0637` n `53` status `ready` deltaP `48.2254` edge `0.1381` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.7899` n `53` status `ready` deltaP `29.1306` edge `0.2353` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1785` n `75` status `ready` deltaP `41.3334` edge `0.3493` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `3.5802` n `53` status `ready` deltaP `20.8957` edge `0.3078` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5637` n `53` status `ready` deltaP `18.6137` edge `0.2359` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0701` n `53` status `ready` deltaP `27.7784` edge `0.096` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2901` n `53` status `ready` deltaP `26.7879` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9934` n `53` status `ready` deltaP `20.1363` edge `0.0755` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8696` n `53` status `ready` deltaP `25.5838` edge `0.233` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7918` n `53` status `ready` deltaP `14.4261` edge `0.5841` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1999` n `53` status `ready` deltaP `16.2778` edge `0.0216` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6876` n `53` status `ready` deltaP `17.594` edge `0.0688` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
