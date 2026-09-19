# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T20:22:28.111077+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8478`

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

- `news_risk_high->crypto_major_24h` score `51.1419` n `72` status `ready` deltaP `27.2569` edge `4.1693` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.6432` n `72` status `ready` deltaP `33.507` edge `3.6348` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `38.006` n `117` status `ready` deltaP `-3.8865` edge `3.2164` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.8566` n `72` status `ready` deltaP `37.1528` edge `0.4946` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8424` n `117` status `ready` deltaP `40.2377` edge `0.4378` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.5183` n `98` status `ready` deltaP `20.3988` edge `0.4448` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2711` n `98` status `ready` deltaP `21.4659` edge `0.3386` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2017` n `98` status `ready` deltaP `18.3246` edge `0.1912` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.6619` n `117` status `ready` deltaP `27.2879` edge `0.0815` maxDD `-0.3276`
- `news_risk_high->crypto_major_1h` score `2.3623` n `98` status `ready` deltaP `19.6719` edge `0.118` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7249` n `72` status `ready` deltaP `22.5694` edge `0.0777` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4248` n `117` status `ready` deltaP `17.5841` edge `0.0267` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.8222` n `98` status `ready` deltaP `19.1295` edge `0.0464` maxDD `-2.0994`
- `market_context_high->fx_4h` score `0.8045` n `117` status `ready` deltaP `17.2269` edge `-0.001` maxDD `-0.0779`
- `news_risk_high->metal_1h` score `0.7195` n `98` status `ready` deltaP `15.6055` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.4857` n `98` status `ready` deltaP `7.4148` edge `0.0316` maxDD `-0.9112`
- `news_risk_high->fx_24h` score `0.4078` n `72` status `ready` deltaP `2.0834` edge `0.0383` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.2518` n `117` status `ready` deltaP `8.1731` edge `-0.0293` maxDD `-0.0027`
- `market_context_high->fx_1h` score `-0.0072` n `117` status `ready` deltaP `3.6287` edge `0.001` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.0145` n `98` status `ready` deltaP `9.2085` edge `0.0818` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
