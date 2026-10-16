# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T18:22:31.474740+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7180`

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

- `risk_on_high->commodity_24h` score `7.7748` n `54` status `ready` deltaP `41.115` edge `0.3738` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.7748` n `54` status `ready` deltaP `41.115` edge `0.3738` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5204` n `127` status `ready` deltaP `19.6718` edge `0.587` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.9081` n `127` status `ready` deltaP `21.1206` edge `0.4837` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.5393` n `54` status `ready` deltaP `22.0924` edge `0.359` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.5393` n `54` status `ready` deltaP `22.0924` edge `0.359` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0919` n `54` status `ready` deltaP `33.3108` edge `0.3878` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0919` n `54` status `ready` deltaP `33.3108` edge `0.3878` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6606` n `127` status `ready` deltaP `13.9681` edge `0.1517` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0213` n `127` status `ready` deltaP `6.3546` edge `0.1233` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5781` n `127` status `ready` deltaP `15.1515` edge `0.0517` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.0842` n `127` status `ready` deltaP `10.4743` edge `0.0101` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.2819` n `54` status `ready` deltaP `4.8459` edge `0.0047` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.2819` n `54` status `ready` deltaP `4.8459` edge `0.0047` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.3597` n `127` status `ready` deltaP `4.0375` edge `0.0018` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3701` n `54` status `ready` deltaP `-1.4014` edge `0.0003` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3701` n `54` status `ready` deltaP `-1.4014` edge `0.0003` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.3829` n `54` status `ready` deltaP `2.301` edge `0.0078` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3829` n `54` status `ready` deltaP `2.301` edge `0.0078` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.4276` n `127` status `ready` deltaP `-0.1703` edge `-0.0019` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
