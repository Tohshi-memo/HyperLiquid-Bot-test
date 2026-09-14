# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T00:52:29.379805+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12228`

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

- `news_risk_high->unknown_1h` score `442.4512` n `82` status `ready` deltaP `-5.6996` edge `36.9511` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.0902` n `82` status `ready` deltaP `36.8923` edge `1.3937` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3412` n `82` status `ready` deltaP `38.0236` edge `1.422` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.5964` n `82` status `ready` deltaP `31.5812` edge `0.8505` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.6591` n `82` status `ready` deltaP `55.3532` edge `0.2869` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.8466` n `56` status `ready` deltaP `39.8276` edge `0.2217` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.5859` n `31` status `ready` deltaP `62.4639` edge `0.0533` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.5859` n `31` status `ready` deltaP `62.4639` edge `0.0533` maxDD `-0.0054`
- `risk_on_high->commodity_24h` score `5.267` n `31` status `ready` deltaP `39.8276` edge `0.1734` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.267` n `31` status `ready` deltaP `39.8276` edge `0.1734` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.0938` n `82` status `ready` deltaP `29.7603` edge `0.2715` maxDD `-0.6334`
- `market_context_high->fx_24h` score `2.7846` n `56` status `ready` deltaP `51.404` edge `0.0501` maxDD `-0.5303`
- `risk_on_high->crypto_alt_24h` score `1.9343` n `31` status `ready` deltaP `-0.8732` edge `0.3137` maxDD `-8.0684`
- `risk_on_and_context->crypto_alt_24h` score `1.9343` n `31` status `ready` deltaP `-0.8732` edge `0.3137` maxDD `-8.0684`
- `risk_on_high->commodity_4h` score `1.8615` n `51` status `ready` deltaP `25.9505` edge `0.0171` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8615` n `51` status `ready` deltaP `25.9505` edge `0.0171` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6805` n `125` status `ready` deltaP `21.9976` edge `0.0352` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.572` n `137` status `ready` deltaP `10.8845` edge `0.0128` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5073` n `82` status `ready` deltaP `13.8719` edge `0.0354` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2164` n `125` status `ready` deltaP `9.6963` edge `0.0107` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
