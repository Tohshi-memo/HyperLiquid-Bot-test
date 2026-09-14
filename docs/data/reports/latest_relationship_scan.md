# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T08:22:32.377101+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_1h` score `443.4389` n `82` status `ready` deltaP `-5.999` edge `37.0354` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.1179` n `82` status `ready` deltaP `41.2027` edge `1.4506` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.5403` n `82` status `ready` deltaP `35.4374` edge `1.3725` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.083` n `82` status `ready` deltaP `35.7191` edge `0.9468` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2553` n `82` status `ready` deltaP `59.4911` edge `0.309` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.9386` n `84` status `ready` deltaP `39.8276` edge `0.3127` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.167` n `41` status `ready` deltaP `39.8276` edge `0.2484` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.167` n `41` status `ready` deltaP `39.8276` edge `0.2484` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.7752` n `82` status `ready` deltaP `34.9327` edge `0.2938` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.199` n `41` status `ready` deltaP `58.0782` edge `0.0503` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.199` n `41` status `ready` deltaP `58.0782` edge `0.0503` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.6662` n `84` status `ready` deltaP `53.3743` edge `0.0546` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9331` n `52` status `ready` deltaP `26.2899` edge `0.0208` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9331` n `52` status `ready` deltaP `26.2899` edge `0.0208` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7334` n `137` status `ready` deltaP `21.6998` edge `0.0416` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7071` n `137` status `ready` deltaP `12.3629` edge `0.0142` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6599` n `82` status `ready` deltaP `16.311` edge `0.0387` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3159` n `137` status `ready` deltaP `11.8357` edge `0.0092` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1916` n `52` status `ready` deltaP `6.7481` edge `0.0062` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1916` n `52` status `ready` deltaP `6.7481` edge `0.0062` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
