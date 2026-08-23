# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T06:07:30.419917+00:00`
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

- `news_risk_high->unknown_4h` score `16.2102` n `46` status `ready` deltaP `26.3322` edge `1.1799` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `5.0553` n `33` status `ready` deltaP `-7.2808` edge `0.7415` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.0553` n `33` status `ready` deltaP `-7.2808` edge `0.7415` maxDD `-1.5876`
- `news_risk_high->equity_4h` score `4.4039` n `46` status `ready` deltaP `33.1058` edge `0.1884` maxDD `-1.0358`
- `news_risk_high->unknown_1h` score `3.815` n `51` status `ready` deltaP `20.5266` edge `0.2115` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.9266` n `46` status `ready` deltaP `34.8621` edge `0.0249` maxDD `-0.0746`
- `news_risk_high->index_4h` score `1.2519` n `46` status `ready` deltaP `17.8089` edge `0.0242` maxDD `-0.0884`
- `news_risk_high->fx_1h` score `1.2098` n `51` status `ready` deltaP `16.696` edge `0.0065` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0699` n `135` status `ready` deltaP `5.5811` edge `0.0968` maxDD `-1.5876`
- `news_risk_high->metal_4h` score `0.883` n `46` status `ready` deltaP `16.4435` edge `-0.0054` maxDD `-0.1177`
- `market_context_high->unknown_4h` score `0.8712` n `128` status `ready` deltaP `22.2561` edge `-0.0586` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.857` n `51` status `ready` deltaP `18.4924` edge `0.0231` maxDD `-0.9204`
- `risk_on_high->fx_1h` score `0.2387` n `33` status `ready` deltaP `6.7139` edge `0.0035` maxDD `-0.0796`
- `risk_on_and_context->fx_1h` score `0.2387` n `33` status `ready` deltaP `6.7139` edge `0.0035` maxDD `-0.0796`
- `news_risk_high->index_1h` score `0.2231` n `51` status `ready` deltaP `9.1229` edge `0.0031` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1739` n `51` status `ready` deltaP `8.3891` edge `-0.0106` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1612` n `128` status `ready` deltaP `8.2317` edge `0.0088` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `-0.0843` n `51` status `ready` deltaP `2.7915` edge `-0.0071` maxDD `-0.1184`
- `risk_on_high->index_1h` score `-0.1472` n `33` status `ready` deltaP `-1.2158` edge `0.0074` maxDD `-0.1197`
- `risk_on_and_context->index_1h` score `-0.1472` n `33` status `ready` deltaP `-1.2158` edge `0.0074` maxDD `-0.1197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
