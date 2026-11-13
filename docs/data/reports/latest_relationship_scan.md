# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T23:07:24.195068+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10332`

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

- `market_context_high->unknown_24h` score `379.7813` n `75` status `ready` deltaP `2.1944` edge `31.6479` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.9614` n `53` status `ready` deltaP `34.3619` edge `2.755` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.7277` n `75` status `ready` deltaP `28.9027` edge `2.1888` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.875` n `75` status `ready` deltaP `47.5834` edge `1.3405` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.7064` n `53` status `ready` deltaP `42.0434` edge `1.8017` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9166` n `53` status `ready` deltaP `34.7158` edge `0.7913` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.0021` n `53` status `ready` deltaP `39.2361` edge `0.2386` maxDD `0.0`
- `market_context_high->index_24h` score `5.2118` n `75` status `ready` deltaP `29.0348` edge `0.2499` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.9991` n `53` status `ready` deltaP `47.4632` edge `0.1378` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.5308` n `53` status `ready` deltaP `27.0473` edge `0.2276` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1114` n `75` status `ready` deltaP `41.3334` edge `0.3407` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5217` n `53` status `ready` deltaP `18.3143` edge `0.2344` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.3286` n `53` status `ready` deltaP `20.2859` edge `0.2909` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.2367` n `53` status `ready` deltaP `29.4553` edge `0.0987` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2901` n `53` status `ready` deltaP `26.7879` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.8886` n `53` status `ready` deltaP `18.9168` edge `0.0749` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7775` n `53` status `ready` deltaP `25.4314` edge `0.2222` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7629` n `53` status `ready` deltaP `14.4261` edge `0.5804` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1616` n `53` status `ready` deltaP `15.8287` edge `0.0214` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6447` n `53` status `ready` deltaP `16.9952` edge `0.0673` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
