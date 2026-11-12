# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T00:07:32.736976+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11566`

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

- `market_context_high->unknown_4h` score `92.3115` n `88` status `ready` deltaP `8.3863` edge `7.6815` maxDD `-0.9161`
- `market_context_high->unknown_24h` score `63.2124` n `88` status `ready` deltaP `4.9937` edge `5.2485` maxDD `-0.4609`
- `news_risk_high->equity_24h` score `49.0173` n `37` status `ready` deltaP `36.8512` edge `3.8391` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `27.0595` n `37` status `ready` deltaP `50.6126` edge `2.1141` maxDD `-12.7247`
- `market_context_high->equity_24h` score `20.2727` n `88` status `ready` deltaP `19.8057` edge `1.7965` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `12.4728` n `37` status `ready` deltaP `26.2415` edge `1.0393` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.252` n `53` status `ready` deltaP `34.1199` edge `0.8224` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.1923` n `37` status `ready` deltaP `33.564` edge `0.3756` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.0048` n `37` status `ready` deltaP `39.9654` edge `0.3173` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.5735` n `88` status `ready` deltaP `34.9638` edge `1.1191` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.731` n `88` status `ready` deltaP `33.969` edge `0.2231` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.24` n `53` status `ready` deltaP `41.1998` edge `0.1163` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8015` n `88` status `ready` deltaP `19.9276` edge `0.2302` maxDD `-2.3671`
- `news_risk_high->crypto_major_4h` score `3.7248` n `53` status `ready` deltaP `20.4078` edge `0.3231` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6329` n `53` status `ready` deltaP `18.7634` edge `0.2489` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.6542` n `53` status `ready` deltaP `23.9892` edge `0.0866` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2248` n `53` status `ready` deltaP `21.0644` edge `0.0886` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0252` n `53` status `ready` deltaP `24.3927` edge `0.0316` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9946` n `53` status `ready` deltaP `23.8773` edge `0.2604` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3832` n `53` status `ready` deltaP `17.9245` edge `0.0259` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
