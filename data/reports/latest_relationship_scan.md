# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T09:37:31.127271+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9372`

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

- `risk_on_high->commodity_24h` score `7.0209` n `54` status `ready` deltaP `38.5017` edge `0.3284` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0209` n `54` status `ready` deltaP `38.5017` edge `0.3284` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.758` n `138` status `ready` deltaP `15.7521` edge `0.5621` maxDD `-4.9825`
- `risk_on_high->crypto_major_4h` score `6.2421` n `64` status `ready` deltaP `35.5564` edge `0.3684` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.2421` n `64` status `ready` deltaP `35.5564` edge `0.3684` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `5.998` n `138` status `ready` deltaP `23.7584` edge `0.4736` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `3.3161` n `64` status `ready` deltaP `11.5854` edge `0.2925` maxDD `-4.1379`
- `risk_on_and_context->crypto_alt_4h` score `3.3161` n `64` status `ready` deltaP `11.5854` edge `0.2925` maxDD `-4.1379`
- `market_context_high->crypto_major_1h` score `0.9549` n `150` status `ready` deltaP `7.2655` edge `0.1117` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.8668` n `150` status `ready` deltaP `9.1158` edge `0.1304` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.3921` n `138` status `ready` deltaP `13.081` edge `0.05` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.1764` n `76` status `ready` deltaP `7.1717` edge `0.0053` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1764` n `76` status `ready` deltaP `7.1717` edge `0.0053` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.14` n `150` status `ready` deltaP `7.8559` edge `0.0045` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2811` n `150` status `ready` deltaP `8.1776` edge `0.009` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3074` n `76` status `ready` deltaP `4.5462` edge `0.0163` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3074` n `76` status `ready` deltaP `4.5462` edge `0.0163` maxDD `-3.7781`
- `market_context_high->equity_1h` score `-0.4371` n `150` status `ready` deltaP `8.8408` edge `0.036` maxDD `-7.0778`
- `risk_on_high->metal_1h` score `-0.459` n `76` status `ready` deltaP `1.5285` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.459` n `76` status `ready` deltaP `1.5285` edge `0.0041` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
