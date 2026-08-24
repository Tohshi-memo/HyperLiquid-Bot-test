# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T10:22:28.427851+00:00`
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

- `news_risk_high->unknown_24h` score `48.9819` n `51` status `ready` deltaP `17.0139` edge `3.9684` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.0107` n `51` status `ready` deltaP `40.237` edge `0.9924` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.1367` n `51` status `ready` deltaP `24.2587` edge `0.9376` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.6632` n `51` status `ready` deltaP `48.9481` edge `0.1608` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.688` n `51` status `ready` deltaP `26.623` edge `0.2069` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6605` n `51` status `ready` deltaP `16.784` edge `0.2236` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.1968` n `51` status `ready` deltaP `37.6255` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `2.1951` n `81` status `ready` deltaP `3.4337` edge `0.2107` maxDD `-1.0533`
- `market_context_high->unknown_4h` score `1.7085` n `137` status `ready` deltaP `19.6502` edge `0.0522` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.4677` n `51` status `ready` deltaP `32.2406` edge `-0.0884` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2326` n `51` status `ready` deltaP `16.8457` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9662` n `51` status `ready` deltaP `18.6421` edge `0.036` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9471` n `51` status `ready` deltaP `13.854` edge `0.0263` maxDD `-0.1788`
- `market_context_high->metal_4h` score `0.2545` n `137` status `ready` deltaP `11.6243` edge `-0.0104` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2504` n `51` status `ready` deltaP `9.4223` edge `0.0046` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2063` n `51` status `ready` deltaP `8.6885` edge `-0.0099` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `-0.0285` n `137` status `ready` deltaP `11.0734` edge `-0.0313` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1061` n `51` status `ready` deltaP `2.3424` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2215` n `51` status `ready` deltaP `6.7582` edge `-0.0104` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.3769` n `137` status `ready` deltaP `-0.9638` edge `-0.0042` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
