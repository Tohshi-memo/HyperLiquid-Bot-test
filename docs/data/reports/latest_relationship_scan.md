# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T06:37:26.068586+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8268`

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

- `market_context_high->crypto_alt_4h` score `8.1179` n `127` status `ready` deltaP `20.5864` edge `0.6307` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0737` n `54` status `ready` deltaP `38.5017` edge `0.3328` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0737` n `54` status `ready` deltaP `38.5017` edge `0.3328` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3171` n `127` status `ready` deltaP `23.712` edge `0.5005` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.1369` n `54` status `ready` deltaP `23.007` edge `0.4027` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.1369` n `54` status `ready` deltaP `23.007` edge `0.4027` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.3577` n `54` status `ready` deltaP `35.9022` edge `0.4046` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3577` n `54` status `ready` deltaP `35.9022` edge `0.4046` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.5746` n `138` status `ready` deltaP `13.1932` edge `0.1497` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0297` n `138` status `ready` deltaP `7.1205` edge `0.1189` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5571` n `127` status `ready` deltaP `14.6941` edge `0.053` maxDD `-1.6961`
- `risk_on_high->index_1h` score `-0.0418` n `64` status `ready` deltaP `4.5937` edge `0.0043` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0418` n `64` status `ready` deltaP `4.5937` edge `0.0043` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1946` n `138` status `ready` deltaP `6.8808` edge `0.004` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.1956` n `138` status `ready` deltaP `9.2163` edge `0.0092` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.2621` n `64` status `ready` deltaP `3.7238` edge `0.0138` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2621` n `64` status `ready` deltaP `3.7238` edge `0.0138` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.4015` n `64` status `ready` deltaP `2.6946` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4015` n `64` status `ready` deltaP `2.6946` edge `0.0037` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.471` n `138` status `ready` deltaP `8.5324` edge `0.0337` maxDD `-7.0778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
