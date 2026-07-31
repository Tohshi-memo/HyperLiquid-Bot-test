# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T16:07:33.357125+00:00`
- Price records: `672`
- Market context records: `8529`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6280.0092` n `52` status `ready` deltaP `44.2174` edge `523.0814` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7608` n `64` status `ready` deltaP `21.2652` edge `0.398` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0543` n `64` status `ready` deltaP `16.8064` edge `0.0782` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8345` n `64` status `ready` deltaP `16.4016` edge `0.0912` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9514` n `64` status `ready` deltaP `6.4405` edge `0.1566` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8457` n `64` status `ready` deltaP `15.0915` edge `0.147` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.524` n `64` status `ready` deltaP `9.0101` edge `0.0598` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3548` n `64` status `ready` deltaP `6.7646` edge `0.0516` maxDD `-2.0972`
- `market_context_high->crypto_alt_4h` score `0.3276` n `45` status `ready` deltaP `5.9248` edge `0.0982` maxDD `-5.323`
- `news_risk_high->fx_1h` score `0.1134` n `64` status `ready` deltaP `5.7354` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0667` n `64` status `ready` deltaP `4.5191` edge `0.0101` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.066` n `64` status `ready` deltaP `2.9345` edge `0.0365` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.0338` n `64` status `ready` deltaP `11.471` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.082` n `64` status `ready` deltaP `3.7051` edge `0.0088` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.3551` n `57` status `ready` deltaP `3.1227` edge `-0.0038` maxDD `-2.0038`
- `market_context_high->metal_1h` score `-0.4576` n `57` status `ready` deltaP `0.0867` edge `-0.0098` maxDD `-1.6224`
- `market_context_high->commodity_4h` score `-0.7364` n `45` status `ready` deltaP `4.6578` edge `0.026` maxDD `-5.4508`
- `market_context_high->fx_1h` score `-0.7658` n `57` status `ready` deltaP `-1.5837` edge `-0.003` maxDD `-0.6874`
- `market_context_high->crypto_alt_1h` score `-0.8289` n `57` status `ready` deltaP `-6.6971` edge `0.0011` maxDD `-3.0178`
- `market_context_high->fx_4h` score `-0.9833` n `45` status `ready` deltaP `-2.3137` edge `-0.0064` maxDD `-1.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
