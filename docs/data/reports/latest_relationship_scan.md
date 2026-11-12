# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T01:07:26.870515+00:00`
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

- `market_context_high->unknown_4h` score `94.2706` n `88` status `ready` deltaP `8.4396` edge `7.8444` maxDD `-0.9161`
- `market_context_high->unknown_24h` score `82.3812` n `88` status `ready` deltaP `4.9937` edge `6.8459` maxDD `-0.4609`
- `news_risk_high->equity_24h` score `45.8695` n `40` status `ready` deltaP `36.1592` edge `3.5814` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `26.0694` n `40` status `ready` deltaP `50.026` edge `2.0355` maxDD `-12.7247`
- `market_context_high->equity_24h` score `19.2633` n `88` status `ready` deltaP `19.1137` edge `1.717` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.2411` n `53` status `ready` deltaP `33.9536` edge `0.8226` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.8332` n `40` status `ready` deltaP `39.9654` edge `0.303` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.831` n `40` status `ready` deltaP `21.782` edge `0.9054` maxDD `-10.9876`
- `news_risk_high->index_24h` score `6.8094` n `40` status `ready` deltaP `32.872` edge `0.3483` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.3185` n `88` status `ready` deltaP `34.9638` edge `1.0864` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.7846` n `88` status `ready` deltaP `34.488` edge `0.2241` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3003` n `53` status `ready` deltaP `41.5181` edge `0.1192` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8152` n `53` status `ready` deltaP `20.7433` edge `0.3284` maxDD `-9.2335`
- `market_context_high->index_24h` score `3.613` n `88` status `ready` deltaP `19.2356` edge `0.2191` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.5897` n `53` status `ready` deltaP `18.6137` edge `0.2463` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.6186` n `53` status `ready` deltaP `23.815` edge `0.0848` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.202` n `53` status `ready` deltaP `20.8985` edge `0.0878` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0682` n `53` status `ready` deltaP `24.2119` edge `0.2676` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.0252` n `53` status `ready` deltaP `24.3927` edge `0.0316` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3509` n `53` status `ready` deltaP `17.6251` edge `0.0252` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
