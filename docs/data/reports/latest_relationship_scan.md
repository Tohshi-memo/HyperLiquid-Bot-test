# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T23:07:28.843337+00:00`
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

- `market_context_high->unknown_4h` score `92.1459` n `88` status `ready` deltaP `8.3863` edge `7.6677` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `51.3287` n `35` status `ready` deltaP `37.5433` edge `4.0271` maxDD `0.0`
- `market_context_high->unknown_24h` score `44.4204` n `88` status `ready` deltaP `4.9937` edge `3.6825` maxDD `-0.4609`
- `news_risk_high->crypto_major_24h` score `28.5648` n `35` status `ready` deltaP `54.4736` edge `2.2138` maxDD `-12.7247`
- `market_context_high->equity_24h` score `21.2641` n `88` status `ready` deltaP `20.4978` edge `1.8745` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `14.2386` n `35` status `ready` deltaP `29.6391` edge `1.1638` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.1884` n `53` status `ready` deltaP `34.1199` edge `0.8171` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.4685` n `35` status `ready` deltaP `34.2561` edge `0.394` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.0876` n `35` status `ready` deltaP `39.9654` edge `0.3242` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.8005` n `88` status `ready` deltaP `34.9638` edge `1.1482` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.6553` n `88` status `ready` deltaP `33.277` edge `0.2214` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.147` n `53` status `ready` deltaP `40.5919` edge `0.1126` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.9913` n `88` status `ready` deltaP `20.6197` edge `0.2414` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.6233` n `53` status `ready` deltaP `18.7634` edge `0.2481` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.6081` n `53` status `ready` deltaP `20.1038` edge `0.3154` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.7075` n `53` status `ready` deltaP `24.4452` edge `0.088` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2272` n `53` status `ready` deltaP `21.0644` edge `0.0888` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9809` n `53` status `ready` deltaP `23.9436` edge `0.0309` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9259` n `53` status `ready` deltaP `23.7254` edge `0.2526` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3832` n `53` status `ready` deltaP `17.9245` edge `0.0259` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
