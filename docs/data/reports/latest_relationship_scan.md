# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T18:37:31.696399+00:00`
- Price records: `672`
- Market context records: `2269`
- Flow alert records: `8428`
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

- `news_risk_high->crypto_alt_24h` score `21.2649` n `43` status `ready` deltaP `51.4252` edge `1.4881` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7264` n `43` status `ready` deltaP `42.1188` edge `1.0737` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.2921` n `43` status `ready` deltaP `32.0494` edge `1.0088` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.1152` n `43` status `ready` deltaP `22.0243` edge `0.8375` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.9297` n `152` status `ready` deltaP `27.6958` edge `0.8274` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `8.586` n `115` status `ready` deltaP `28.2835` edge `0.5681` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `8.5424` n `152` status `ready` deltaP `32.5898` edge `0.6756` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `8.1495` n `43` status `ready` deltaP `32.328` edge `0.4862` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5519` n `152` status `ready` deltaP `22.2641` edge `0.3752` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.5032` n `115` status `ready` deltaP `15.7352` edge `0.9899` maxDD `-25.1408`
- `news_risk_high->index_24h` score `3.7783` n `43` status `ready` deltaP `12.5767` edge `0.2729` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7616` n `43` status `ready` deltaP `32.1575` edge `0.335` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6195` n `43` status `ready` deltaP `37.2295` edge `0.0719` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3887` n `115` status `ready` deltaP `14.3765` edge `0.2383` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2651` n `43` status `ready` deltaP `3.0725` edge `0.3333` maxDD `-3.202`
- `market_context_high->index_4h` score `2.6338` n `152` status `ready` deltaP `24.4143` edge `0.1393` maxDD `-2.2732`
- `market_context_high->equity_4h` score `2.4942` n `152` status `ready` deltaP `18.9746` edge `0.2218` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.2585` n `159` status `ready` deltaP `13.522` edge `0.2168` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0589` n `43` status `ready` deltaP `26.3648` edge `0.0142` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9372` n `159` status `ready` deltaP `13.522` edge `0.1907` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
