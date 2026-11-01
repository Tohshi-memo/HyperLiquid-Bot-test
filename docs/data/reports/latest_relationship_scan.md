# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T08:52:26.083634+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6505`

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

- `market_context_high->unknown_24h` score `7032.7598` n `55` status `ready` deltaP `3.9931` edge `586.0367` maxDD `0.0`
- `market_context_high->unknown_4h` score `373.2303` n `55` status `ready` deltaP `5.3464` edge `31.0712` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `66.9306` n `115` status `ready` deltaP `-5.5076` edge `5.6429` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `57.9004` n `55` status `ready` deltaP `2.7137` edge `4.818` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.5284` n `55` status `ready` deltaP `45.2304` edge `1.5161` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.8648` n `98` status `ready` deltaP `29.6379` edge `1.0101` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.1846` n `55` status `ready` deltaP `59.0278` edge `0.2052` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.6527` n `55` status `ready` deltaP `46.1364` edge `0.2779` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.6493` n `55` status `ready` deltaP `22.5305` edge `0.35` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3627` n `55` status `ready` deltaP `29.673` edge `0.2827` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.7344` n `108` status `ready` deltaP `17.5305` edge `0.4163` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3841` n `55` status `ready` deltaP `31.6768` edge `0.0959` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3042` n `55` status `ready` deltaP `5.4379` edge `0.3093` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.472` n `55` status `ready` deltaP `10.8586` edge `0.3122` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7867` n `55` status `ready` deltaP `-5.1673` edge `0.4153` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.551` n `55` status `ready` deltaP `18.3508` edge `0.0494` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.3895` n `55` status `ready` deltaP `1.6794` edge `0.1571` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3256` n `55` status `ready` deltaP `7.7327` edge `0.1199` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.2516` n `55` status `ready` deltaP `3.3261` edge `0.1492` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.86` n `55` status `ready` deltaP `10.7267` edge `0.025` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
