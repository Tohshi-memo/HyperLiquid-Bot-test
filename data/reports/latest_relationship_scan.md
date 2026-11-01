# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T07:37:26.302277+00:00`
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

- `market_context_high->unknown_24h` score `7033.1202` n `55` status `ready` deltaP `4.6875` edge `586.0621` maxDD `0.0`
- `market_context_high->unknown_4h` score `373.2855` n `55` status `ready` deltaP `5.3464` edge `31.0758` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `72.2206` n `110` status `ready` deltaP `-4.8584` edge `6.0794` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `48.8909` n `55` status `ready` deltaP `2.4143` edge `4.0692` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.7083` n `55` status `ready` deltaP `46.0985` edge `1.5253` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.092` n `98` status `ready` deltaP `30.3324` edge `1.0244` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.2793` n `55` status `ready` deltaP `59.8958` edge `0.2073` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.717` n `55` status `ready` deltaP `46.31` edge `0.2821` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.7413` n `55` status `ready` deltaP `23.1402` edge `0.3536` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4463` n `55` status `ready` deltaP `30.2827` edge `0.2856` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.8263` n `108` status `ready` deltaP `18.1402` edge `0.4199` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3877` n `55` status `ready` deltaP `31.6768` edge `0.0962` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3394` n `55` status `ready` deltaP `5.7428` edge `0.3102` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.5971` n `55` status `ready` deltaP `11.5531` edge `0.3236` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9344` n `55` status `ready` deltaP `-4.4728` edge `0.4296` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5632` n `55` status `ready` deltaP `18.5033` edge `0.0494` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4422` n `55` status `ready` deltaP `2.1285` edge `0.1585` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4132` n `55` status `ready` deltaP `8.1818` edge `0.1242` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3595` n `55` status `ready` deltaP `3.9249` edge `0.1542` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8612` n `55` status `ready` deltaP `10.7267` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
