# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T23:52:28.989447+00:00`
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

- `market_context_high->unknown_4h` score `92.3475` n `88` status `ready` deltaP `8.3863` edge `7.6845` maxDD `-0.9161`
- `market_context_high->unknown_24h` score `58.5012` n `88` status `ready` deltaP `4.9937` edge `4.8559` maxDD `-0.4609`
- `news_risk_high->equity_24h` score `49.2639` n `37` status `ready` deltaP `37.0242` edge `3.8585` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `27.1843` n `37` status `ready` deltaP `50.6126` edge `2.1245` maxDD `-12.7247`
- `market_context_high->equity_24h` score `20.5193` n `88` status `ready` deltaP `19.9787` edge `1.8159` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `12.57` n `37` status `ready` deltaP `26.2415` edge `1.0474` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.2388` n `53` status `ready` deltaP `34.1199` edge `0.8213` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.2398` n `37` status `ready` deltaP `33.737` edge `0.3784` maxDD `0.0`
- `news_risk_high->commodity_24h` score `6.9904` n `37` status `ready` deltaP `39.9654` edge `0.3161` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.6367` n `88` status `ready` deltaP `34.9638` edge `1.1272` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.7112` n `88` status `ready` deltaP `33.796` edge `0.2226` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2147` n `53` status `ready` deltaP `41.0478` edge `0.1152` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.849` n `88` status `ready` deltaP `20.1006` edge `0.233` maxDD `-2.3671`
- `news_risk_high->crypto_major_4h` score `3.7104` n `53` status `ready` deltaP `20.4078` edge `0.3219` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6389` n `53` status `ready` deltaP `18.7634` edge `0.2494` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.6723` n `53` status `ready` deltaP `24.1412` edge `0.0871` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.226` n `53` status `ready` deltaP `21.0644` edge `0.0887` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0097` n `53` status `ready` deltaP `24.243` edge `0.0313` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9837` n `53` status `ready` deltaP `23.8773` edge `0.259` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3844` n `53` status `ready` deltaP `17.9245` edge `0.026` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
