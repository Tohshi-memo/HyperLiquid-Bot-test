# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T16:37:32.377040+00:00`
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

- `news_risk_high->unknown_24h` score `45.5441` n `53` status `ready` deltaP `11.5717` edge `3.7182` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.7132` n `53` status `ready` deltaP `33.8775` edge `0.8777` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.3945` n `53` status `ready` deltaP `26.2061` edge `0.8681` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `6.944` n `53` status `ready` deltaP `29.6771` edge `0.4739` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9502` n `53` status `ready` deltaP `39.3098` edge `0.0823` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.0133` n `53` status `ready` deltaP `36.2614` edge `0.0228` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.9827` n `137` status `ready` deltaP `24.5672` edge `0.1256` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.861` n `53` status `ready` deltaP `16.162` edge `0.1662` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.0298` n `53` status `ready` deltaP `30.583` edge `-0.0305` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.8495` n `53` status `ready` deltaP `20.6058` edge `0.0938` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.1734` n `137` status `ready` deltaP `12.4022` edge `0.06` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.1536` n `53` status `ready` deltaP `16.0688` edge `0.006` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5105` n `53` status `ready` deltaP `13.6736` edge `0.0107` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3948` n `53` status `ready` deltaP `10.5271` edge `-0.006` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1518` n `53` status `ready` deltaP `6.8973` edge `0.0064` maxDD `-0.1788`
- `news_risk_high->metal_4h` score `0.0884` n `53` status `ready` deltaP `8.5922` edge `0.0032` maxDD `-0.249`
- `news_risk_high->index_1h` score `-0.0628` n `53` status `ready` deltaP `3.9996` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.1431` n `53` status `ready` deltaP `2.2314` edge `-0.0042` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4107` n `137` status `ready` deltaP `3.1918` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.8959` n `137` status `ready` deltaP `5.6312` edge `-0.025` maxDD `-2.9763`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
