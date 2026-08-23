# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T06:57:42.829612+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `news_risk_high->unknown_4h` score `15.3016` n `49` status `ready` deltaP `26.4653` edge `1.1033` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `5.0483` n `33` status `ready` deltaP `-7.5802` edge `0.7426` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.0483` n `33` status `ready` deltaP `-7.5802` edge `0.7426` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.8043` n `51` status `ready` deltaP `20.2272` edge `0.2126` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `3.4986` n `49` status `ready` deltaP `28.2198` edge `0.1673` maxDD `-1.7772`
- `news_risk_high->fx_4h` score `2.795` n `49` status `ready` deltaP `33.4868` edge `0.0231` maxDD `-0.0746`
- `news_risk_high->fx_1h` score `1.2218` n `51` status `ready` deltaP `16.8457` edge `0.0065` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1117` n `135` status `ready` deltaP `6.7632` edge `0.0924` maxDD `-1.5876`
- `news_risk_high->index_4h` score `0.9243` n `49` status `ready` deltaP `14.1208` edge `0.0218` maxDD `-0.1132`
- `news_risk_high->equity_1h` score `0.8757` n `51` status `ready` deltaP `18.7918` edge `0.0235` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.7284` n `125` status `ready` deltaP `22.1061` edge `-0.0695` maxDD `-0.3736`
- `news_risk_high->metal_4h` score `0.3557` n `49` status `ready` deltaP `12.3756` edge `-0.0086` maxDD `-0.2079`
- `news_risk_high->index_1h` score `0.248` n `51` status `ready` deltaP `9.572` edge `0.0033` maxDD `-0.1583`
- `risk_on_high->fx_1h` score `0.2464` n `33` status `ready` deltaP `6.8636` edge `0.0035` maxDD `-0.0796`
- `risk_on_and_context->fx_1h` score `0.2464` n `33` status `ready` deltaP `6.8636` edge `0.0035` maxDD `-0.0796`
- `market_context_high->fx_4h` score `0.1556` n `125` status `ready` deltaP `8.1317` edge `0.009` maxDD `-0.3527`
- `news_risk_high->commodity_1h` score `0.1356` n `51` status `ready` deltaP `7.94` edge `-0.0108` maxDD `-0.4666`
- `market_context_high->commodity_24h` score `0.1054` n `109` status `ready` deltaP `-0.5893` edge `0.0955` maxDD `-2.2898`
- `news_risk_high->metal_1h` score `-0.0765` n `51` status `ready` deltaP `2.9412` edge `-0.0071` maxDD `-0.1184`
- `risk_on_high->index_1h` score `-0.1223` n `33` status `ready` deltaP `-0.7667` edge `0.0076` maxDD `-0.1197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
