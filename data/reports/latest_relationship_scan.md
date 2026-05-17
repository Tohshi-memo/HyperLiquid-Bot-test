# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T22:07:16.556460+00:00`
- Price records: `672`
- Market context records: `1055`
- Flow alert records: `4943`
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

- `market_context_high->crypto_major_24h` score `14.5074` n `180` status `ready` deltaP `33.2353` edge `1.0379` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.6127` n `180` status `ready` deltaP `11.6993` edge `0.4298` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.0438` n `180` status `ready` deltaP `10.3268` edge `0.2553` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.3986` n `180` status `ready` deltaP `9.6079` edge `0.2083` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.0303` n `180` status `ready` deltaP `-7.451` edge `0.3637` maxDD `-11.2533`
- `market_context_high->fx_1h` score `-0.0717` n `182` status `ready` deltaP `5.3975` edge `0.0004` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4582` n `182` status `ready` deltaP `4.111` edge `0.0124` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5893` n `182` status `ready` deltaP `-0.2336` edge `0.0252` maxDD `-4.1532`
- `market_context_high->commodity_1h` score `-0.6341` n `182` status `ready` deltaP `1.2963` edge `0.0193` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.7225` n `181` status `ready` deltaP `0.7521` edge `0.002` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-0.7938` n `182` status `ready` deltaP `6.0966` edge `0.0057` maxDD `-6.9993`
- `market_context_high->crypto_alt_1h` score `-1.2622` n `182` status `ready` deltaP `0.4064` edge `0.0007` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3466` n `181` status `ready` deltaP `-0.3571` edge `0.0378` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.4949` n `181` status `ready` deltaP `1.2431` edge `0.0679` maxDD `-10.0609`
- `market_context_high->metal_1h` score `-1.7264` n `182` status `ready` deltaP `3.1026` edge `-0.0336` maxDD `-6.8095`
- `market_context_high->crypto_alt_4h` score `-2.775` n `181` status `ready` deltaP `1.3214` edge `0.0354` maxDD `-15.0367`
- `market_context_high->crypto_major_4h` score `-3.0529` n `181` status `ready` deltaP `6.5625` edge `0.0501` maxDD `-20.8606`
- `market_context_high->fx_24h` score `-3.1852` n `180` status `ready` deltaP `3.0719` edge `-0.0212` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5379` n `181` status `ready` deltaP `-4.8089` edge `0.054` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.7327` n `181` status `ready` deltaP `-0.678` edge `-0.1607` maxDD `-18.7332`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
