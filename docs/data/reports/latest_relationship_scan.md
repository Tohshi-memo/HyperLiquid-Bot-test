# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T12:22:30.932823+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->commodity_4h` score `1.0321` n `169` status `ready` deltaP `13.061` edge `0.0704` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7671` n `136` status `ready` deltaP `18.7634` edge `0.0196` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.6733` n `169` status `ready` deltaP `9.4214` edge `0.0276` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0806` n `169` status `ready` deltaP `8.6241` edge `0.0092` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1078` n `169` status `ready` deltaP `4.5663` edge `0.0009` maxDD `-0.613`
- `market_context_high->equity_24h` score `-0.4677` n `136` status `ready` deltaP `1.5165` edge `0.2643` maxDD `-21.0709`
- `market_context_high->index_24h` score `-0.5672` n `136` status `ready` deltaP `1.8261` edge `0.0937` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7536` n `169` status `ready` deltaP `-1.978` edge `-0.0019` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7782` n `169` status `ready` deltaP `-4.0596` edge `-0.0091` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-1.0596` n `136` status `ready` deltaP `-1.0411` edge `0.0468` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.1943` n `169` status `ready` deltaP `-1.6068` edge `-0.0023` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2037` n `169` status `ready` deltaP `-1.8843` edge `-0.0095` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.6066` n `169` status `ready` deltaP `-9.4276` edge `-0.041` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9242` n `169` status `ready` deltaP `-6.0002` edge `-0.0303` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.223` n `169` status `ready` deltaP `-11.4059` edge `-0.1255` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.6798` n `169` status `ready` deltaP `-10.6898` edge `-0.062` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-4.0399` n `169` status `ready` deltaP `-12.9122` edge `-0.1561` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3751` n `136` status `ready` deltaP `-11.9075` edge `-0.1409` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.403` n `136` status `ready` deltaP `-2.0236` edge `-0.104` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.6041` n `136` status `ready` deltaP `-5.3752` edge `-0.1957` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
