# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T07:04:50.087667+00:00`
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

- `news_risk_high->unknown_24h` score `43.919` n `51` status `ready` deltaP `3.9931` edge `3.6333` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8735` n `51` status `ready` deltaP `24.8685` edge `0.9116` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.6908` n `51` status `ready` deltaP `38.8481` edge `0.725` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.9223` n `51` status `ready` deltaP `47.9064` edge `0.106` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3366` n `51` status `ready` deltaP `16.4846` edge `0.1986` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.1983` n `51` status `ready` deltaP `37.778` edge `0.0281` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.8479` n `51` status `ready` deltaP `24.6413` edge `0.1501` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.8793` n `133` status `ready` deltaP `19.3105` edge `0.0687` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1559` n `51` status `ready` deltaP `15.9475` edge `0.007` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.762` n `51` status `ready` deltaP `16.696` edge `0.0228` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.5836` n `51` status `ready` deltaP `11.1101` edge `0.0143` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3741` n `51` status `ready` deltaP `10.0358` edge `-0.0049` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.041` n `51` status `ready` deltaP `5.8295` edge `0.0017` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0509` n `133` status `ready` deltaP `10.8234` edge `-0.0315` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.2189` n `51` status `ready` deltaP `0.2466` edge `-0.0074` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3299` n `51` status `ready` deltaP `5.5387` edge `-0.0113` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4818` n `133` status `ready` deltaP `1.7503` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6024` n `51` status `ready` deltaP `21.6503` edge `-0.1903` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7177` n `133` status `ready` deltaP `5.7893` edge `-0.0347` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.0993` n `133` status `ready` deltaP `-4.8737` edge `-0.0053` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
