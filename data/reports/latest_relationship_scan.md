# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T16:08:55.678839+00:00`
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

- `news_risk_high->unknown_24h` score `45.4649` n `53` status `ready` deltaP `11.5717` edge `3.7116` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.351` n `53` status `ready` deltaP `25.9026` edge `0.8665` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `12.3387` n `53` status `ready` deltaP `33.5321` edge `0.8488` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.9428` n `53` status `ready` deltaP `29.6771` edge `0.4738` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9514` n `53` status `ready` deltaP `39.3098` edge `0.0824` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.0255` n `53` status `ready` deltaP `36.4131` edge `0.0228` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.9392` n `137` status `ready` deltaP `24.2637` edge `0.124` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.8753` n `53` status `ready` deltaP `16.2067` edge `0.1671` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `1.9734` n `53` status `ready` deltaP `30.2376` edge `-0.0329` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.818` n `53` status `ready` deltaP `20.3024` edge `0.0932` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.1878` n `137` status `ready` deltaP `12.4469` edge `0.0609` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.1665` n `53` status `ready` deltaP `16.2292` edge `0.006` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4967` n `53` status `ready` deltaP `13.5426` edge `0.0098` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3816` n `53` status `ready` deltaP `10.3774` edge `-0.0061` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1542` n `53` status `ready` deltaP `6.8973` edge `0.0066` maxDD `-0.1788`
- `news_risk_high->metal_4h` score `0.0461` n `53` status `ready` deltaP `8.2887` edge `0.0017` maxDD `-0.249`
- `news_risk_high->index_1h` score `-0.0543` n `53` status `ready` deltaP `4.1622` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.1585` n `53` status `ready` deltaP `2.0839` edge `-0.0045` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4024` n `137` status `ready` deltaP `3.3522` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.9382` n `137` status `ready` deltaP `5.3277` edge `-0.0265` maxDD `-2.9763`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
