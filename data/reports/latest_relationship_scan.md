# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T21:06:27.531115+00:00`
- Price records: `672`
- Market context records: `1051`
- Flow alert records: `4931`
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

- `market_context_high->crypto_major_24h` score `14.1666` n `182` status `ready` deltaP `32.5799` edge `1.0222` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5013` n `182` status `ready` deltaP `11.6258` edge `0.421` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.7753` n `182` status `ready` deltaP `9.8402` edge `0.2445` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.187` n `182` status `ready` deltaP `9.1283` edge `0.2022` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.2868` n `182` status `ready` deltaP `-7.7298` edge `0.3473` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0714` n `184` status `ready` deltaP `5.4023` edge `0.0004` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4279` n `184` status `ready` deltaP `4.4454` edge `0.0127` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6408` n `184` status `ready` deltaP `-0.3515` edge `0.0246` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6862` n `184` status `ready` deltaP `0.9145` edge `0.0175` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-0.9469` n `184` status `ready` deltaP `6.0564` edge `0.0047` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.1205` n `183` status `ready` deltaP `0.6556` edge `0.0019` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.2483` n `184` status `ready` deltaP `0.384` edge `0.002` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3287` n `183` status `ready` deltaP `-0.0733` edge `0.0374` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.6933` n `183` status `ready` deltaP `1.0196` edge `0.0673` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.9081` n `184` status `ready` deltaP `2.9127` edge `-0.0336` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.785` n `183` status `ready` deltaP `1.2187` edge `0.0376` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.217` n `182` status `ready` deltaP `2.46` edge `-0.0212` maxDD `-19.2774`
- `market_context_high->crypto_major_4h` score `-3.2865` n `183` status `ready` deltaP `6.514` edge `0.0533` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.5309` n `183` status `ready` deltaP `-4.7364` edge `0.0541` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-4.0221` n `183` status `ready` deltaP `-1.1596` edge `-0.1646` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
