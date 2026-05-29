# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T18:42:29.451135+00:00`
- Price records: `672`
- Market context records: `2270`
- Flow alert records: `8430`
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

- `news_risk_high->crypto_alt_24h` score `21.2625` n `43` status `ready` deltaP `51.4252` edge `1.4879` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7264` n `43` status `ready` deltaP `42.1188` edge `1.0737` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.2921` n `43` status `ready` deltaP `32.0494` edge `1.0088` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.114` n `43` status `ready` deltaP `22.0243` edge `0.8374` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.9345` n `152` status `ready` deltaP `27.6958` edge `0.8278` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `8.5848` n `115` status `ready` deltaP `28.2835` edge `0.568` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `8.546` n `152` status `ready` deltaP `32.5898` edge `0.6759` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `8.1483` n `43` status `ready` deltaP `32.328` edge `0.4861` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5543` n `152` status `ready` deltaP `22.2641` edge `0.3754` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.5024` n `115` status `ready` deltaP `15.7352` edge `0.9898` maxDD `-25.1408`
- `news_risk_high->index_24h` score `3.7783` n `43` status `ready` deltaP `12.5767` edge `0.2729` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7608` n `43` status `ready` deltaP `32.1575` edge `0.3349` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6195` n `43` status `ready` deltaP `37.2295` edge `0.0719` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3887` n `115` status `ready` deltaP `14.3765` edge `0.2383` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2651` n `43` status `ready` deltaP `3.0725` edge `0.3333` maxDD `-3.202`
- `market_context_high->index_4h` score `2.6326` n `152` status `ready` deltaP `24.4143` edge `0.1392` maxDD `-2.2732`
- `market_context_high->equity_4h` score `2.4942` n `152` status `ready` deltaP `18.9746` edge `0.2218` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.2561` n `159` status `ready` deltaP `13.522` edge `0.2166` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0577` n `43` status `ready` deltaP `26.3648` edge `0.0141` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.936` n `159` status `ready` deltaP `13.522` edge `0.1906` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
