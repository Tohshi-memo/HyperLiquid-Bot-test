# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T23:37:16.854038+00:00`
- Price records: `672`
- Market context records: `1789`
- Flow alert records: `7044`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8882`

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

- `market_context_high->metal_24h` score `7.2801` n `189` status `ready` deltaP `28.5714` edge `0.6588` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.212` n `30` status `ready` deltaP `28.1911` edge `0.3952` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.814` n `194` status `ready` deltaP `21.7076` edge `0.5164` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.3671` n `194` status `ready` deltaP `22.7826` edge `0.4526` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.7225` n `194` status `ready` deltaP `15.7546` edge `0.4323` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.2122` n `30` status `ready` deltaP `24.7206` edge `0.1346` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0249` n `194` status `ready` deltaP `16.4744` edge `0.2517` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.8394` n `189` status `ready` deltaP `14.633` edge `0.2619` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.6029` n `189` status `ready` deltaP `15.7077` edge `0.5187` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.0429` n `189` status `ready` deltaP `12.8472` edge `0.5333` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9103` n `194` status `ready` deltaP `12.4591` edge `0.1017` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8079` n `30` status `ready` deltaP `20.2643` edge `-0.0043` maxDD `-0.1774`
- `news_risk_high->unknown_4h` score `0.529` n `30` status `ready` deltaP `11.0467` edge `0.0665` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3985` n `199` status `ready` deltaP `7.1044` edge `0.097` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.0733` n `199` status `ready` deltaP `4.5384` edge `0.0832` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0267` n `199` status `ready` deltaP `4.9763` edge `0.0499` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2709` n `199` status `ready` deltaP `3.2551` edge `0.0189` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3633` n `194` status `ready` deltaP `12.4073` edge `0.1399` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.3923` n `189` status `ready` deltaP `8.8376` edge `0.0133` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4341` n `30` status `ready` deltaP `17.006` edge `-0.1218` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
