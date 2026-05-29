# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T19:37:19.070531+00:00`
- Price records: `672`
- Market context records: `2274`
- Flow alert records: `8441`
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

- `news_risk_high->crypto_alt_24h` score `20.9695` n `43` status `ready` deltaP `51.078` edge `1.4658` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.6348` n `43` status `ready` deltaP `41.4244` edge `1.0707` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.0733` n `43` status `ready` deltaP `31.355` edge `0.9952` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.8364` n `43` status `ready` deltaP `21.3299` edge `0.8189` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.4618` n `156` status `ready` deltaP `26.7667` edge `0.7946` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `8.2796` n `115` status `ready` deltaP `27.589` edge `0.5472` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `8.1649` n `156` status `ready` deltaP `31.4415` edge `0.6518` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.8431` n `43` status `ready` deltaP `31.6335` edge `0.4653` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5411` n `156` status `ready` deltaP `21.9786` edge `0.3762` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.322` n `115` status `ready` deltaP `15.0408` edge `0.9713` maxDD `-25.1408`
- `news_risk_high->index_24h` score `3.7675` n `43` status `ready` deltaP `12.5767` edge `0.272` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7577` n `43` status `ready` deltaP `32.1575` edge `0.3345` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6051` n `43` status `ready` deltaP `37.2295` edge `0.0707` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3779` n `115` status `ready` deltaP `14.3765` edge `0.2374` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.3529` n `43` status `ready` deltaP `3.4197` edge `0.3383` maxDD `-3.202`
- `market_context_high->index_4h` score `2.5808` n `156` status `ready` deltaP `24.2769` edge `0.1358` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `2.3772` n `159` status `ready` deltaP `14.1208` edge `0.2227` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.3607` n `156` status `ready` deltaP `18.8203` edge `0.2117` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0735` n `43` status `ready` deltaP `26.5173` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `2.0355` n `159` status `ready` deltaP `14.1208` edge `0.1949` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
