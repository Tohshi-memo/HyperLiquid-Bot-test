# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T20:52:15.364355+00:00`
- Price records: `672`
- Market context records: `1050`
- Flow alert records: `4928`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8668`

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

- `market_context_high->crypto_major_24h` score `14.1965` n `182` status `ready` deltaP `32.6839` edge `1.024` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5225` n `182` status `ready` deltaP `11.6061` edge `0.4229` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.828` n `182` status `ready` deltaP `9.9738` edge `0.248` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.2158` n `182` status `ready` deltaP `9.2623` edge `0.2037` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.3571` n `182` status `ready` deltaP `-7.6006` edge `0.3523` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.08` n `184` status `ready` deltaP `5.2526` edge `0.0003` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4399` n `184` status `ready` deltaP `4.2957` edge `0.0127` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6396` n `184` status `ready` deltaP `-0.3515` edge `0.0247` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6874` n `184` status `ready` deltaP `0.9145` edge `0.0174` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-0.9481` n `184` status `ready` deltaP `6.0564` edge `0.0046` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.1339` n `183` status `ready` deltaP `0.5031` edge `0.0018` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.2471` n `184` status `ready` deltaP `0.384` edge `0.0021` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3287` n `183` status `ready` deltaP `-0.0733` edge `0.0374` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.6679` n `183` status `ready` deltaP `1.172` edge `0.0684` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.9045` n `184` status `ready` deltaP `2.9127` edge `-0.0333` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.7608` n `183` status `ready` deltaP `1.3711` edge `0.0386` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.2207` n `182` status `ready` deltaP `2.3893` edge `-0.0212` maxDD `-19.2774`
- `market_context_high->crypto_major_4h` score `-3.2395` n `183` status `ready` deltaP `6.6665` edge `0.0562` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.5574` n `183` status `ready` deltaP `-4.8888` edge `0.0529` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-4.0089` n `183` status `ready` deltaP `-1.1596` edge `-0.1629` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
