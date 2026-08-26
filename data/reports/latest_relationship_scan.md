# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T14:52:37.534959+00:00`
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

- `news_risk_high->unknown_24h` score `45.261` n `53` status `ready` deltaP `11.6319` edge `3.6942` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.2658` n `53` status `ready` deltaP `25.4372` edge `0.8625` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `11.6656` n `53` status `ready` deltaP `32.8583` edge `0.7972` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.8861` n `53` status `ready` deltaP `29.4189` edge `0.4708` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9939` n `53` status `ready` deltaP `39.7668` edge `0.0829` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.9936` n `53` status `ready` deltaP `36.0303` edge `0.0227` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.8989` n `136` status `ready` deltaP `23.7447` edge `0.1241` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.8166` n `53` status `ready` deltaP `15.8626` edge `0.1645` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `1.8621` n `53` status `ready` deltaP `29.5368` edge `-0.0375` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7647` n `53` status `ready` deltaP `20.0414` edge `0.0905` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1417` n `53` status `ready` deltaP `15.9191` edge `0.006` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1291` n `137` status `ready` deltaP `12.1028` edge `0.0583` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.4521` n `53` status `ready` deltaP `13.0748` edge `0.0072` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4092` n `53` status `ready` deltaP `10.5271` edge `-0.0048` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1609` n `53` status `ready` deltaP `6.9662` edge `0.0067` maxDD `-0.1788`
- `news_risk_high->metal_4h` score `-0.0349` n `53` status `ready` deltaP `7.7111` edge `-0.0012` maxDD `-0.249`
- `news_risk_high->index_1h` score `-0.055` n `53` status `ready` deltaP `4.1493` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.2114` n `53` status `ready` deltaP `1.6326` edge `-0.0059` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4185` n `137` status `ready` deltaP `3.0421` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.864` n `136` status `ready` deltaP `5.2278` edge `-0.0274` maxDD `-2.6898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
