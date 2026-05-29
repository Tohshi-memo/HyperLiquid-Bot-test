# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T21:37:24.534864+00:00`
- Price records: `672`
- Market context records: `2283`
- Flow alert records: `8466`
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

- `news_risk_high->crypto_alt_24h` score `20.3935` n `43` status `ready` deltaP `49.8627` edge `1.4259` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.4956` n `43` status `ready` deltaP `40.2091` edge `1.0672` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.6154` n `43` status `ready` deltaP `29.9661` edge `0.9663` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.2969` n `43` status `ready` deltaP `19.941` edge `0.7832` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.8345` n `159` status `ready` deltaP `25.3758` edge `0.7516` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `7.8133` n `115` status `ready` deltaP `26.2001` edge `0.5176` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `7.6918` n `159` status `ready` deltaP `29.8933` edge `0.6227` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.3768` n `43` status `ready` deltaP `30.2446` edge `0.4357` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.691` n `159` status `ready` deltaP `22.3079` edge `0.3865` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9714` n `115` status `ready` deltaP `13.6519` edge `0.9356` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8158` n `43` status `ready` deltaP `32.6148` edge `0.3389` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.629` n `43` status `ready` deltaP `11.5351` edge `0.2674` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.5727` n `43` status `ready` deltaP `37.2295` edge `0.068` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.5622` n `43` status `ready` deltaP `4.4614` edge `0.3488` maxDD `-3.202`
- `market_context_high->index_24h` score `3.2393` n `115` status `ready` deltaP `13.3349` edge `0.2328` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.4737` n `159` status `ready` deltaP `23.8533` edge `0.1297` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.138` n `43` status `ready` deltaP `27.2794` edge `0.0147` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.1242` n `159` status `ready` deltaP `13.2226` edge `0.2076` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.1156` n `159` status `ready` deltaP `18.2323` edge `0.1952` maxDD `-5.9024`
- `market_context_high->crypto_major_1h` score `1.8904` n `159` status `ready` deltaP `13.6717` edge `0.1858` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
