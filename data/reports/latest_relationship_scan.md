# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T17:22:34.666397+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10692`

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

- `news_risk_high->unknown_4h` score `395.0174` n `78` status `ready` deltaP `-21.9981` edge `33.1541` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.9091` n `78` status `ready` deltaP `46.9017` edge `1.5522` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.2509` n `78` status `ready` deltaP `34.1747` edge `1.3568` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.2276` n `78` status `ready` deltaP `39.4364` edge `1.0174` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7051` n `78` status `ready` deltaP `61.9391` edge `0.3301` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.8385` n `113` status `ready` deltaP `38.0208` edge `0.3164` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.3605` n `78` status `ready` deltaP `37.7938` edge `0.3235` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1065` n `51` status `ready` deltaP `38.0208` edge `0.2554` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1065` n `51` status `ready` deltaP `38.0208` edge `0.2554` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.7121` n `51` status `ready` deltaP `52.7267` edge `0.0454` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.7121` n `51` status `ready` deltaP `52.7267` edge `0.0454` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.3009` n `113` status `ready` deltaP `49.3778` edge `0.0508` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9701` n `52` status `ready` deltaP `26.1374` edge `0.0249` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9701` n `52` status `ready` deltaP `26.1374` edge `0.0249` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7704` n `137` status `ready` deltaP `21.5473` edge `0.0457` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7622` n `137` status `ready` deltaP `12.6623` edge `0.0168` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6469` n `78` status `ready` deltaP `15.8966` edge `0.0398` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2468` n `52` status `ready` deltaP `7.0475` edge `0.0088` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2468` n `52` status `ready` deltaP `7.0475` edge `0.0088` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2186` n `137` status `ready` deltaP `10.1589` edge `0.0079` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
