# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T06:52:35.326948+00:00`
- Price records: `672`
- Market context records: `6163`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.6345` n `32` status `ready` deltaP `42.8879` edge `0.7817` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.4662` n `32` status `ready` deltaP `65.5172` edge `0.1854` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1642` n `32` status `ready` deltaP `43.3523` edge `0.0626` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6782` n `195` status `ready` deltaP `0.9543` edge `0.2343` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.4033` n `32` status `ready` deltaP `16.3147` edge `0.1491` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.1911` n `32` status `ready` deltaP `12.7807` edge `0.1142` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5941` n `32` status `ready` deltaP `8.0277` edge `0.0688` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.2209` n `195` status `ready` deltaP `-0.9091` edge `0.2777` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0924` n `195` status `ready` deltaP `20.3227` edge `0.1332` maxDD `-11.8809`
- `news_risk_high->index_24h` score `0.0035` n `32` status `ready` deltaP `10.2155` edge `0.0195` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.0389` n `195` status `ready` deltaP `2.7273` edge `0.0703` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.27` n `195` status `ready` deltaP `1.5845` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5831` n `195` status `ready` deltaP `4.1842` edge `0.0161` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.732` n `195` status `ready` deltaP `-1.8394` edge `-0.0041` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7676` n `32` status `ready` deltaP `-2.994` edge `-0.0287` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8152` n `195` status `ready` deltaP `2.3906` edge `-0.004` maxDD `-2.0564`
- `news_risk_high->commodity_24h` score `-0.8574` n `32` status `ready` deltaP `11.7888` edge `-0.1295` maxDD `-0.3101`
- `market_context_high->equity_1h` score `-0.9458` n `195` status `ready` deltaP `-2.2056` edge `0.005` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9818` n `195` status `ready` deltaP `3.0117` edge `0.0293` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
