# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T09:22:34.535718+00:00`
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

- `market_context_high->unknown_24h` score `238.0358` n `88` status `ready` deltaP `6.0318` edge `19.8102` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `89.3706` n `88` status `ready` deltaP `7.2201` edge `7.4442` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `29.8511` n `52` status `ready` deltaP `23.9486` edge `2.3891` maxDD `-3.2263`
- `market_context_high->equity_24h` score `14.6193` n `88` status `ready` deltaP `16.5185` edge `1.3473` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.1917` n `52` status `ready` deltaP `37.9491` edge `1.5066` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5606` n `53` status `ready` deltaP `35.1731` edge `0.8411` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.9143` n `52` status `ready` deltaP `40.1384` edge `0.3086` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.0588` n `88` status `ready` deltaP `34.9638` edge `0.9249` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.9113` n `88` status `ready` deltaP `35.0071` edge `0.2312` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.4131` n `53` status `ready` deltaP `42.4327` edge `0.1225` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1968` n `53` status `ready` deltaP `22.5725` edge `0.348` maxDD `-9.2335`
- `news_risk_high->index_24h` score `3.9793` n `52` status `ready` deltaP `21.0074` edge `0.2176` maxDD `-0.4168`
- `news_risk_high->equity_1h` score `3.5442` n `53` status `ready` deltaP `18.1646` edge `0.2455` maxDD `-3.6997`
- `market_context_high->index_24h` score `2.8474` n `88` status `ready` deltaP `16.9864` edge `0.1703` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.77` n `53` status `ready` deltaP `24.8821` edge `0.0903` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.3265` n `53` status `ready` deltaP `26.1936` edge `0.2875` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.3031` n `53` status `ready` deltaP `22.118` edge `0.0881` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1307` n `53` status `ready` deltaP `25.2909` edge `0.0344` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3317` n `53` status `ready` deltaP `17.4754` edge `0.0246` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8326` n `53` status `ready` deltaP `18.3425` edge `0.0824` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
