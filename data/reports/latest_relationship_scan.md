# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T16:22:30.769379+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5374`

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

- `market_context_high->unknown_4h` score `33.4993` n `113` status `ready` deltaP `-0.4439` edge `2.8281` maxDD `-1.016`
- `market_context_high->fx_1h` score `-0.042` n `113` status `ready` deltaP `4.0088` edge `0.0028` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0427` n `113` status `ready` deltaP `7.1539` edge `0.0086` maxDD `-0.4545`
- `market_context_high->commodity_24h` score `-0.0869` n `63` status `ready` deltaP `6.9941` edge `0.0412` maxDD `-3.6055`
- `market_context_high->commodity_1h` score `-0.505` n `113` status `ready` deltaP `-0.1828` edge `0.0092` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6263` n `113` status `ready` deltaP `4.7838` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6853` n `113` status `ready` deltaP `-2.4853` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8039` n `113` status `ready` deltaP `-1.7807` edge `0.0317` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.1548` n `63` status `ready` deltaP `-4.7868` edge `-0.0136` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.3698` n `113` status `ready` deltaP `2.4985` edge `-0.0342` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.4834` n `63` status `ready` deltaP `3.497` edge `0.0103` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8928` n `113` status `ready` deltaP `4.7661` edge `-0.0185` maxDD `-5.3474`
- `market_context_high->index_24h` score `-2.0392` n `63` status `ready` deltaP `-1.2152` edge `-0.1251` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.1878` n `113` status `ready` deltaP `-8.3774` edge `-0.0372` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1846` n `113` status `ready` deltaP `-2.0097` edge `-0.0646` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.5828` n `63` status `ready` deltaP `-8.7798` edge `0.027` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.9099` n `113` status `ready` deltaP `-0.8386` edge `-0.0929` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.3825` n `63` status `ready` deltaP `-3.2739` edge `-0.279` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.9596` n `113` status `ready` deltaP `-12.7428` edge `-0.2452` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-11.6248` n `63` status `ready` deltaP `-16.9643` edge `-0.8489` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
