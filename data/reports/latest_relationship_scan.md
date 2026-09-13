# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T22:22:29.743866+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `8503.5504` n `56` status `ready` deltaP `10.2093` edge `708.5813` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `436.03` n `82` status `ready` deltaP `-5.5499` edge `36.415` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.8011` n `82` status `ready` deltaP `36.5475` edge `1.3719` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.298` n `82` status `ready` deltaP `38.0236` edge `1.4184` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.0468` n `82` status `ready` deltaP `29.857` edge `0.8162` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.4372` n `82` status `ready` deltaP `53.6291` edge `0.2799` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `4.9466` n `56` status `ready` deltaP `39.8276` edge `0.1467` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.925` n `32` status `ready` deltaP `39.8276` edge `0.1449` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.925` n `32` status `ready` deltaP `39.8276` edge `0.1449` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.9139` n `82` status `ready` deltaP `28.0362` edge `0.268` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.985` n `32` status `ready` deltaP `54.9138` edge `0.0391` maxDD `-0.4662`
- `risk_on_and_context->fx_24h` score `2.985` n `32` status `ready` deltaP `54.9138` edge `0.0391` maxDD `-0.4662`
- `market_context_high->crypto_alt_24h` score `2.6847` n `56` status `ready` deltaP `1.835` edge `0.3794` maxDD `-9.7663`
- `risk_on_high->crypto_alt_24h` score `2.6758` n `32` status `ready` deltaP `-2.6293` edge `0.3741` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.6758` n `32` status `ready` deltaP `-2.6293` edge `0.3741` maxDD `-7.0204`
- `risk_on_high->commodity_4h` score `1.5977` n `54` status `ready` deltaP `22.4424` edge `0.0185` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.5977` n `54` status `ready` deltaP `22.4424` edge `0.0185` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.2149` n `129` status `ready` deltaP `18.308` edge `0.021` maxDD `-0.345`
- `market_context_high->fx_24h` score `1.1715` n `56` status `ready` deltaP `35.2709` edge `0.0138` maxDD `-2.2328`
- `news_risk_high->index_4h` score `0.4307` n `82` status `ready` deltaP `12.6524` edge `0.0337` maxDD `-0.6935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
