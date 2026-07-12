# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T00:37:37.897968+00:00`
- Price records: `672`
- Market context records: `6446`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.5837` n `32` status `ready` deltaP `29.5139` edge `0.7833` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.9304` n `145` status `ready` deltaP `21.1698` edge `0.9331` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3208` n `32` status `ready` deltaP `52.4306` edge `0.1772` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9524` n `32` status `ready` deltaP `34.2014` edge `0.1219` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2285` n `32` status `ready` deltaP `11.1111` edge `0.4178` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4446` n `32` status `ready` deltaP `29.491` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5513` n `32` status `ready` deltaP `14.128` edge `0.1514` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.0674` n `183` status `ready` deltaP `-6.2465` edge `0.2207` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.9222` n `32` status `ready` deltaP `10.1235` edge `0.0969` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0613` n `183` status `ready` deltaP `7.3421` edge `0.0238` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1289` n `32` status `ready` deltaP `6.6804` edge `-0.0208` maxDD `-0.7581`
- `market_context_high->metal_4h` score `-0.2147` n `183` status `ready` deltaP `7.5037` edge `0.0409` maxDD `-2.7056`
- `market_context_high->unknown_4h` score `-0.4959` n `183` status `ready` deltaP `-15.473` edge `0.3024` maxDD `-10.5788`
- `news_risk_high->metal_1h` score `-0.5309` n `32` status `ready` deltaP `0.8982` edge `-0.0243` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5639` n `183` status `ready` deltaP `0.625` edge `0.0013` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.5753` n `145` status `ready` deltaP `1.5505` edge `0.1337` maxDD `-5.6914`
- `market_context_high->equity_4h` score `-0.5796` n `183` status `ready` deltaP `7.0605` edge `0.0485` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.6366` n `183` status `ready` deltaP `-1.2761` edge `-0.0048` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.6492` n `32` status `ready` deltaP `1.9097` edge `-0.0088` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
