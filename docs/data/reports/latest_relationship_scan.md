# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T07:37:30.731987+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11471`

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

- `news_risk_high->unknown_4h` score `365.6234` n `83` status `ready` deltaP `-21.6629` edge `30.7025` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `24.3963` n `78` status `ready` deltaP `47.7698` edge `1.7536` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.1297` n `78` status `ready` deltaP `39.7303` edge `1.643` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.6416` n `78` status `ready` deltaP `49.3322` edge `1.152` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.0925` n `78` status `ready` deltaP `57.2516` edge `0.3103` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.83` n `78` status `ready` deltaP `38.4882` edge `0.358` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.5498` n `52` status `ready` deltaP `35.9375` edge `0.2229` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5498` n `52` status `ready` deltaP `35.9375` edge `0.2229` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2507` n `149` status `ready` deltaP `29.2261` edge `0.2119` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3669` n `52` status `ready` deltaP `31.9311` edge `-0.0114` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3669` n `52` status `ready` deltaP `31.9311` edge `-0.0114` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.232` n `149` status `ready` deltaP `29.1562` edge `0.0132` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9811` n `52` status `ready` deltaP `26.2899` edge `0.0248` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9811` n `52` status `ready` deltaP `26.2899` edge `0.0248` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8808` n `149` status `ready` deltaP `22.7922` edge `0.0466` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8006` n `149` status `ready` deltaP `13.2169` edge `0.0163` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6538` n `83` status `ready` deltaP `16.614` edge `0.0359` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.563` n `52` status `ready` deltaP `10.7646` edge `0.1619` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.563` n `52` status `ready` deltaP `10.7646` edge `0.1619` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.1773` n `52` status `ready` deltaP `6.299` edge `0.008` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
