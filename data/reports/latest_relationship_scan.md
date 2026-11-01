# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T01:37:27.174564+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6231`

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

- `market_context_high->unknown_24h` score `4480.0869` n `76` status `ready` deltaP `-8.8451` edge `373.4328` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `180.7605` n `76` status `ready` deltaP `1.1955` edge `15.0687` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `78.4288` n `108` status `ready` deltaP `-5.1951` edge `6.599` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.7769` n `92` status `ready` deltaP `35.0921` edge `1.1148` maxDD `-6.3871`
- `market_context_high->equity_24h` score `11.9589` n `76` status `ready` deltaP `23.1359` edge `1.0868` maxDD `-12.5572`
- `news_risk_high->crypto_alt_4h` score `5.504` n `108` status `ready` deltaP `20.7317` edge `0.4591` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.3112` n `76` status `ready` deltaP `46.2171` edge `0.1528` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.6119` n `76` status `ready` deltaP `26.1232` edge `0.0769` maxDD `-0.3387`
- `market_context_high->fx_1h` score `0.9557` n `76` status `ready` deltaP `14.7101` edge `0.0` maxDD `-0.1407`
- `news_risk_high->crypto_alt_1h` score `0.8361` n `108` status `ready` deltaP `8.727` edge `0.1069` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.701` n `76` status `ready` deltaP `13.4788` edge `0.0425` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.6122` n `76` status `ready` deltaP `8.9741` edge `0.0202` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.5776` n `76` status `ready` deltaP `12.7407` edge `0.0023` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.214` n `76` status `ready` deltaP `0.4491` edge `0.112` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.1247` n `76` status `ready` deltaP `-5.8167` edge `0.1941` maxDD `-4.48`
- `market_context_high->commodity_24h` score `-0.0034` n `76` status `ready` deltaP `24.068` edge `0.0846` maxDD `-12.639`
- `market_context_high->crypto_major_1h` score `-0.1927` n `76` status `ready` deltaP `1.9146` edge `0.0653` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.2896` n `76` status `ready` deltaP `1.3788` edge `0.0181` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.6779` n `108` status `ready` deltaP `4.0031` edge `-0.0032` maxDD `-1.3981`
- `market_context_high->index_1h` score `-0.7311` n `76` status `ready` deltaP `-1.0164` edge `0.0017` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
