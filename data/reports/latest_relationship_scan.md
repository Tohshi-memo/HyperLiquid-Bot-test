# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T17:37:25.323226+00:00`
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

- `news_risk_high->unknown_24h` score `46.4357` n `52` status `ready` deltaP `11.5717` edge `3.7925` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.5898` n `52` status `ready` deltaP `34.4958` edge `0.8633` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.3827` n `52` status `ready` deltaP `26.7042` edge `0.8638` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.2639` n `52` status `ready` deltaP `31.201` edge `0.4904` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.049` n `52` status `ready` deltaP `40.4245` edge `0.0831` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.1916` n `52` status `ready` deltaP `37.7786` edge `0.0233` maxDD `-0.0683`
- `market_context_high->unknown_4h` score `3.1152` n `137` status `ready` deltaP `25.1741` edge `0.1326` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7084` n `52` status `ready` deltaP `15.6494` edge `0.1569` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.0942` n `52` status `ready` deltaP `31.2375` edge `-0.0295` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7556` n `52` status `ready` deltaP `19.867` edge `0.0909` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.1663` n `137` status `ready` deltaP `12.2525` edge `0.0604` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.0952` n `52` status `ready` deltaP `15.3386` edge `0.006` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9556` n `52` status `ready` deltaP `14.567` edge `0.0141` maxDD `-0.5267`
- `news_risk_high->commodity_1h` score `0.3318` n `52` status `ready` deltaP `11.6882` edge `-0.0041` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2041` n `52` status `ready` deltaP `7.5668` edge `0.0063` maxDD `-0.1788`
- `news_risk_high->metal_4h` score `0.0756` n `52` status `ready` deltaP `8.5824` edge `0.0022` maxDD `-0.249`
- `news_risk_high->index_1h` score `-0.0212` n `52` status `ready` deltaP `4.6753` edge `0.0009` maxDD `-0.1165`
- `news_risk_high->metal_1h` score `-0.0402` n `52` status `ready` deltaP `3.0977` edge `-0.0032` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4185` n `137` status `ready` deltaP `3.0421` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.821` n `137` status `ready` deltaP `6.2382` edge `-0.0228` maxDD `-2.9763`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
