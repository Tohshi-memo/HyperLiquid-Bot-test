# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T20:52:18.073859+00:00`
- Price records: `672`
- Market context records: `2279`
- Flow alert records: `8456`
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

- `news_risk_high->crypto_alt_24h` score `20.534` n `43` status `ready` deltaP `50.2099` edge `1.4353` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5318` n `43` status `ready` deltaP `40.5563` edge `1.0679` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.7651` n `43` status `ready` deltaP `30.4869` edge `0.9753` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.4466` n `43` status `ready` deltaP `20.4618` edge `0.7922` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.9522` n `115` status `ready` deltaP `26.721` edge `0.5257` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.8993` n `159` status `ready` deltaP `25.3758` edge `0.757` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.7206` n `159` status `ready` deltaP `29.8933` edge `0.6251` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.5157` n `43` status `ready` deltaP `30.7655` edge `0.4438` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.568` n `159` status `ready` deltaP `21.8505` edge `0.3793` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.0686` n `115` status `ready` deltaP `14.1727` edge `0.9446` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8057` n `43` status `ready` deltaP `32.6148` edge `0.3376` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6712` n `43` status `ready` deltaP `11.8823` edge `0.2686` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.5835` n `43` status `ready` deltaP `37.2295` edge `0.0689` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.5267` n `43` status `ready` deltaP `4.2878` edge `0.347` maxDD `-3.202`
- `market_context_high->index_24h` score `3.2815` n `115` status `ready` deltaP `13.6821` edge `0.234` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.4881` n `159` status `ready` deltaP `23.8533` edge `0.1309` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `2.2273` n `159` status `ready` deltaP `13.3723` edge `0.2152` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.1746` n `159` status `ready` deltaP `18.3848` edge `0.1991` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.099` n `43` status `ready` deltaP `26.8221` edge `0.0145` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9432` n `159` status `ready` deltaP `13.6717` edge `0.1902` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
