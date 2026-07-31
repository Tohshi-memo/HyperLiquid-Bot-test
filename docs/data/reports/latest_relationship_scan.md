# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T17:52:55.981953+00:00`
- Price records: `672`
- Market context records: `8536`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5914`

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

- `news_risk_high->unknown_24h` score `6279.7812` n `52` status `ready` deltaP `43.0021` edge `523.0705` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.793` n `64` status `ready` deltaP `21.1128` edge `0.4017` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0325` n `64` status `ready` deltaP `16.654` edge `0.0774` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7002` n `64` status `ready` deltaP `15.8028` edge `0.084` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0257` n `64` status `ready` deltaP `6.7454` edge `0.1641` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8001` n `64` status `ready` deltaP `14.6341` edge `0.1442` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.6239` n `52` status `ready` deltaP `7.9033` edge `0.123` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.475` n `64` status `ready` deltaP `8.4113` edge `0.0575` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3438` n `64` status `ready` deltaP `6.7646` edge `0.0502` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0722` n `64` status `ready` deltaP `4.9869` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0227` n `64` status `ready` deltaP `2.4771` edge `0.034` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0177` n `64` status `ready` deltaP `3.7706` edge `0.0088` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `-0.0064` n `64` status `ready` deltaP `11.0137` edge `0.0218` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1143` n `64` status `ready` deltaP `3.4057` edge `0.0081` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2926` n `62` status `ready` deltaP `1.9123` edge `0.0` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3184` n `62` status `ready` deltaP `3.7087` edge `-0.003` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5018` n `62` status `ready` deltaP `-2.627` edge `0.0159` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7561` n `62` status `ready` deltaP `0.7968` edge `-0.0154` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9553` n `62` status `ready` deltaP `-2.8443` edge `-0.0112` maxDD `-1.6224`
- `market_context_high->fx_4h` score `-1.1895` n `52` status `ready` deltaP `-2.0873` edge `-0.0056` maxDD `-1.3685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
