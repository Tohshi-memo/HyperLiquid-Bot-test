# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T11:07:23.033253+00:00`
- Price records: `672`
- Market context records: `2656`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `8.0621` n `121` status `ready` deltaP `17.3052` edge `0.5893` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `7.3427` n `121` status `ready` deltaP `12.1571` edge `0.8802` maxDD `-19.9486`
- `market_context_high->crypto_alt_4h` score `5.2412` n `121` status `ready` deltaP `25.1499` edge `0.537` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.951` n `121` status `ready` deltaP `15.923` edge `0.4041` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9379` n `121` status `ready` deltaP `10.0899` edge `0.1992` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0563` n `133` status `ready` deltaP `9.0991` edge `0.1461` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.5735` n `121` status `ready` deltaP `9.9705` edge `0.0794` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.5705` n `133` status `ready` deltaP `7.449` edge `0.1173` maxDD `-4.2199`
- `market_context_high->metal_4h` score `0.0493` n `121` status `ready` deltaP `6.9202` edge `0.0396` maxDD `-2.5301`
- `market_context_high->index_4h` score `-0.0259` n `121` status `ready` deltaP `7.4985` edge `0.032` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0361` n `133` status `ready` deltaP `2.9445` edge `0.0353` maxDD `-1.9684`
- `market_context_high->index_1h` score `-0.178` n `133` status `ready` deltaP `3.2507` edge `0.0129` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.3994` n `133` status `ready` deltaP `-1.4205` edge `0.0029` maxDD `-0.2373`
- `market_context_high->commodity_1h` score `-0.441` n `133` status `ready` deltaP `3.5298` edge `0.0036` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.4536` n `121` status `ready` deltaP `7.3935` edge `0.0001` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.5962` n `133` status `ready` deltaP `-1.2809` edge `0.0015` maxDD `-1.8854`
- `market_context_high->fx_4h` score `-0.7587` n `121` status `ready` deltaP `-1.3518` edge `0.0115` maxDD `-0.5902`
- `market_context_high->commodity_4h` score `-1.1182` n `121` status `ready` deltaP `4.6739` edge `0.0175` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.1678` n `133` status `ready` deltaP `-3.7886` edge `0.0118` maxDD `-2.7085`
- `market_context_high->equity_24h` score `-1.4413` n `121` status `ready` deltaP `7.0263` edge `-0.0692` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
