# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T09:37:32.360191+00:00`
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

- `market_context_high->unknown_24h` score `242.9175` n `88` status `ready` deltaP `6.0318` edge `20.217` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `89.0226` n `88` status `ready` deltaP `7.2201` edge `7.4152` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.4411` n `53` status `ready` deltaP `21.0486` edge `2.3004` maxDD `-3.6503`
- `market_context_high->equity_24h` score `14.1154` n `88` status `ready` deltaP `14.9379` edge `1.3326` maxDD `-16.8057`
- `news_risk_high->crypto_major_24h` score `11.9521` n `53` status `ready` deltaP `36.8969` edge `1.4829` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5496` n `53` status `ready` deltaP `35.1731` edge `0.841` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.8819` n `53` status `ready` deltaP `40.1384` edge `0.3059` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.0205` n `88` status `ready` deltaP `34.9638` edge `0.92` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.9233` n `88` status `ready` deltaP `35.0071` edge `0.2322` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.4313` n `53` status `ready` deltaP `42.5852` edge `0.123` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1872` n `53` status `ready` deltaP `22.5725` edge `0.3472` maxDD `-9.2335`
- `news_risk_high->index_24h` score `3.6952` n `53` status `ready` deltaP `19.302` edge `0.2096` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.613` n `53` status `ready` deltaP `18.0149` edge `0.244` maxDD `-3.7082`
- `market_context_high->index_24h` score `2.8306` n `88` status `ready` deltaP `16.9864` edge `0.1689` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7736` n `53` status `ready` deltaP `24.8821` edge `0.0906` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.3202` n `53` status `ready` deltaP `26.1936` edge `0.2867` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.2897` n `53` status `ready` deltaP `21.9656` edge `0.088` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1451` n `53` status `ready` deltaP `25.4406` edge `0.0346` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3173` n `53` status `ready` deltaP `17.3257` edge `0.0244` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8334` n `53` status `ready` deltaP `18.3425` edge `0.0825` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
