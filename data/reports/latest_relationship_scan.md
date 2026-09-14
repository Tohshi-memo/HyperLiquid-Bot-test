# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T06:37:29.802275+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11550`

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

- `news_risk_high->unknown_1h` score `443.5709` n `82` status `ready` deltaP `-5.999` edge `37.0464` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.9679` n `82` status `ready` deltaP `40.1682` edge `1.445` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.9296` n `82` status `ready` deltaP `36.6443` edge `1.3969` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.906` n `82` status `ready` deltaP `35.5467` edge `0.9332` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2055` n `82` status `ready` deltaP `59.3187` edge `0.306` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.7682` n `77` status `ready` deltaP `39.8276` edge `0.2985` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2294` n `41` status `ready` deltaP `39.8276` edge `0.2536` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2294` n `41` status `ready` deltaP `39.8276` edge `0.2536` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.6151` n `82` status `ready` deltaP `33.7259` edge `0.2885` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.328` n `41` status `ready` deltaP `59.2851` edge `0.053` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.328` n `41` status `ready` deltaP `59.2851` edge `0.053` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7205` n `77` status `ready` deltaP `53.9319` edge `0.0554` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9939` n `52` status `ready` deltaP `26.8996` edge `0.0218` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9939` n `52` status `ready` deltaP `26.8996` edge `0.0218` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7942` n `137` status `ready` deltaP `22.3095` edge `0.0426` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8053` n `137` status `ready` deltaP `13.2611` edge `0.0164` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6299` n `82` status `ready` deltaP `15.8536` edge `0.0379` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3286` n `137` status `ready` deltaP `11.9881` edge `0.0098` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2899` n `52` status `ready` deltaP `7.6463` edge `0.0084` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2899` n `52` status `ready` deltaP `7.6463` edge `0.0084` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
