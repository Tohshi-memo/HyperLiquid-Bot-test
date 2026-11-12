# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T10:52:29.616818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `266.2719` n `88` status `ready` deltaP `6.0318` edge `22.1632` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `98.0178` n `88` status `ready` deltaP `7.2201` edge `8.1648` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.9743` n `53` status `ready` deltaP `21.0486` edge `2.2615` maxDD `-3.6503`
- `market_context_high->equity_24h` score `13.6486` n `88` status `ready` deltaP `14.9379` edge `1.2937` maxDD `-16.8057`
- `news_risk_high->crypto_major_24h` score `11.6183` n `53` status `ready` deltaP `36.8969` edge `1.4401` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3422` n `53` status `ready` deltaP `34.4109` edge `0.8288` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.0296` n `53` status `ready` deltaP `40.8304` edge `0.3136` maxDD `0.0`
- `market_context_high->metal_24h` score `4.9929` n `88` status `ready` deltaP `35.0071` edge `0.238` maxDD `-1.4245`
- `market_context_high->crypto_alt_24h` score `4.8544` n `88` status `ready` deltaP `34.9638` edge `0.8987` maxDD `-33.4213`
- `news_risk_high->metal_4h` score `4.5138` n `53` status `ready` deltaP `43.3474` edge `0.1248` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.0074` n `53` status `ready` deltaP `21.8103` edge `0.3373` maxDD `-9.2335`
- `news_risk_high->index_24h` score `3.6153` n `53` status `ready` deltaP `19.129` edge `0.2041` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.6106` n `53` status `ready` deltaP `18.0149` edge `0.2438` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.8474` n `53` status `ready` deltaP `25.3394` edge `0.0937` maxDD `-0.3611`
- `market_context_high->index_24h` score `2.7508` n `88` status `ready` deltaP `16.8134` edge `0.1634` maxDD `-2.3671`
- `news_risk_high->index_4h` score `2.2191` n `53` status `ready` deltaP `21.2034` edge `0.0872` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2019` n `53` status `ready` deltaP `25.5838` edge `0.2756` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1187` n `53` status `ready` deltaP `25.1412` edge `0.0344` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3173` n `53` status `ready` deltaP `17.3257` edge `0.0244` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7718` n `53` status `ready` deltaP `17.594` edge `0.0796` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
