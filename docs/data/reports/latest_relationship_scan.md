# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T07:37:28.680613+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11728`

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

- `market_context_high->unknown_4h` score `79.8266` n `88` status `ready` deltaP `7.8298` edge `6.6448` maxDD `-0.9161`
- `market_context_high->equity_24h` score `33.8714` n `88` status `ready` deltaP `31.0448` edge `2.8548` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `13.0357` n `47` status `ready` deltaP `37.0816` edge `0.9513` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.5966` n `88` status `ready` deltaP `34.6749` edge `1.3804` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.099` n `88` status `ready` deltaP `31.1553` edge `0.3468` maxDD `-2.3671`
- `market_context_high->metal_24h` score `3.9797` n `88` status `ready` deltaP `30.6818` edge `0.1824` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.7755` n `47` status `ready` deltaP `22.9761` edge `0.3102` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6093` n `52` status `ready` deltaP `17.8835` edge `0.2528` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.4968` n `47` status `ready` deltaP `34.954` edge `0.096` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.3102` n `47` status `ready` deltaP `26.8941` edge `0.1219` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.0775` n `47` status `ready` deltaP `29.4726` edge `0.1036` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2387` n `47` status `ready` deltaP `27.5363` edge `0.2673` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5635` n `52` status `ready` deltaP `19.8065` edge `0.0237` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3931` n `52` status `ready` deltaP `18.1829` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7093` n `52` status `ready` deltaP `17.6531` edge `0.0466` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.5557` n `52` status `ready` deltaP `17.8028` edge `0.0505` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.1564` n `52` status `ready` deltaP `-2.3952` edge `0.0364` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.3622` n `88` status `ready` deltaP `3.2866` edge `-0.0001` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.3844` n `88` status `ready` deltaP `3.1982` edge `0.0143` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6589` n `88` status `ready` deltaP `1.5798` edge `0.0156` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
