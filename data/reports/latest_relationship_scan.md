# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T13:22:28.903193+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6597`

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

- `market_context_high->unknown_24h` score `7031.5334` n `55` status `ready` deltaP `1.5625` edge `585.9507` maxDD `0.0`
- `market_context_high->unknown_4h` score `378.5723` n `55` status `ready` deltaP `5.0416` edge `31.5184` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.2995` n `55` status `ready` deltaP `3.3125` edge `6.1806` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.2133` n `55` status `ready` deltaP `43.8415` edge `1.4991` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.8396` n `98` status `ready` deltaP `29.6379` edge `1.008` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.853` n `55` status `ready` deltaP `55.9028` edge `0.1984` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.4809` n `55` status `ready` deltaP `45.7892` edge `0.2659` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.9377` n `55` status `ready` deltaP `23.75` edge `0.3659` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.5137` n `55` status `ready` deltaP `30.4352` edge `0.2902` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.0796` n `116` status `ready` deltaP `15.3017` edge `0.3766` maxDD `-7.4246`
- `market_context_high->equity_4h` score `3.3678` n `55` status `ready` deltaP `5.4379` edge `0.3146` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3551` n `55` status `ready` deltaP `31.5244` edge `0.0945` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4514` n `55` status `ready` deltaP `11.0322` edge `0.3084` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.761` n `55` status `ready` deltaP `-5.1673` edge `0.412` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5654` n `55` status `ready` deltaP `18.3508` edge `0.0506` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4925` n `55` status `ready` deltaP `2.7273` edge `0.1587` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3748` n `55` status `ready` deltaP `8.0321` edge `0.122` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3116` n `55` status `ready` deltaP `3.6255` edge `0.1522` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9115` n `55` status `ready` deltaP `11.3255` edge `0.0253` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5872` n `55` status `ready` deltaP `14.0855` edge `-0.0002` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
