# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T10:07:29.778689+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11540`

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

- `market_context_high->unknown_24h` score `252.2259` n `88` status `ready` deltaP `6.0318` edge `20.9927` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `91.5594` n `88` status `ready` deltaP `7.2201` edge `7.6266` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.2191` n `53` status `ready` deltaP `21.0486` edge `2.2819` maxDD `-3.6503`
- `market_context_high->equity_24h` score `13.8934` n `88` status `ready` deltaP `14.9379` edge `1.3141` maxDD `-16.8057`
- `news_risk_high->crypto_major_24h` score `11.8016` n `53` status `ready` deltaP `36.8969` edge `1.4636` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.4604` n `53` status `ready` deltaP `34.8682` edge `0.8356` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9341` n `53` status `ready` deltaP `40.3114` edge `0.3091` maxDD `0.0`
- `market_context_high->metal_24h` score `4.9509` n `88` status `ready` deltaP `35.0071` edge `0.2345` maxDD `-1.4245`
- `market_context_high->crypto_alt_24h` score `4.941` n `88` status `ready` deltaP `34.9638` edge `0.9098` maxDD `-33.4213`
- `news_risk_high->metal_4h` score `4.464` n `53` status `ready` deltaP `42.8901` edge `0.1237` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1136` n `53` status `ready` deltaP `22.2676` edge `0.3431` maxDD `-9.2335`
- `news_risk_high->index_24h` score `3.6652` n `53` status `ready` deltaP `19.302` edge `0.2071` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.589` n `53` status `ready` deltaP `17.8652` edge `0.243` maxDD `-3.7082`
- `market_context_high->index_24h` score `2.8006` n `88` status `ready` deltaP `16.9864` edge `0.1664` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7978` n `53` status `ready` deltaP `25.0345` edge `0.0916` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.2748` n `53` status `ready` deltaP `26.0411` edge `0.2819` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.2605` n `53` status `ready` deltaP `21.6607` edge `0.0876` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1451` n `53` status `ready` deltaP `25.4406` edge `0.0346` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3041` n `53` status `ready` deltaP `17.176` edge `0.0243` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8108` n `53` status `ready` deltaP `18.0431` edge `0.0816` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
