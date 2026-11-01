# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T07:52:27.212974+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6477`

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

- `market_context_high->unknown_24h` score `7033.0343` n `55` status `ready` deltaP `4.5139` edge `586.0561` maxDD `0.0`
- `market_context_high->unknown_4h` score `373.5807` n `55` status `ready` deltaP `5.3464` edge `31.1004` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `73.9965` n `111` status `ready` deltaP `-4.6946` edge `6.2263` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `53.5601` n `55` status `ready` deltaP `2.4143` edge `4.4583` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.6764` n `55` status `ready` deltaP `45.9249` edge `1.5238` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.0373` n `98` status `ready` deltaP `30.1587` edge `1.021` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.2642` n `55` status `ready` deltaP `59.7222` edge `0.2072` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.7062` n `55` status `ready` deltaP `46.31` edge `0.2812` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.7111` n `55` status `ready` deltaP `22.9878` edge `0.3521` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4221` n `55` status `ready` deltaP `30.1303` edge `0.2846` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.7961` n `108` status `ready` deltaP `17.9878` edge `0.4184` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3865` n `55` status `ready` deltaP `31.6768` edge `0.0961` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3236` n `55` status `ready` deltaP `5.5903` edge `0.3099` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.5701` n `55` status `ready` deltaP `11.3795` edge `0.3213` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.8988` n `55` status `ready` deltaP `-4.6465` edge `0.4262` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.551` n `55` status `ready` deltaP `18.3508` edge `0.0494` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.441` n `55` status `ready` deltaP `2.1285` edge `0.1584` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4096` n `55` status `ready` deltaP `8.1818` edge `0.1239` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3379` n `55` status `ready` deltaP `3.7752` edge `0.1534` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8612` n `55` status `ready` deltaP `10.7267` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
