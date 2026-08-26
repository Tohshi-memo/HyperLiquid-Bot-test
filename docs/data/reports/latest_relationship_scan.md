# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T16:22:30.238666+00:00`
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

- `news_risk_high->unknown_24h` score `45.5045` n `53` status `ready` deltaP `11.5717` edge `3.7149` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.5121` n `53` status `ready` deltaP `33.7048` edge `0.8621` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.3715` n `53` status `ready` deltaP `26.0543` edge `0.8672` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `6.9416` n `53` status `ready` deltaP `29.6771` edge `0.4737` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9502` n `53` status `ready` deltaP `39.3098` edge `0.0823` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.0255` n `53` status `ready` deltaP `36.4131` edge `0.0228` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.9597` n `137` status `ready` deltaP `24.4154` edge `0.1247` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.8747` n `53` status `ready` deltaP `16.2592` edge `0.1667` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.0028` n `53` status `ready` deltaP `30.4103` edge `-0.0316` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.8349` n `53` status `ready` deltaP `20.4541` edge `0.0936` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.1872` n `137` status `ready` deltaP `12.4994` edge `0.0605` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.1601` n `53` status `ready` deltaP `16.1491` edge `0.006` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5047` n `53` status `ready` deltaP `13.608` edge `0.0104` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3876` n `53` status `ready` deltaP `10.4521` edge `-0.0061` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.153` n `53` status `ready` deltaP `6.8973` edge `0.0065` maxDD `-0.1788`
- `news_risk_high->metal_4h` score `0.0679` n `53` status `ready` deltaP `8.4404` edge `0.0025` maxDD `-0.249`
- `news_risk_high->index_1h` score `-0.0585` n `53` status `ready` deltaP `4.081` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.1502` n `53` status `ready` deltaP `2.1576` edge `-0.0043` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4065` n `137` status `ready` deltaP `3.2721` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.9165` n `137` status `ready` deltaP `5.4794` edge `-0.0257` maxDD `-2.9763`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
