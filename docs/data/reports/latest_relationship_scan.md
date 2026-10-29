# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T17:37:30.539322+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1622.0006` n `134` status `ready` deltaP `-0.3602` edge `135.2121` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `66.1028` n `134` status `ready` deltaP `6.8188` edge `5.4764` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.0578` n `134` status `ready` deltaP `25.8888` edge `0.0172` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3299` n `134` status `ready` deltaP `10.4545` edge `0.0105` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2223` n `134` status `ready` deltaP `12.8708` edge `0.0546` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0838` n `134` status `ready` deltaP `13.087` edge `0.0131` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0847` n `134` status `ready` deltaP `3.8788` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3271` n `134` status `ready` deltaP `1.4948` edge `0.0142` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4214` n `134` status `ready` deltaP `1.2036` edge `-0.0022` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.5093` n `134` status `ready` deltaP `1.4881` edge `0.0352` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.5492` n `134` status `ready` deltaP `4.7703` edge `0.0252` maxDD `-5.2213`
- `market_context_high->fx_24h` score `-0.8944` n `134` status `ready` deltaP `6.5765` edge `0.0147` maxDD `-0.9792`
- `market_context_high->index_1h` score `-0.9864` n `134` status `ready` deltaP `-3.5928` edge `-0.0024` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.2384` n `134` status `ready` deltaP `1.6512` edge `0.0167` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.6285` n `134` status `ready` deltaP `-3.0966` edge `-0.0297` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.7193` n `134` status `ready` deltaP `3.9257` edge `0.0181` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4638` n `134` status `ready` deltaP `-7.349` edge `-0.0243` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.7916` n `134` status `ready` deltaP `4.3502` edge `-0.0574` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-3.434` n `134` status `ready` deltaP `8.152` edge `-0.0648` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.6339` n `134` status `ready` deltaP `-0.3109` edge `-0.033` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
