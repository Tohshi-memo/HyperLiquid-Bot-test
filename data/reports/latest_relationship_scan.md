# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T17:07:27.415710+00:00`
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

- `news_risk_high->unknown_24h` score `45.6197` n `53` status `ready` deltaP `11.5717` edge `3.7245` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.0864` n `53` status `ready` deltaP `34.2229` edge `0.9065` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.4476` n `53` status `ready` deltaP `26.5096` edge `0.8705` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `6.9176` n `53` status `ready` deltaP `29.6771` edge `0.4717` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9316` n `53` status `ready` deltaP `39.1371` edge `0.0819` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.0357` n `137` status `ready` deltaP `24.8707` edge `0.128` maxDD `-0.5994`
- `news_risk_high->fx_4h` score `3.0` n `53` status `ready` deltaP `36.1096` edge `0.0227` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.8598` n `53` status `ready` deltaP `16.162` edge `0.1661` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.0815` n `53` status `ready` deltaP `30.9284` edge `-0.0285` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.8156` n `53` status `ready` deltaP `20.3024` edge `0.093` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.1722` n `137` status `ready` deltaP `12.4022` edge `0.0599` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.1297` n `53` status `ready` deltaP `15.7694` edge `0.006` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4894` n `53` status `ready` deltaP `13.5239` edge `0.009` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3948` n `53` status `ready` deltaP `10.5271` edge `-0.006` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.1259` n `53` status `ready` deltaP `8.8957` edge `0.0043` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1239` n `53` status `ready` deltaP `6.5938` edge `0.0061` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0721` n `53` status `ready` deltaP `3.8499` edge `0.0004` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.1443` n `53` status `ready` deltaP `2.2314` edge `-0.0043` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4263` n `137` status `ready` deltaP `2.8924` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.8585` n `137` status `ready` deltaP `5.9347` edge `-0.0239` maxDD `-2.9763`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
