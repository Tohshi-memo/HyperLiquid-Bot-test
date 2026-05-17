# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T16:36:23.409053+00:00`
- Price records: `672`
- Market context records: `1030`
- Flow alert records: `4874`
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

- `market_context_high->crypto_major_24h` score `14.1625` n `184` status `ready` deltaP `32.859` edge `1.02` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.4957` n `184` status `ready` deltaP `11.2862` edge `0.4228` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.1003` n `184` status `ready` deltaP `11.1781` edge `0.2773` maxDD `-4.1434`
- `market_context_high->index_24h` score `2.3322` n `184` status `ready` deltaP `10.477` edge `0.2155` maxDD `-2.2794`
- `market_context_high->metal_24h` score `0.241` n `184` status `ready` deltaP `-6.2491` edge `0.3908` maxDD `-19.3245`
- `market_context_high->fx_1h` score `-0.0932` n `184` status `ready` deltaP `4.9532` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.5037` n `184` status `ready` deltaP `3.7522` edge `0.011` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6213` n `184` status `ready` deltaP `0.192` edge `0.0226` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.7162` n `184` status `ready` deltaP `0.7648` edge `0.016` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0081` n `184` status `ready` deltaP `1.9552` edge `0.0026` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.1325` n `184` status `ready` deltaP `5.8514` edge `-0.0094` maxDD `-7.9187`
- `market_context_high->crypto_alt_1h` score `-1.4051` n `184` status `ready` deltaP `0.0293` edge `-0.0087` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.4081` n `184` status `ready` deltaP `-0.3911` edge `0.0329` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.4381` n `184` status `ready` deltaP `1.7704` edge `-0.0369` maxDD `-7.7421`
- `market_context_high->equity_4h` score `-1.591` n `184` status `ready` deltaP `1.4581` edge `0.0729` maxDD `-10.5498`
- `market_context_high->crypto_alt_4h` score `-2.9403` n `184` status `ready` deltaP `0.5833` edge `0.0289` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.1507` n `184` status `ready` deltaP `7.1911` edge `0.0601` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1725` n `184` status `ready` deltaP `3.1049` edge `-0.0198` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.6127` n `184` status `ready` deltaP `-5.2492` edge `0.0507` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9915` n `184` status `ready` deltaP `-1.6901` edge `-0.1569` maxDD `-20.8181`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
