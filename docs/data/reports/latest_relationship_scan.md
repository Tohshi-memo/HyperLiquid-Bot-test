# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T10:37:35.718561+00:00`
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

- `market_context_high->unknown_24h` score `261.4947` n `88` status `ready` deltaP `6.0318` edge `21.7651` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `94.6614` n `88` status `ready` deltaP `7.2201` edge `7.8851` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.0499` n `53` status `ready` deltaP `21.0486` edge `2.2678` maxDD `-3.6503`
- `market_context_high->equity_24h` score `13.7242` n `88` status `ready` deltaP `14.9379` edge `1.3` maxDD `-16.8057`
- `news_risk_high->crypto_major_24h` score `11.6775` n `53` status `ready` deltaP `36.8969` edge `1.4477` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3856` n `53` status `ready` deltaP `34.5633` edge `0.8314` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.0002` n `53` status `ready` deltaP `40.6574` edge `0.3123` maxDD `0.0`
- `market_context_high->metal_24h` score `4.9797` n `88` status `ready` deltaP `35.0071` edge `0.2369` maxDD `-1.4245`
- `market_context_high->crypto_alt_24h` score `4.8825` n `88` status `ready` deltaP `34.9638` edge `0.9023` maxDD `-33.4213`
- `news_risk_high->metal_4h` score `4.4968` n `53` status `ready` deltaP `43.1949` edge `0.1244` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.0472` n `53` status `ready` deltaP `21.9628` edge `0.3396` maxDD `-9.2335`
- `news_risk_high->index_24h` score `3.6261` n `53` status `ready` deltaP `19.129` edge `0.205` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.595` n `53` status `ready` deltaP `17.8652` edge `0.2435` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.828` n `53` status `ready` deltaP `25.187` edge `0.0931` maxDD `-0.3611`
- `market_context_high->index_24h` score `2.7616` n `88` status `ready` deltaP `16.8134` edge `0.1643` maxDD `-2.3671`
- `news_risk_high->index_4h` score `2.2337` n `53` status `ready` deltaP `21.3558` edge `0.0874` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2262` n `53` status `ready` deltaP `25.7363` edge `0.2777` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1187` n `53` status `ready` deltaP `25.1412` edge `0.0344` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3053` n `53` status `ready` deltaP `17.176` edge `0.0244` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7843` n `53` status `ready` deltaP `17.7437` edge `0.0802` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
