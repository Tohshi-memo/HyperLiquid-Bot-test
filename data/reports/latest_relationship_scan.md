# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T09:07:28.406784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11722`

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

- `market_context_high->unknown_4h` score `81.7442` n `88` status `ready` deltaP `7.8298` edge `6.8046` maxDD `-0.9161`
- `market_context_high->equity_24h` score `33.2757` n `88` status `ready` deltaP `30.0031` edge `2.8121` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `13.1089` n `47` status `ready` deltaP `37.0816` edge `0.9574` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.8138` n `88` status `ready` deltaP `35.7165` edge `1.4013` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.9784` n `88` status `ready` deltaP `30.1136` edge `0.3437` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.1197` n `88` status `ready` deltaP `31.2026` edge `0.1906` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.9444` n `47` status `ready` deltaP `23.7383` edge `0.3192` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6129` n `52` status `ready` deltaP `17.8835` edge `0.2531` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5076` n `47` status `ready` deltaP `34.954` edge `0.0969` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.2278` n `47` status `ready` deltaP `26.2844` edge `0.1191` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1015` n `47` status `ready` deltaP `29.4726` edge `0.1056` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.3869` n `47` status `ready` deltaP `28.451` edge `0.2802` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5959` n `52` status `ready` deltaP `20.1059` edge `0.0244` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4111` n `52` status `ready` deltaP `18.3326` edge `0.0255` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7729` n `52` status `ready` deltaP `18.1022` edge `0.0489` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.5806` n `52` status `ready` deltaP `17.9525` edge `0.0527` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.1732` n `52` status `ready` deltaP `-2.5449` edge `0.036` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.352` n `88` status `ready` deltaP `3.4976` edge `0.015` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3731` n `88` status `ready` deltaP `3.1369` edge `-0.0005` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7125` n `88` status `ready` deltaP `0.9701` edge `0.0128` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
