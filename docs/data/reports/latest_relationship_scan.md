# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T18:22:23.968771+00:00`
- Price records: `672`
- Market context records: `2268`
- Flow alert records: `8425`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

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

- `news_risk_high->crypto_alt_24h` score `21.3627` n `43` status `ready` deltaP `51.5988` edge `1.4951` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7487` n `43` status `ready` deltaP `42.2925` edge `1.0744` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.354` n `43` status `ready` deltaP `32.223` edge `1.0128` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.2011` n `43` status `ready` deltaP `22.198` edge `0.8435` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.8959` n `151` status `ready` deltaP `27.6783` edge `0.8247` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `8.6695` n `115` status `ready` deltaP `28.4571` edge `0.5739` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `8.5071` n `151` status `ready` deltaP `32.6291` edge `0.6724` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `8.233` n `43` status `ready` deltaP `32.5016` edge `0.492` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `5.5591` n `115` status `ready` deltaP `15.9089` edge `0.9959` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4812` n `151` status `ready` deltaP `22.0855` edge `0.3705` maxDD `-1.8773`
- `news_risk_high->index_24h` score `3.7807` n `43` status `ready` deltaP `12.5767` edge `0.2731` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7515` n `43` status `ready` deltaP `32.1575` edge `0.3337` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6219` n `43` status `ready` deltaP `37.2295` edge `0.0721` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3911` n `115` status `ready` deltaP `14.3765` edge `0.2385` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2272` n `43` status `ready` deltaP `2.8989` edge `0.3313` maxDD `-3.202`
- `market_context_high->index_4h` score `2.635` n `151` status `ready` deltaP `24.4448` edge `0.1392` maxDD `-2.2732`
- `market_context_high->equity_4h` score `2.4694` n `151` status `ready` deltaP `19.0094` edge `0.2195` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.2477` n `159` status `ready` deltaP `13.522` edge `0.2159` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0589` n `43` status `ready` deltaP `26.3648` edge `0.0142` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.9929` n `115` status `ready` deltaP `19.766` edge `0.187` maxDD `-6.8828`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
