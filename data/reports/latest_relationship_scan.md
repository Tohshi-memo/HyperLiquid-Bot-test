# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T09:07:20.286885+00:00`
- Price records: `672`
- Market context records: `2333`
- Flow alert records: `8608`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `20.8105` n `43` status `ready` deltaP `50.0363` edge `1.4595` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.5496` n `43` status `ready` deltaP `43.3341` edge `1.1342` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.2711` n `43` status `ready` deltaP `29.7925` edge `1.0221` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.5482` n `43` status `ready` deltaP `19.7674` edge `0.8053` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.3587` n `130` status `ready` deltaP `17.6923` edge `1.0512` maxDD `-25.1408`
- `market_context_high->unknown_24h` score `7.2934` n `130` status `ready` deltaP `24.4258` edge `0.4861` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.1834` n `43` status `ready` deltaP `27.4669` edge `0.4381` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `6.6902` n `159` status `ready` deltaP `22.9368` edge `0.6725` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.6578` n `159` status `ready` deltaP `26.3872` edge `0.5599` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.3663` n `159` status `ready` deltaP `21.6981` edge `0.3635` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.372` n `43` status `ready` deltaP `11.8823` edge `0.327` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0065` n `43` status `ready` deltaP `33.9868` edge `0.3542` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4266` n `130` status `ready` deltaP `15.1202` edge `0.2365` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4222` n `43` status `ready` deltaP `36.1879` edge `0.0624` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.1342` n `43` status `ready` deltaP `27.127` edge `0.0154` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.0222` n `159` status `ready` deltaP `19.8899` edge `0.1185` maxDD `-2.2732`
- `market_context_high->equity_24h` score `1.9937` n `130` status `ready` deltaP `19.0412` edge `0.1919` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `1.8544` n `159` status `ready` deltaP `12.025` edge `0.1931` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.605` n `159` status `ready` deltaP `12.1747` edge `0.172` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.5275` n `43` status `ready` deltaP `4.2878` edge `0.1804` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
