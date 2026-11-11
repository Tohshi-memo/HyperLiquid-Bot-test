# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T07:52:26.560792+00:00`
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

- `market_context_high->unknown_4h` score `80.027` n `88` status `ready` deltaP `7.8298` edge `6.6615` maxDD `-0.9161`
- `market_context_high->equity_24h` score `33.7699` n `88` status `ready` deltaP `30.8712` edge `2.8475` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `13.0525` n `47` status `ready` deltaP `37.0816` edge `0.9527` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.6392` n `88` status `ready` deltaP `34.8485` edge `1.3847` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.0779` n `88` status `ready` deltaP `30.9817` edge `0.3462` maxDD `-2.3671`
- `market_context_high->metal_24h` score `3.9953` n `88` status `ready` deltaP `30.6818` edge `0.1837` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.8081` n `47` status `ready` deltaP `23.1286` edge `0.3119` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6081` n `52` status `ready` deltaP `17.8835` edge `0.2527` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5004` n `47` status `ready` deltaP `34.954` edge `0.0963` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.292` n `47` status `ready` deltaP `26.7417` edge `0.1214` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.0811` n `47` status `ready` deltaP `29.4726` edge `0.1039` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2646` n `47` status `ready` deltaP `27.6888` edge `0.2696` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5635` n `52` status `ready` deltaP `19.8065` edge `0.0237` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4063` n `52` status `ready` deltaP `18.3326` edge `0.0251` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7081` n `52` status `ready` deltaP `17.6531` edge `0.0465` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.558` n `52` status `ready` deltaP `17.8028` edge `0.0508` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.1432` n `52` status `ready` deltaP `-2.2455` edge `0.0365` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.3537` n `88` status `ready` deltaP `3.4363` edge `0.0` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.3844` n `88` status `ready` deltaP `3.1982` edge `0.0143` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6707` n `88` status `ready` deltaP `1.4274` edge `0.0151` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
