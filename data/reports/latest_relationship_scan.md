# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T16:07:13.656026+00:00`
- Price records: `672`
- Market context records: `1028`
- Flow alert records: `4867`
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

- `market_context_high->crypto_major_24h` score `14.0578` n `186` status `ready` deltaP `32.7805` edge `1.0118` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.474` n `186` status `ready` deltaP `11.2549` edge `0.4212` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.7087` n `186` status `ready` deltaP `10.4484` edge `0.2637` maxDD `-4.6108`
- `market_context_high->index_24h` score `2.0216` n `186` status `ready` deltaP `9.7535` edge `0.2067` maxDD `-2.5941`
- `market_context_high->fx_1h` score `-0.0857` n `186` status `ready` deltaP `5.0979` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.5225` n `186` status `ready` deltaP `3.6974` edge `0.0098` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5799` n `186` status `ready` deltaP `0.5601` edge `0.0236` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.698` n `186` status `ready` deltaP `0.932` edge `0.0164` maxDD `-3.7959`
- `market_context_high->metal_24h` score `-0.9716` n `186` status `ready` deltaP `-6.7712` edge `0.3608` maxDD `-24.0633`
- `market_context_high->fx_4h` score `-0.9982` n `186` status `ready` deltaP `2.0784` edge `0.0026` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2847` n `186` status `ready` deltaP `5.5196` edge `-0.0123` maxDD `-8.5243`
- `market_context_high->index_4h` score `-1.379` n `186` status `ready` deltaP `-0.1164` edge `0.0335` maxDD `-6.1444`
- `market_context_high->crypto_alt_1h` score `-1.4687` n `186` status `ready` deltaP `-0.2849` edge `-0.0119` maxDD `-5.3538`
- `market_context_high->equity_4h` score `-1.4958` n `186` status `ready` deltaP `1.5687` edge `0.0801` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.6017` n `186` status `ready` deltaP `1.1509` edge `-0.0389` maxDD `-8.2625`
- `market_context_high->crypto_alt_4h` score `-2.8111` n `186` status `ready` deltaP `0.6524` edge `0.0392` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.9905` n `186` status `ready` deltaP `7.3188` edge `0.0726` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1968` n `186` status `ready` deltaP `2.6527` edge `-0.0199` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5594` n `186` status `ready` deltaP `-4.583` edge `0.0507` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9866` n `186` status `ready` deltaP `-1.6194` edge `-0.1564` maxDD `-20.8458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
