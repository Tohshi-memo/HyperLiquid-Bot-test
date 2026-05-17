# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T14:52:12.536869+00:00`
- Price records: `672`
- Market context records: `1022`
- Flow alert records: `4851`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `13.7157` n `191` status `ready` deltaP `32.584` edge `0.9846` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.3657` n `191` status `ready` deltaP `11.1769` edge `0.4127` maxDD `-9.5387`
- `market_context_high->equity_24h` score `1.6201` n `191` status `ready` deltaP `8.7069` edge `0.2287` maxDD `-6.4722`
- `market_context_high->index_24h` score `1.2355` n `191` status `ready` deltaP `8.0274` edge `0.1851` maxDD `-3.5195`
- `market_context_high->fx_1h` score `-0.132` n `191` status `ready` deltaP `4.223` edge `0.0005` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5263` n `191` status `ready` deltaP `2.2831` edge `0.0217` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6092` n `191` status `ready` deltaP `2.8686` edge `0.0081` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6981` n `191` status `ready` deltaP `-0.1983` edge `0.0188` maxDD `-4.3858`
- `market_context_high->fx_4h` score `-0.8908` n `191` status `ready` deltaP `3.3169` edge `0.0033` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2819` n `191` status `ready` deltaP `4.5984` edge `-0.0227` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.3405` n `191` status `ready` deltaP `0.5451` edge `0.0323` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.3457` n `191` status `ready` deltaP `2.0496` edge `0.0894` maxDD `-10.5498`
- `market_context_high->crypto_alt_1h` score `-1.3598` n `191` status `ready` deltaP `-1.1639` edge `-0.0226` maxDD `-8.1842`
- `market_context_high->metal_1h` score `-1.7446` n `191` status `ready` deltaP `0.8559` edge `-0.0391` maxDD `-8.5553`
- `market_context_high->crypto_alt_4h` score `-2.6644` n `191` status `ready` deltaP `0.7909` edge `0.0505` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.7642` n `191` status `ready` deltaP `7.598` edge `0.0896` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2537` n `191` status `ready` deltaP `1.5747` edge `-0.02` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.4038` n `191` status `ready` deltaP `-3.2835` edge `0.055` maxDD `-13.0076`
- `market_context_high->metal_24h` score `-3.9654` n `191` status `ready` deltaP `-8.0127` edge `0.2888` maxDD `-35.9335`
- `market_context_high->metal_4h` score `-4.1107` n `191` status `ready` deltaP `-2.1445` edge `-0.1582` maxDD `-21.6945`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
