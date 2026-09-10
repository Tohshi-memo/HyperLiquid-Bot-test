# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T01:07:29.167769+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.8266` n `114` status `ready` deltaP `28.0793` edge `0.988` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.8266` n `114` status `ready` deltaP `28.0793` edge `0.988` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.826` n `236` status `ready` deltaP `20.6009` edge `0.6809` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `7.2856` n `114` status `ready` deltaP `23.1359` edge `1.1866` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2856` n `114` status `ready` deltaP `23.1359` edge `1.1866` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `7.0014` n `114` status `ready` deltaP `36.4677` edge `0.3775` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.0014` n `114` status `ready` deltaP `36.4677` edge `0.3775` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8651` n `114` status `ready` deltaP `26.2035` edge `0.3166` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8651` n `114` status `ready` deltaP `26.2035` edge `0.3166` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.8464` n `114` status `ready` deltaP `28.4448` edge `0.0518` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8464` n `114` status `ready` deltaP `28.4448` edge `0.0518` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.2027` n `236` status `ready` deltaP `11.9792` edge `0.1037` maxDD `0.0`
- `market_context_high->index_24h` score `2.1273` n `236` status `ready` deltaP `23.4493` edge `0.0603` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.4383` n `114` status `ready` deltaP `11.9792` edge `0.04` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.4383` n `114` status `ready` deltaP `11.9792` edge `0.04` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1228` n `114` status `ready` deltaP `4.2599` edge `0.1004` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1228` n `114` status `ready` deltaP `4.2599` edge `0.1004` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6642` n `114` status `ready` deltaP `18.951` edge `0.0744` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6642` n `114` status `ready` deltaP `18.951` edge `0.0744` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.53` n `114` status `ready` deltaP `15.1513` edge `-0.0037` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
