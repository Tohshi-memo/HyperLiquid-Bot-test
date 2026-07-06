# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T06:37:29.153905+00:00`
- Price records: `672`
- Market context records: `5853`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10104`

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

- `news_risk_high->fx_4h` score `3.6999` n `30` status `ready` deltaP `38.628` edge `0.0554` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9759` n `30` status `ready` deltaP `23.9321` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8963` n `30` status `ready` deltaP `11.8363` edge `0.0827` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7419` n `254` status `ready` deltaP `7.8464` edge `0.1553` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.277` n `30` status `ready` deltaP `5.4691` edge `0.0452` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3278` n `254` status `ready` deltaP `0.9925` edge `-0.0001` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.3962` n `30` status `ready` deltaP `1.8363` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4422` n `254` status `ready` deltaP `4.326` edge `0.035` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5169` n `254` status `ready` deltaP `3.2274` edge `0.0025` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5706` n `254` status `ready` deltaP `-1.4475` edge `-0.0034` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.5807` n `254` status `ready` deltaP `0.9041` edge `0.0043` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8275` n `254` status `ready` deltaP `3.6211` edge `0.039` maxDD `-6.2348`
- `market_context_high->equity_24h` score `-0.8778` n `228` status `ready` deltaP `17.0321` edge `0.3212` maxDD `-31.6316`
- `market_context_high->crypto_alt_1h` score `-0.9769` n `254` status `ready` deltaP `2.3457` edge `0.0364` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.196` n `254` status `ready` deltaP `0.2401` edge `0.0138` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2237` n `30` status `ready` deltaP `-12.2455` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7324` n `254` status `ready` deltaP `-3.7342` edge `-0.0023` maxDD `-2.2593`
- `news_risk_high->commodity_4h` score `-1.759` n `30` status `ready` deltaP `-13.1199` edge `-0.0505` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8117` n `228` status `ready` deltaP `4.8794` edge `0.017` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0471` n `254` status `ready` deltaP `-4.2179` edge `-0.038` maxDD `-8.3735`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
