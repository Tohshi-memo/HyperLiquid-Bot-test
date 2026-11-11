# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T04:37:37.908411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11742`

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

- `market_context_high->unknown_4h` score `79.1158` n `88` status `ready` deltaP `7.525` edge `6.5876` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.5038` n `88` status `ready` deltaP `32.2601` edge `2.8994` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.5722` n `38` status `ready` deltaP `34.0581` edge `0.8495` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.883` n `88` status `ready` deltaP `32.5915` edge `1.3028` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1641` n `88` status `ready` deltaP `31.8497` edge `0.3476` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8642` n `47` status `ready` deltaP `20.544` edge `0.2563` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.4292` n `88` status `ready` deltaP `28.9457` edge `0.1481` maxDD `-1.4245`
- `news_risk_high->commodity_4h` score `3.2844` n `38` status `ready` deltaP `24.4865` edge `0.1358` maxDD `-0.3611`
- `news_risk_high->metal_4h` score `2.6974` n `38` status `ready` deltaP `31.4265` edge `0.0529` maxDD `-1.0104`
- `news_risk_high->index_4h` score `2.5306` n `38` status `ready` deltaP `25.4413` edge `0.0849` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.3352` n `38` status `ready` deltaP `29.4367` edge `0.267` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.8191` n `38` status `ready` deltaP `18.9104` edge `0.2559` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `1.6069` n `47` status `ready` deltaP `20.8434` edge `0.0204` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4477` n `47` status `ready` deltaP `18.8655` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1212` n `47` status `ready` deltaP `22.9074` edge `0.0848` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7897` n `47` status `ready` deltaP `21.2288` edge `0.0649` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2092` n `47` status `ready` deltaP `-4.2075` edge `0.0347` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.4168` n `88` status `ready` deltaP `2.5381` edge `-0.0021` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4504` n `88` status `ready` deltaP `3.0485` edge `0.0098` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6714` n `88` status `ready` deltaP `1.5798` edge `0.014` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
