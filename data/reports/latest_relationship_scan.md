# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T11:07:31.517122+00:00`
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

- `news_risk_high->unknown_24h` score `48.6375` n `51` status `ready` deltaP `17.0139` edge `3.9397` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.9231` n `51` status `ready` deltaP `40.237` edge `0.9851` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.1751` n `51` status `ready` deltaP `24.2587` edge `0.9408` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.638` n `51` status `ready` deltaP `48.9481` edge `0.1587` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.7445` n `51` status `ready` deltaP `17.0834` edge `0.2286` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.677` n `51` status `ready` deltaP `26.4706` edge `0.207` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.1968` n `51` status `ready` deltaP `37.6255` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `1.8507` n `81` status `ready` deltaP `3.4337` edge `0.182` maxDD `-1.0533`
- `market_context_high->unknown_4h` score `1.7469` n `137` status `ready` deltaP `19.6502` edge `0.0554` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.402` n `51` status `ready` deltaP `31.7198` edge `-0.0904` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2074` n `51` status `ready` deltaP `16.5463` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9701` n `51` status `ready` deltaP `18.6421` edge `0.0365` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9593` n `51` status `ready` deltaP `14.0064` edge `0.0263` maxDD `-0.1788`
- `market_context_high->metal_4h` score `0.3019` n `137` status `ready` deltaP `12.0816` edge `-0.0095` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.252` n `51` status `ready` deltaP `9.4223` edge `0.0048` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1787` n `51` status `ready` deltaP `8.3891` edge `-0.0102` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0555` n `137` status `ready` deltaP `11.3728` edge `-0.0263` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.0983` n `51` status `ready` deltaP `2.4921` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1741` n `51` status `ready` deltaP `7.2155` edge `-0.0095` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.3691` n `137` status `ready` deltaP `-0.8141` edge `-0.0042` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
