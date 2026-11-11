# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T21:52:28.662600+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11578`

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

- `market_context_high->unknown_4h` score `92.9236` n `88` status `ready` deltaP `8.5383` edge `7.7315` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `54.5215` n `30` status `ready` deltaP `38.4083` edge `4.2874` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `29.7227` n `30` status `ready` deltaP `53.737` edge `2.3152` maxDD `-12.7247`
- `market_context_high->equity_24h` score `22.5657` n `88` status `ready` deltaP `21.3628` edge `1.9772` maxDD `-16.7984`
- `market_context_high->unknown_24h` score `21.3084` n `88` status `ready` deltaP `4.9937` edge `1.7565` maxDD `-0.4609`
- `news_risk_high->crypto_alt_24h` score `16.6515` n `30` status `ready` deltaP `36.955` edge `1.3161` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.1368` n `53` status `ready` deltaP `34.1199` edge `0.8128` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.8257` n `30` status `ready` deltaP `35.1211` edge `0.418` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.4776` n `30` status `ready` deltaP `39.9654` edge `0.3567` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.0685` n `88` status `ready` deltaP `35.1368` edge `1.1814` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.5705` n `88` status `ready` deltaP `32.4119` edge `0.2201` maxDD `-1.4245`
- `market_context_high->index_24h` score `4.2297` n `88` status `ready` deltaP `21.4847` edge `0.2555` maxDD `-2.3671`
- `news_risk_high->metal_4h` score `4.0526` n `53` status `ready` deltaP `39.832` edge `0.1098` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.465` n `53` status `ready` deltaP `18.0149` edge `0.2399` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.4237` n `53` status `ready` deltaP `19.344` edge `0.3051` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.7135` n `53` status `ready` deltaP `24.4452` edge `0.0885` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2344` n `53` status `ready` deltaP `21.0644` edge `0.0894` maxDD `-0.8235`
- `news_risk_high->metal_24h` score `2.0537` n `30` status `ready` deltaP `25.0634` edge `0.1316` maxDD `-0.4982`
- `news_risk_high->metal_1h` score `2.0061` n `53` status `ready` deltaP `24.243` edge `0.031` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.8147` n `53` status `ready` deltaP `23.1175` edge `0.2424` maxDD `-10.1088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
