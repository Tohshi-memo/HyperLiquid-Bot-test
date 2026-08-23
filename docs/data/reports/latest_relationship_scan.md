# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T06:22:29.386313+00:00`
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

- `news_risk_high->unknown_4h` score `15.9463` n `47` status `ready` deltaP `26.3784` edge `1.1576` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `5.0693` n `33` status `ready` deltaP `-7.2808` edge `0.7433` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.0693` n `33` status `ready` deltaP `-7.2808` edge `0.7433` maxDD `-1.5876`
- `news_risk_high->equity_4h` score `4.0909` n `47` status `ready` deltaP `31.4543` edge `0.1808` maxDD `-1.3003`
- `news_risk_high->unknown_1h` score `3.8366` n `51` status `ready` deltaP `20.5266` edge `0.2133` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.9403` n `47` status `ready` deltaP `35.0934` edge `0.0245` maxDD `-0.0746`
- `news_risk_high->fx_1h` score `1.2098` n `51` status `ready` deltaP `16.696` edge `0.0065` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.1434` n `47` status `ready` deltaP `16.5737` edge `0.0234` maxDD `-0.0884`
- `market_context_high->unknown_1h` score `0.9847` n `135` status `ready` deltaP `5.5811` edge `0.0897` maxDD `-1.5876`
- `news_risk_high->equity_1h` score `0.8672` n `51` status `ready` deltaP `18.6421` edge `0.0234` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.7113` n `127` status `ready` deltaP `22.2069` edge `-0.0716` maxDD `-0.3736`
- `news_risk_high->metal_4h` score `0.7021` n `47` status `ready` deltaP `15.0233` edge `-0.0065` maxDD `-0.1449`
- `risk_on_high->fx_1h` score `0.2387` n `33` status `ready` deltaP `6.7139` edge `0.0035` maxDD `-0.0796`
- `risk_on_and_context->fx_1h` score `0.2387` n `33` status `ready` deltaP `6.7139` edge `0.0035` maxDD `-0.0796`
- `news_risk_high->index_1h` score `0.2317` n `51` status `ready` deltaP `9.2726` edge `0.0032` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1608` n `51` status `ready` deltaP `8.2394` edge `-0.0107` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1376` n `127` status `ready` deltaP `7.9364` edge `0.0088` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `-0.0765` n `51` status `ready` deltaP `2.9412` edge `-0.0071` maxDD `-0.1184`
- `risk_on_high->index_1h` score `-0.1386` n `33` status `ready` deltaP `-1.0661` edge `0.0075` maxDD `-0.1197`
- `risk_on_and_context->index_1h` score `-0.1386` n `33` status `ready` deltaP `-1.0661` edge `0.0075` maxDD `-0.1197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
