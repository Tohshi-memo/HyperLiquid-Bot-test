# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T05:07:34.547311+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3971`

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

- `market_context_high->unknown_1h` score `28743.5599` n `33` status `ready` deltaP `2.0232` edge `2395.2926` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3197.0573` n `31` status `ready` deltaP `3.3291` edge `266.4049` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `1738.2781` n `31` status `ready` deltaP `1.6322` edge `144.8632` maxDD `-0.7395`
- `news_risk_high->equity_24h` score `42.1219` n `31` status `ready` deltaP `48.2639` edge `3.1884` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.789` n `31` status `ready` deltaP `49.1319` edge `2.9882` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.289` n `31` status `ready` deltaP `48.4375` edge `2.5345` maxDD `0.0`
- `market_context_high->unknown_4h` score `19.3647` n `33` status `ready` deltaP `0.4943` edge `1.6243` maxDD `-0.7765`
- `news_risk_high->crypto_alt_4h` score `10.7451` n `31` status `ready` deltaP `26.3031` edge `0.8071` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.2804` n `31` status `ready` deltaP `34.8119` edge `0.6521` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.2433` n `31` status `ready` deltaP `37.2247` edge `0.6535` maxDD `-2.178`
- `news_risk_high->index_24h` score `6.8954` n `31` status `ready` deltaP `49.6528` edge `0.2436` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7726` n `31` status `ready` deltaP `17.2354` edge `0.8951` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5575` n `31` status `ready` deltaP `19.5383` edge `0.1849` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3376` n `31` status `ready` deltaP `36.1576` edge `0.0631` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6435` n `31` status `ready` deltaP `31.3937` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4275` n `31` status `ready` deltaP `9.7112` edge `0.2926` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2121` n `31` status `ready` deltaP `12.4058` edge `0.2366` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.2059` n `33` status `ready` deltaP `27.5684` edge `0.0285` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5001` n `31` status `ready` deltaP `29.433` edge `0.024` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
