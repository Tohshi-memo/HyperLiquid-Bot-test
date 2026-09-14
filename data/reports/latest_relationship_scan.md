# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T01:37:01.432898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11184`

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
- `news_risk_high->crypto_alt_24h` score `19.1754` n `82` status `ready` deltaP `36.8923` edge `1.4008` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.352` n `82` status `ready` deltaP `38.0236` edge `1.4229` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.7853` n `82` status `ready` deltaP `32.0984` edge `0.8628` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.7317` n `82` status `ready` deltaP `55.8704` edge `0.2895` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.143` n `57` status `ready` deltaP `39.8276` edge `0.2464` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.7398` n `34` status `ready` deltaP `39.8276` edge `0.2128` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7398` n `34` status `ready` deltaP `39.8276` edge `0.2128` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.6009` n `34` status `ready` deltaP `62.2312` edge `0.0561` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.6009` n `34` status `ready` deltaP `62.2312` edge `0.0561` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.1568` n `82` status `ready` deltaP `30.2776` edge `0.2733` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8328` n `57` status `ready` deltaP `54.6461` edge `0.06` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9463` n `52` status `ready` deltaP `26.2899` edge `0.0219` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9463` n `52` status `ready` deltaP `26.2899` edge `0.0219` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7782` n `126` status `ready` deltaP `22.169` edge `0.0422` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6508` n `137` status `ready` deltaP `11.6144` edge `0.0145` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5381` n `82` status `ready` deltaP `14.3292` edge `0.0363` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2684` n `126` status `ready` deltaP `10.6804` edge `0.0108` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1723` n `137` status `ready` deltaP `5.6613` edge `0.0024` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1354` n `52` status `ready` deltaP `5.9996` edge `0.0065` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
