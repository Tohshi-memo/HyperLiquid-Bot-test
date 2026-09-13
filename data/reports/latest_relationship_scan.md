# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T01:37:27.776163+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12553`

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

- `market_context_high->unknown_24h` score `16586.9486` n `59` status `ready` deltaP `12.0616` edge `1382.1705` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `378.754` n `82` status `ready` deltaP `-5.8493` edge `31.644` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.1874` n `82` status `ready` deltaP `32.9268` edge `1.3449` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0711` n `82` status `ready` deltaP `39.6723` edge `1.3885` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.4295` n `59` status `ready` deltaP `46.3542` edge `0.5601` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.2889` n `59` status `ready` deltaP `22.8814` edge `0.7876` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.1724` n `82` status `ready` deltaP `15.8664` edge `0.5866` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.0974` n `82` status `ready` deltaP `42.1324` edge `0.2449` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.0088` n `82` status `ready` deltaP `28.2182` edge `0.2747` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2668` n `59` status `ready` deltaP `42.5347` edge `0.072` maxDD `0.0`
- `market_context_high->index_24h` score `3.9761` n `59` status `ready` deltaP `42.7319` edge `0.0857` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.3647` n `59` status `ready` deltaP `9.016` edge `0.1064` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.15` n `82` status `ready` deltaP `8.0792` edge `0.0282` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1025` n `54` status `ready` deltaP `6.0989` edge `0.0009` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1025` n `54` status `ready` deltaP `6.0989` edge `0.0009` maxDD `-0.3081`
- `risk_on_high->crypto_alt_4h` score `0.0768` n `52` status `ready` deltaP `7.1412` edge `0.1297` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.0768` n `52` status `ready` deltaP `7.1412` edge `0.1297` maxDD `-6.7304`
- `risk_on_high->index_1h` score `-0.0881` n `54` status `ready` deltaP `4.8071` edge `0.0005` maxDD `-0.1736`
- `risk_on_and_context->index_1h` score `-0.0881` n `54` status `ready` deltaP `4.8071` edge `0.0005` maxDD `-0.1736`
- `risk_on_high->fx_1h` score `-0.1401` n `54` status `ready` deltaP `0.693` edge `0.003` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
