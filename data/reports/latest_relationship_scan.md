# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T15:53:03.766312+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `45.4265` n `53` status `ready` deltaP `11.5717` edge `3.7084` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.3316` n `53` status `ready` deltaP `25.7508` edge `0.8659` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `12.1389` n `53` status `ready` deltaP `33.3594` edge `0.8333` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.9368` n `53` status `ready` deltaP `29.6771` edge `0.4733` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9526` n `53` status `ready` deltaP `39.3098` edge `0.0825` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.0255` n `53` status `ready` deltaP `36.4131` edge `0.0228` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.9198` n `137` status `ready` deltaP `24.1119` edge `0.1234` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.8736` n `53` status `ready` deltaP `16.1545` edge `0.1673` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `1.944` n `53` status `ready` deltaP `30.0648` edge `-0.0342` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.8156` n `53` status `ready` deltaP `20.3024` edge `0.093` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.186` n `137` status `ready` deltaP `12.3947` edge `0.0611` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.1609` n `53` status `ready` deltaP `16.16` edge `0.006` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4894` n `53` status `ready` deltaP `13.4775` edge `0.0093` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3757` n `53` status `ready` deltaP `10.3029` edge `-0.0061` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1542` n `53` status `ready` deltaP `6.8973` edge `0.0066` maxDD `-0.1788`
- `news_risk_high->metal_4h` score `0.0244` n `53` status `ready` deltaP `8.1369` edge `0.0009` maxDD `-0.249`
- `news_risk_high->index_1h` score `-0.0579` n `53` status `ready` deltaP `4.0942` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.1668` n `53` status `ready` deltaP `2.0105` edge `-0.0047` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.406` n `137` status `ready` deltaP `3.283` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.96` n `137` status `ready` deltaP `5.1759` edge `-0.0273` maxDD `-2.9763`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
