# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T01:22:33.424449+00:00`
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

- `market_context_high->unknown_24h` score `16583.8202` n `59` status `ready` deltaP `12.0616` edge `1381.9098` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `378.7936` n `82` status `ready` deltaP `-5.8493` edge `31.6473` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.2253` n `82` status `ready` deltaP `33.1004` edge `1.3469` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0922` n `82` status `ready` deltaP `39.8459` edge `1.3891` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.4024` n `59` status `ready` deltaP `46.1806` edge `0.559` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.3268` n `59` status `ready` deltaP `23.055` edge `0.7896` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.1453` n `82` status `ready` deltaP `15.6928` edge `0.5855` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.0823` n `82` status `ready` deltaP `41.9588` edge `0.2448` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.0251` n `82` status `ready` deltaP `28.3918` edge `0.2749` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2819` n `59` status `ready` deltaP `42.7083` edge `0.0721` maxDD `0.0`
- `market_context_high->index_24h` score `3.961` n `59` status `ready` deltaP `42.5583` edge `0.0856` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.3753` n `59` status `ready` deltaP `9.1896` edge `0.1066` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.1413` n `82` status `ready` deltaP `7.9268` edge `0.0281` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.0422` n `53` status `ready` deltaP `5.3751` edge `0.0007` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.0422` n `53` status `ready` deltaP `5.3751` edge `0.0007` maxDD `-0.3081`
- `risk_on_high->index_1h` score `-0.0008` n `53` status `ready` deltaP `5.8553` edge `0.0005` maxDD `-0.1711`
- `risk_on_and_context->index_1h` score `-0.0008` n `53` status `ready` deltaP `5.8553` edge `0.0005` maxDD `-0.1711`
- `risk_on_high->crypto_alt_4h` score `-0.0245` n `51` status `ready` deltaP `6.274` edge `0.1225` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `-0.0245` n `51` status `ready` deltaP `6.274` edge `0.1225` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `-0.1006` n `53` status `ready` deltaP `1.4518` edge `0.003` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
