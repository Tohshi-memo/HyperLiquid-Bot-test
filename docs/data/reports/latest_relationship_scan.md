# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T06:22:32.986238+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11520`

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

- `news_risk_high->unknown_1h` score `443.5517` n `82` status `ready` deltaP `-6.1487` edge `37.0458` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.9361` n `82` status `ready` deltaP `39.9958` edge `1.4435` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.9734` n `82` status `ready` deltaP `36.8167` edge `1.3994` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.861` n `82` status `ready` deltaP `35.3743` edge `0.9306` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.1845` n `82` status `ready` deltaP `59.1463` edge `0.3054` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.7622` n `76` status `ready` deltaP `39.8276` edge `0.298` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2366` n `41` status `ready` deltaP `39.8276` edge `0.2542` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2366` n `41` status `ready` deltaP `39.8276` edge `0.2542` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.5929` n `82` status `ready` deltaP `33.5534` edge `0.2878` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.3478` n `41` status `ready` deltaP `59.4576` edge `0.0535` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.3478` n `41` status `ready` deltaP `59.4576` edge `0.0535` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7261` n `76` status `ready` deltaP `54.0019` edge `0.0554` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9963` n `52` status `ready` deltaP `26.8996` edge `0.022` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9963` n `52` status `ready` deltaP `26.8996` edge `0.022` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7966` n `137` status `ready` deltaP `22.3095` edge `0.0428` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7933` n `137` status `ready` deltaP `13.1114` edge `0.0164` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6204` n `82` status `ready` deltaP `15.7012` edge `0.0377` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3301` n `137` status `ready` deltaP `11.9881` edge `0.01` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2779` n `52` status `ready` deltaP `7.4966` edge `0.0084` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2779` n `52` status `ready` deltaP `7.4966` edge `0.0084` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
