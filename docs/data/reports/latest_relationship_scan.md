# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T00:07:23.365517+00:00`
- Price records: `672`
- Market context records: `2295`
- Flow alert records: `8497`
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

- `news_risk_high->crypto_alt_24h` score `20.5093` n `43` status `ready` deltaP `50.0363` edge `1.4344` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5472` n `43` status `ready` deltaP `40.2091` edge `1.0715` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5331` n `43` status `ready` deltaP `29.7925` edge `0.9606` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3166` n `43` status `ready` deltaP `19.7674` edge `0.786` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.7131` n `159` status `ready` deltaP `25.2233` edge `0.7425` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.6558` n `159` status `ready` deltaP `29.8933` edge `0.6197` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.4375` n `115` status `ready` deltaP `24.6376` edge `0.4967` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.001` n `43` status `ready` deltaP `28.6821` edge `0.4148` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.7166` n `159` status `ready` deltaP `22.6127` edge `0.3866` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9842` n `115` status `ready` deltaP `13.4783` edge `0.9384` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8728` n `43` status `ready` deltaP `32.6148` edge `0.3462` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6746` n `43` status `ready` deltaP `11.5351` edge `0.2712` maxDD `-1.3507`
- `news_risk_high->commodity_24h` score `3.4362` n `43` status `ready` deltaP `4.4614` edge `0.3383` maxDD `-3.202`
- `news_risk_high->fx_24h` score `3.4359` n `43` status `ready` deltaP `36.0142` edge `0.0647` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.2849` n `115` status `ready` deltaP `13.3349` edge `0.2366` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.3087` n `159` status `ready` deltaP `22.4814` edge `0.1251` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.205` n `43` status `ready` deltaP `28.0416` edge `0.0152` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.1685` n `159` status `ready` deltaP `13.6717` edge `0.2083` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.9263` n `159` status `ready` deltaP `13.9711` edge `0.1868` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.8631` n `159` status `ready` deltaP `16.8604` edge `0.1833` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
