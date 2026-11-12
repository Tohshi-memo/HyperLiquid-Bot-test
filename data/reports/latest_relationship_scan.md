# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T11:52:26.242306+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11644`

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

- `market_context_high->unknown_24h` score `285.1882` n `88` status `ready` deltaP `6.5508` edge `23.7361` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `105.2374` n `88` status `ready` deltaP `7.525` edge `8.7644` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.6599` n `53` status `ready` deltaP `21.0486` edge `2.2353` maxDD `-3.6503`
- `market_context_high->equity_24h` score `13.3342` n `88` status `ready` deltaP `14.9379` edge `1.2675` maxDD `-16.8057`
- `news_risk_high->crypto_major_24h` score `11.4014` n `53` status `ready` deltaP `36.8969` edge `1.4123` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.1676` n `53` status `ready` deltaP `33.9536` edge `0.8173` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.1426` n `53` status `ready` deltaP `41.5225` edge `0.3184` maxDD `0.0`
- `market_context_high->metal_24h` score `5.0421` n `88` status `ready` deltaP `35.0071` edge `0.2421` maxDD `-1.4245`
- `market_context_high->crypto_alt_24h` score `4.7756` n `88` status `ready` deltaP `34.9638` edge `0.8886` maxDD `-33.4213`
- `news_risk_high->metal_4h` score `4.5926` n `53` status `ready` deltaP `43.9571` edge `0.1273` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.9352` n `53` status `ready` deltaP `21.6579` edge `0.3323` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6238` n `53` status `ready` deltaP `18.0149` edge `0.2449` maxDD `-3.7082`
- `news_risk_high->index_24h` score `3.5697` n `53` status `ready` deltaP `19.129` edge `0.2003` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `2.9262` n `53` status `ready` deltaP `25.9492` edge `0.0962` maxDD `-0.3611`
- `market_context_high->index_24h` score `2.7052` n `88` status `ready` deltaP `16.8134` edge `0.1596` maxDD `-2.3671`
- `news_risk_high->metal_1h` score `2.1774` n `53` status `ready` deltaP `25.74` edge `0.0353` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1584` n `53` status `ready` deltaP `20.5937` edge `0.0862` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1495` n `53` status `ready` deltaP `25.4314` edge `0.2699` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3305` n `53` status `ready` deltaP `17.4754` edge `0.0245` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7917` n `53` status `ready` deltaP `18.9413` edge `0.0804` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
