# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T01:22:26.519111+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11118`

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

- `news_risk_high->unknown_1h` score `442.2688` n `82` status `ready` deltaP `-5.5499` edge `36.9349` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.1442` n `82` status `ready` deltaP `36.8923` edge `1.3982` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.346` n `82` status `ready` deltaP `38.0236` edge `1.4224` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.7211` n `82` status `ready` deltaP `31.926` edge `0.8586` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.7071` n `82` status `ready` deltaP `55.698` edge `0.2886` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.0758` n `56` status `ready` deltaP `39.8276` edge `0.2408` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.6054` n `33` status `ready` deltaP `39.8276` edge `0.2016` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.6054` n `33` status `ready` deltaP `39.8276` edge `0.2016` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.5979` n `33` status `ready` deltaP `62.3145` edge `0.0553` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.5979` n `33` status `ready` deltaP `62.3145` edge `0.0553` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.137` n `82` status `ready` deltaP `30.1052` edge `0.2728` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8291` n `56` status `ready` deltaP `54.6305` edge `0.0598` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8471` n `51` status `ready` deltaP `25.9505` edge `0.0159` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8471` n `51` status `ready` deltaP `25.9505` edge `0.0159` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7393` n `125` status `ready` deltaP `21.9976` edge `0.0401` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6376` n `137` status `ready` deltaP `11.4647` edge `0.0144` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5279` n `82` status `ready` deltaP `14.1768` edge `0.036` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2493` n `125` status `ready` deltaP `10.3439` edge `0.0106` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1603` n `137` status `ready` deltaP `5.5116` edge `0.0024` maxDD `-0.063`
- `risk_on_high->crypto_alt_24h` score `0.1299` n `33` status `ready` deltaP `-3.6103` edge `0.2261` maxDD `-11.6298`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
