# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T21:37:26.433692+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `13046.9364` n `56` status `ready` deltaP `10.2093` edge `1087.1968` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `4428.0115` n `34` status `ready` deltaP `10.3144` edge `368.9387` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `4428.0115` n `34` status `ready` deltaP `10.3144` edge `368.9387` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `436.018` n `82` status `ready` deltaP `-5.4002` edge `36.413` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.7123` n `82` status `ready` deltaP `36.2027` edge `1.3668` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3016` n `82` status `ready` deltaP `38.0236` edge `1.4187` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.8975` n `82` status `ready` deltaP `29.3398` edge `0.8072` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.373` n `82` status `ready` deltaP `53.1118` edge `0.278` maxDD `-0.0797`
- `risk_on_high->commodity_24h` score `4.8662` n `34` status `ready` deltaP `39.8276` edge `0.14` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8662` n `34` status `ready` deltaP `39.8276` edge `0.14` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.8653` n `82` status `ready` deltaP `27.519` edge `0.2674` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.763` n `56` status `ready` deltaP `39.8276` edge `0.1314` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.5343` n `56` status `ready` deltaP `5.0616` edge `0.4269` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `3.2021` n `34` status `ready` deltaP `0.3347` edge `0.3982` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.2021` n `34` status `ready` deltaP `0.3347` edge `0.3982` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `2.3517` n `34` status `ready` deltaP `47.3428` edge `0.0262` maxDD `-0.8922`
- `risk_on_and_context->fx_24h` score `2.3517` n `34` status `ready` deltaP `47.3428` edge `0.0262` maxDD `-0.8922`
- `risk_on_high->commodity_4h` score `1.4024` n `57` status `ready` deltaP `20.2557` edge `0.0168` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.4024` n `57` status `ready` deltaP `20.2557` edge `0.0168` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.1099` n `129` status `ready` deltaP `17.6853` edge `0.0164` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
