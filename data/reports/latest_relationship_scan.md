# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T03:07:13.260520+00:00`
- Price records: `672`
- Market context records: `1077`
- Flow alert records: `5006`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.372` n `160` status `ready` deltaP `35.0676` edge `1.1769` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.7659` n `160` status `ready` deltaP `12.0439` edge `0.5236` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.4007` n `160` status `ready` deltaP `14.6284` edge `0.4022` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.49` n `160` status `ready` deltaP `-2.4324` edge `0.5571` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.4581` n `160` status `ready` deltaP `14.7466` edge `0.304` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5477` n `162` status `ready` deltaP `8.8057` edge `0.1491` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.4196` n `162` status `ready` deltaP `13.3206` edge `0.1981` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.8429` n `162` status `ready` deltaP `7.2512` edge `0.0902` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6249` n `170` status `ready` deltaP `8.2599` edge `0.0287` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5819` n `170` status `ready` deltaP `3.3832` edge `0.0637` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.3421` n `170` status `ready` deltaP `7.7545` edge `0.0438` maxDD `-3.3594`
- `market_context_high->fx_1h` score `0.0152` n `170` status `ready` deltaP `6.8457` edge `0.0012` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1108` n `170` status `ready` deltaP `7.3811` edge `0.0026` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.1934` n `170` status `ready` deltaP `3.2635` edge `0.0464` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3849` n `162` status `ready` deltaP `7.2682` edge `0.1699` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6831` n `162` status `ready` deltaP `1.5846` edge `0.0015` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-1.0793` n `170` status `ready` deltaP `-1.4336` edge `0.0004` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.9671` n `162` status `ready` deltaP `4.4414` edge `-0.0864` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.0311` n `162` status `ready` deltaP `8.6645` edge `-0.1012` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.0914` n `160` status `ready` deltaP `4.9493` edge `-0.0217` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
