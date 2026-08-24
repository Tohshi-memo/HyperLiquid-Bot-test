# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T10:37:28.482274+00:00`
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

- `news_risk_high->unknown_24h` score `48.2431` n `51` status `ready` deltaP `18.9236` edge `3.8941` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0454` n `51` status `ready` deltaP `25.6307` edge `0.921` maxDD `-0.0473`
- `news_risk_high->equity_24h` score `12.5646` n `51` status `ready` deltaP `36.9383` edge `0.8907` maxDD `-4.5256`
- `news_risk_high->index_24h` score `5.6536` n `51` status `ready` deltaP `48.9481` edge `0.16` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.6416` n `51` status `ready` deltaP `16.784` edge `0.2219` maxDD `-0.7596`
- `news_risk_high->equity_4h` score `3.4446` n `51` status `ready` deltaP `25.8608` edge `0.1903` maxDD `-2.0521`
- `news_risk_high->fx_4h` score `3.1968` n `51` status `ready` deltaP `37.6255` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `1.8428` n `81` status `ready` deltaP `4.1088` edge `0.1989` maxDD `-1.8181`
- `market_context_high->unknown_4h` score `1.6615` n `137` status `ready` deltaP `20.2922` edge `0.0496` maxDD `-0.7137`
- `news_risk_high->metal_24h` score `1.4454` n `51` status `ready` deltaP `32.067` edge `-0.0891` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2194` n `51` status `ready` deltaP `16.696` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->index_4h` score `0.9459` n `51` status `ready` deltaP `13.854` edge `0.0262` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.8405` n `51` status `ready` deltaP `16.8311` edge `0.0314` maxDD `-0.8678`
- `market_context_high->metal_4h` score `0.2703` n `137` status `ready` deltaP `11.7767` edge `-0.0101` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2504` n `51` status `ready` deltaP `9.4223` edge `0.0046` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2063` n `51` status `ready` deltaP `8.6885` edge `-0.0099` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `-0.1061` n `51` status `ready` deltaP `2.3424` edge `-0.0069` maxDD `-0.1184`
- `market_context_high->unknown_1h` score `-0.1686` n `137` status `ready` deltaP `8.8837` edge `-0.0286` maxDD `-1.5738`
- `news_risk_high->metal_4h` score `-0.2057` n `51` status `ready` deltaP `6.9106` edge `-0.0101` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.3769` n `137` status `ready` deltaP `-0.9638` edge `-0.0042` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
