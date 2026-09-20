# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T02:07:35.808543+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9116`

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

- `news_risk_high->crypto_major_24h` score `45.5592` n `77` status `ready` deltaP `20.6034` edge `3.7526` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `40.7644` n `77` status `ready` deltaP `31.7009` edge `3.3236` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `21.9009` n `96` status `ready` deltaP `-4.7256` edge `1.8799` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.7732` n `94` status `ready` deltaP `38.6673` edge `0.4425` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.5162` n `77` status `ready` deltaP `36.0277` edge `0.3904` maxDD `-0.0053`
- `news_risk_high->crypto_alt_4h` score `5.9522` n `98` status `ready` deltaP `22.8378` edge `0.4647` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.662` n `98` status `ready` deltaP `23.1427` edge `0.36` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.9642` n `96` status `ready` deltaP `36.2805` edge `0.1018` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2952` n `98` status `ready` deltaP `18.7737` edge `0.196` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.5337` n `98` status `ready` deltaP `20.8695` edge `0.1243` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.8972` n `97` status `ready` deltaP `21.9643` edge `0.0327` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.6208` n `77` status `ready` deltaP `22.9776` edge `0.0663` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1585` n `96` status `ready` deltaP `21.1128` edge `0.0026` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8199` n `98` status `ready` deltaP `19.1295` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7303` n `98` status `ready` deltaP `15.7552` edge `0.016` maxDD `-0.8144`
- `market_context_high->fx_24h` score `0.6866` n `94` status `ready` deltaP `11.957` edge `-0.0183` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.4877` n `97` status `ready` deltaP `9.5593` edge `0.0027` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3887` n `98` status `ready` deltaP `6.3669` edge `0.0305` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.0906` n `77` status `ready` deltaP `15.5394` edge `0.0386` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
