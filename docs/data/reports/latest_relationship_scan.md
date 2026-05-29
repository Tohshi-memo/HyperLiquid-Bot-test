# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T23:07:17.410503+00:00`
- Price records: `672`
- Market context records: `2290`
- Flow alert records: `8485`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9288`

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

- `news_risk_high->crypto_alt_24h` score `20.4157` n `43` status `ready` deltaP `50.0363` edge `1.4266` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5052` n `43` status `ready` deltaP `40.2091` edge `1.068` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5223` n `43` status `ready` deltaP `29.7925` edge `0.9597` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.2374` n `43` status `ready` deltaP `19.7674` edge `0.7794` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.8129` n `159` status `ready` deltaP `25.3758` edge `0.7498` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.6858` n `159` status `ready` deltaP `29.8933` edge `0.6222` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.5644` n `115` status `ready` deltaP `25.1585` edge `0.5038` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.1279` n `43` status `ready` deltaP `29.203` edge `0.4219` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.7382` n `159` status `ready` deltaP `22.6127` edge `0.3884` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9327` n `115` status `ready` deltaP `13.4783` edge `0.9318` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8486` n `43` status `ready` deltaP `32.6148` edge `0.3431` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6422` n `43` status `ready` deltaP `11.5351` edge `0.2685` maxDD `-1.3507`
- `news_risk_high->commodity_24h` score `3.5526` n `43` status `ready` deltaP `4.4614` edge `0.348` maxDD `-3.202`
- `news_risk_high->fx_24h` score `3.4769` n `43` status `ready` deltaP `36.3615` edge `0.0658` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.2525` n `115` status `ready` deltaP `13.3349` edge `0.2339` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.3681` n `159` status `ready` deltaP `22.9387` edge `0.127` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.1892` n `43` status `ready` deltaP `27.8892` edge `0.0149` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.1325` n `159` status `ready` deltaP `13.522` edge `0.2063` maxDD `-6.1656`
- `market_context_high->equity_4h` score `1.9597` n `159` status `ready` deltaP `17.3177` edge `0.1883` maxDD `-5.9024`
- `market_context_high->crypto_major_1h` score `1.8592` n `159` status `ready` deltaP `13.522` edge `0.1842` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
