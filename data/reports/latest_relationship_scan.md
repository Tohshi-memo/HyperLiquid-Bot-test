# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T09:52:28.457440+00:00`
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

- `news_risk_high->unknown_24h` score `49.2075` n `51` status `ready` deltaP `17.0139` edge `3.9872` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.0767` n `51` status `ready` deltaP `40.237` edge `0.9979` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0755` n `51` status `ready` deltaP `24.2587` edge `0.9325` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.68` n `51` status `ready` deltaP `48.9481` edge `0.1622` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7256` n `51` status `ready` deltaP `26.9279` edge `0.208` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5897` n `51` status `ready` deltaP `16.784` edge `0.2177` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2103` n `51` status `ready` deltaP `37.778` edge `0.0291` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `2.0715` n `82` status `ready` deltaP `3.5993` edge `0.1993` maxDD `-1.0533`
- `market_context_high->unknown_4h` score `1.7807` n `138` status `ready` deltaP `19.6978` edge `0.0579` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.5122` n `51` status `ready` deltaP `32.5878` edge `-0.087` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2578` n `51` status `ready` deltaP `17.1451` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9654` n `51` status `ready` deltaP `18.6421` edge `0.0359` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9471` n `51` status `ready` deltaP `13.854` edge `0.0263` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2504` n `51` status `ready` deltaP `9.4223` edge `0.0046` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.2478` n `138` status `ready` deltaP `11.5257` edge `-0.0103` maxDD `-1.3378`
- `news_risk_high->commodity_1h` score `0.2207` n `51` status `ready` deltaP `8.8382` edge `-0.0097` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0703` n `138` status `ready` deltaP `11.2427` edge `-0.0242` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1053` n `51` status `ready` deltaP `2.3424` edge `-0.0068` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2483` n `51` status `ready` deltaP `6.4533` edge `-0.0106` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4402` n `138` status `ready` deltaP `2.354` edge `0.0011` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
