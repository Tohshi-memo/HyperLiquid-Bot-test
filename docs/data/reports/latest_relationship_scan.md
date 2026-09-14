# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T08:07:51.985204+00:00`
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

- `news_risk_high->unknown_1h` score `443.5613` n `82` status `ready` deltaP `-5.999` edge `37.0456` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.0981` n `82` status `ready` deltaP `41.0302` edge `1.4501` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.5985` n `82` status `ready` deltaP `35.6098` edge `1.3762` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.0578` n `82` status `ready` deltaP `35.7191` edge `0.9447` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2505` n `82` status `ready` deltaP `59.4911` edge `0.3086` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.9026` n `83` status `ready` deltaP `39.8276` edge `0.3097` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1754` n `41` status `ready` deltaP `39.8276` edge `0.2491` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1754` n `41` status `ready` deltaP `39.8276` edge `0.2491` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.7506` n `82` status `ready` deltaP `34.7603` edge `0.2929` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.2164` n `41` status `ready` deltaP `58.2507` edge `0.0506` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.2164` n `41` status `ready` deltaP `58.2507` edge `0.0506` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.6768` n `83` status `ready` deltaP `53.4608` edge `0.0549` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9319` n `52` status `ready` deltaP `26.2899` edge `0.0207` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9319` n `52` status `ready` deltaP `26.2899` edge `0.0207` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7322` n `137` status `ready` deltaP `21.6998` edge `0.0415` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.725` n `137` status `ready` deltaP `12.5126` edge `0.0147` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6591` n `82` status `ready` deltaP `16.311` edge `0.0386` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3159` n `137` status `ready` deltaP `11.8357` edge `0.0092` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2096` n `52` status `ready` deltaP `6.8978` edge `0.0067` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2096` n `52` status `ready` deltaP `6.8978` edge `0.0067` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
