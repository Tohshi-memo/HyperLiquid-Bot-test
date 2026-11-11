# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T06:52:25.136382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11726`

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

- `market_context_high->unknown_4h` score `79.3294` n `88` status `ready` deltaP `7.525` edge `6.6054` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.1711` n `88` status `ready` deltaP `31.5656` edge `2.8763` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.9901` n `47` status `ready` deltaP `37.0816` edge `0.9475` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.4627` n `88` status `ready` deltaP `34.154` edge `1.3667` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1598` n `88` status `ready` deltaP `31.6761` edge `0.3484` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.9605` n `50` status `ready` deltaP `20.3533` edge `0.2656` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.9142` n `88` status `ready` deltaP `30.5082` edge `0.1781` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.6693` n `47` status `ready` deltaP `22.5188` edge `0.3044` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.4884` n `47` status `ready` deltaP `34.954` edge `0.0953` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.3028` n `47` status `ready` deltaP `26.7417` edge `0.1223` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.0667` n `47` status `ready` deltaP `29.4726` edge `0.1027` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1518` n `47` status `ready` deltaP `27.079` edge `0.2592` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.5967` n `50` status `ready` deltaP `20.503` edge `0.0265` maxDD `-0.4103`
- `news_risk_high->metal_1h` score `1.4808` n `50` status `ready` deltaP `18.8024` edge `0.0235` maxDD `-0.3692`
- `news_risk_high->crypto_alt_1h` score `0.8177` n `50` status `ready` deltaP `19.8922` edge `0.066` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6883` n `50` status `ready` deltaP `19.8922` edge `0.0608` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `0.0145` n `50` status `ready` deltaP `-0.8443` edge `0.0403` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3748` n `88` status `ready` deltaP `3.3479` edge `0.0141` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3911` n `88` status `ready` deltaP `2.8375` edge `-0.0008` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6637` n `88` status `ready` deltaP `1.4274` edge `0.016` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
