# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T09:52:31.360860+00:00`
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

- `news_risk_high->unknown_1h` score `442.9457` n `82` status `ready` deltaP `-6.1487` edge `36.9953` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.3045` n `82` status `ready` deltaP `41.781` edge `1.4623` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.3762` n `82` status `ready` deltaP `34.8112` edge `1.363` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.0906` n `82` status `ready` deltaP `35.4844` edge `0.949` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2404` n `82` status `ready` deltaP `59.3199` edge `0.3089` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `7.0483` n `86` status `ready` deltaP `40.1042` edge `0.32` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2191` n `41` status `ready` deltaP `40.1042` edge `0.2509` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2191` n `41` status `ready` deltaP `40.1042` edge `0.2509` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.8145` n `82` status `ready` deltaP `34.989` edge `0.2967` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.1337` n `41` status `ready` deltaP `57.4568` edge `0.049` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.1337` n `41` status `ready` deltaP `57.4568` edge `0.049` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.613` n `86` status `ready` deltaP `52.9191` edge `0.0532` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9451` n `52` status `ready` deltaP `26.2899` edge `0.0218` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9451` n `52` status `ready` deltaP `26.2899` edge `0.0218` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7454` n `137` status `ready` deltaP `21.6998` edge `0.0426` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7071` n `137` status `ready` deltaP `12.3629` edge `0.0142` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6646` n `82` status `ready` deltaP `16.311` edge `0.0393` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3326` n `137` status `ready` deltaP `12.1406` edge `0.0093` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.195` n `137` status `ready` deltaP `5.9607` edge `0.0023` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1916` n `52` status `ready` deltaP `6.7481` edge `0.0062` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
