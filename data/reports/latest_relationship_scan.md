# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T05:22:17.579335+00:00`
- Price records: `672`
- Market context records: `1915`
- Flow alert records: `7412`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6052`

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

- `market_context_high->crypto_alt_4h` score `7.8396` n `199` status `ready` deltaP `24.4906` edge `0.6045` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.3003` n `199` status `ready` deltaP `29.5441` edge `0.536` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9831` n `199` status `ready` deltaP `17.958` edge `0.4146` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.7041` n `199` status `ready` deltaP `16.2589` edge `0.2264` maxDD `-5.0894`
- `market_context_high->metal_24h` score `0.9779` n `192` status `ready` deltaP `13.8889` edge `0.2315` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `0.9148` n `192` status `ready` deltaP `13.5416` edge `0.518` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.7935` n `207` status `ready` deltaP `8.5561` edge `0.1077` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.634` n `207` status `ready` deltaP `7.8756` edge `0.1117` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.6255` n `192` status `ready` deltaP `6.25` edge `0.1333` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.5624` n `199` status `ready` deltaP `10.8553` edge `0.0834` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.0576` n `192` status `ready` deltaP `11.8056` edge `0.0214` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.105` n `207` status `ready` deltaP `5.1195` edge `0.0365` maxDD `-2.6836`
- `market_context_high->index_1h` score `-0.6262` n `207` status `ready` deltaP `0.2683` edge `0.0092` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6276` n `199` status `ready` deltaP `12.238` edge `0.1353` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6313` n `207` status `ready` deltaP `-2.8067` edge `0.001` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.636` n `207` status `ready` deltaP `5.1065` edge `0.018` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.7861` n `199` status `ready` deltaP `-1.9901` edge `0.0013` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-1.1283` n `207` status `ready` deltaP `1.33` edge `-0.0077` maxDD `-3.6151`
- `market_context_high->equity_24h` score `-1.1443` n `192` status `ready` deltaP `6.5973` edge `0.3505` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `-1.9691` n `192` status `ready` deltaP `13.8889` edge `0.6019` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
