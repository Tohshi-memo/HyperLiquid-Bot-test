# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T10:50:12.330922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `48.7659` n `51` status `ready` deltaP `17.0139` edge `3.9504` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.9447` n `51` status `ready` deltaP `40.237` edge `0.9869` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.1799` n `51` status `ready` deltaP `24.2587` edge `0.9412` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.6452` n `51` status `ready` deltaP `48.9481` edge `0.1593` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.7289` n `51` status `ready` deltaP `16.9337` edge `0.2283` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.6565` n `51` status `ready` deltaP `26.3182` edge `0.2063` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.1847` n `51` status `ready` deltaP `37.4731` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `1.9791` n `81` status `ready` deltaP `3.4337` edge `0.1927` maxDD `-1.0533`
- `market_context_high->unknown_4h` score `1.7517` n `137` status `ready` deltaP `19.6502` edge `0.0558` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.4231` n `51` status `ready` deltaP `31.8934` edge `-0.0898` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2074` n `51` status `ready` deltaP `16.5463` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9654` n `51` status `ready` deltaP `18.6421` edge `0.0359` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9459` n `51` status `ready` deltaP `13.854` edge `0.0262` maxDD `-0.1788`
- `market_context_high->metal_4h` score `0.2861` n `137` status `ready` deltaP `11.9291` edge `-0.0098` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2504` n `51` status `ready` deltaP `9.4223` edge `0.0046` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1919` n `51` status `ready` deltaP `8.5388` edge `-0.0101` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0399` n `137` status `ready` deltaP `11.2231` edge `-0.0266` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.0983` n `51` status `ready` deltaP `2.4921` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1899` n `51` status `ready` deltaP `7.063` edge `-0.0098` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.3691` n `137` status `ready` deltaP `-0.8141` edge `-0.0042` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
