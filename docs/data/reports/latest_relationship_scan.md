# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T05:52:31.372785+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3983`

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

- `news_risk_high->unknown_1h` score `3218.7061` n `31` status `ready` deltaP `1.6322` edge `268.2322` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3208.5091` n `31` status `ready` deltaP `3.4815` edge `267.3582` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `88.4142` n `31` status `ready` deltaP `1.6322` edge `7.3664` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `41.5222` n `31` status `ready` deltaP `47.7431` edge `3.1419` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.3789` n `31` status `ready` deltaP `48.6111` edge `2.9575` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.8501` n `31` status `ready` deltaP `47.9167` edge `2.5014` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7811` n `31` status `ready` deltaP `26.3031` edge `0.8101` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.3155` n `31` status `ready` deltaP `37.3771` edge `0.6585` maxDD `-2.178`
- `news_risk_high->metal_24h` score `10.0695` n `31` status `ready` deltaP `34.291` edge `0.638` maxDD `-0.1986`
- `news_risk_high->index_24h` score `6.8058` n `31` status `ready` deltaP `49.1319` edge `0.2396` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7796` n `31` status `ready` deltaP `17.2354` edge `0.896` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6355` n `31` status `ready` deltaP `19.9874` edge `0.1884` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3606` n `31` status `ready` deltaP `36.31` edge `0.064` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6614` n `31` status `ready` deltaP `31.5434` edge `0.02` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4501` n `31` status `ready` deltaP `9.8609` edge `0.2945` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2409` n `31` status `ready` deltaP `12.7052` edge `0.2383` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.0898` n `31` status `ready` deltaP `26.6572` edge `0.0249` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.49` n `31` status `ready` deltaP `29.2833` edge `0.0237` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0882` n `31` status `ready` deltaP `16.6257` edge `0.0844` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
