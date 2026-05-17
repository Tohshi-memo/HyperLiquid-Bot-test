# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T15:37:17.419953+00:00`
- Price records: `672`
- Market context records: `1026`
- Flow alert records: `4861`
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

- `market_context_high->crypto_major_24h` score `13.9099` n `188` status `ready` deltaP `32.7019` edge `1.0` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.4247` n `188` status `ready` deltaP `11.2236` edge `0.4173` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.2273` n `188` status `ready` deltaP `9.7379` edge `0.2486` maxDD `-5.5665`
- `market_context_high->index_24h` score `1.7032` n `188` status `ready` deltaP `9.0492` edge `0.1979` maxDD `-2.9701`
- `market_context_high->fx_1h` score `-0.0985` n `188` status `ready` deltaP `4.851` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.5655` n `188` status `ready` deltaP `3.2647` edge `0.0091` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5864` n `188` status `ready` deltaP `0.5382` edge `0.0232` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6289` n `188` status `ready` deltaP `1.4811` edge `0.0185` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9532` n `188` status `ready` deltaP `2.5817` edge `0.003` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.0529` n `188` status `ready` deltaP `5.0516` edge `-0.0183` maxDD `-10.0289`
- `market_context_high->index_4h` score `-1.3539` n `188` status `ready` deltaP `0.1524` edge `0.0338` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.4032` n `188` status `ready` deltaP `1.826` edge `0.0861` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.6886` n `188` status `ready` deltaP `0.8441` edge `-0.0388` maxDD `-8.3315`
- `market_context_high->crypto_alt_1h` score `-1.7559` n `188` status `ready` deltaP `-0.7357` edge `-0.0172` maxDD `-6.604`
- `market_context_high->metal_24h` score `-2.1881` n `188` status `ready` deltaP `-7.2783` edge `0.3312` maxDD `-28.8684`
- `market_context_high->crypto_alt_4h` score `-2.7138` n `188` status `ready` deltaP `0.7135` edge `0.0469` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.873` n `188` status `ready` deltaP `7.4371` edge `0.0816` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2197` n `188` status `ready` deltaP `2.2127` edge `-0.0199` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.4892` n `188` status `ready` deltaP `-3.931` edge `0.0522` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9874` n `188` status `ready` deltaP `-1.5471` edge `-0.1562` maxDD `-20.9091`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
