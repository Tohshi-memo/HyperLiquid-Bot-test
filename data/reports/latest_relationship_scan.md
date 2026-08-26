# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T17:52:43.875537+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `47.0753` n `51` status `ready` deltaP `11.5717` edge `3.8458` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.3509` n `51` status `ready` deltaP `26.591` edge `0.8619` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `11.8236` n `51` status `ready` deltaP `34.5931` edge `0.7988` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.591` n `51` status `ready` deltaP `32.7847` edge `0.5071` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1889` n `51` status `ready` deltaP `41.9486` edge `0.0846` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.3455` n `51` status `ready` deltaP `39.5132` edge `0.0244` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.1428` n `137` status `ready` deltaP `25.1741` edge `0.1349` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7214` n `51` status `ready` deltaP `15.2724` edge `0.1605` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.0678` n `51` status `ready` deltaP `31.3725` edge `-0.0326` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.6127` n `51` status `ready` deltaP `19.5662` edge `0.081` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.2062` n `51` status `ready` deltaP `16.696` edge `0.0062` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1663` n `137` status `ready` deltaP `12.2525` edge `0.0604` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `1.1586` n `51` status `ready` deltaP `15.8125` edge `0.0192` maxDD `-0.2455`
- `news_risk_high->commodity_1h` score `0.4211` n `51` status `ready` deltaP `12.8948` edge `-0.0007` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1481` n `51` status `ready` deltaP `6.9267` edge `0.0059` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.0425` n `51` status `ready` deltaP `5.6945` edge `0.0017` maxDD `-0.0709`
- `news_risk_high->metal_1h` score `0.0077` n `51` status `ready` deltaP `4.0038` edge `-0.0031` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0199` n `51` status `ready` deltaP `8.0931` edge `-0.0025` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4185` n `137` status `ready` deltaP `3.0421` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->unknown_24h` score `-0.775` n `133` status `ready` deltaP `5.5567` edge `-0.0289` maxDD `-3.1513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
