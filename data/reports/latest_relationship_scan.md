# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T02:07:37.667673+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3899`

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

- `market_context_high->unknown_1h` score `32131.5627` n `45` status `ready` deltaP `1.2674` edge `2677.6312` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22762.9824` n `45` status `ready` deltaP `2.1105` edge `1896.915` maxDD `-0.7765`
- `news_risk_high->unknown_4h` score `1510.0349` n `31` status `ready` deltaP `3.3291` edge `125.8197` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `896.6077` n `31` status `ready` deltaP `1.4825` edge `74.725` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `82.5445` n `31` status `ready` deltaP `6.0764` edge `6.8382` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.2566` n `31` status `ready` deltaP `50.3472` edge `3.3524` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.2084` n `31` status `ready` deltaP `51.2153` edge `3.0926` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.1573` n `31` status `ready` deltaP `50.5208` edge `2.6763` maxDD `0.0`
- `news_risk_high->metal_24h` score `10.9894` n `31` status `ready` deltaP `36.8952` edge `0.6973` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8631` n `31` status `ready` deltaP `26.6079` edge `0.8149` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.1941` n `31` status `ready` deltaP `37.2247` edge `0.6494` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.2217` n `31` status `ready` deltaP `51.7361` edge `0.2569` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7382` n `31` status `ready` deltaP `17.2354` edge `0.8907` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2877` n `31` status `ready` deltaP `45.0101` edge `0.1534` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5563` n `31` status `ready` deltaP `19.688` edge `0.1838` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3148` n `31` status `ready` deltaP `36.1576` edge `0.0612` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6375` n `31` status `ready` deltaP `31.3937` edge `0.019` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3854` n `31` status `ready` deltaP `9.7112` edge `0.2872` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3717` n `45` status `ready` deltaP `29.3259` edge `0.0306` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.1879` n `31` status `ready` deltaP `12.4058` edge `0.2335` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
