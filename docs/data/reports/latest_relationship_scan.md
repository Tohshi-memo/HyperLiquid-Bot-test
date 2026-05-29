# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T23:37:19.058581+00:00`
- Price records: `672`
- Market context records: `2292`
- Flow alert records: `8491`
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

- `news_risk_high->crypto_alt_24h` score `20.4445` n `43` status `ready` deltaP `50.0363` edge `1.429` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5172` n `43` status `ready` deltaP `40.2091` edge `1.069` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5187` n `43` status `ready` deltaP `29.7925` edge `0.9594` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.2662` n `43` status `ready` deltaP `19.7674` edge `0.7818` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.7575` n `159` status `ready` deltaP `25.2233` edge `0.7462` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.6702` n `159` status `ready` deltaP `29.8933` edge `0.6209` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.5397` n `115` status `ready` deltaP `24.9849` edge `0.5029` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.1032` n `43` status `ready` deltaP `29.0294` edge `0.421` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.725` n `159` status `ready` deltaP `22.6127` edge `0.3873` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9514` n `115` status `ready` deltaP `13.4783` edge `0.9342` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8626` n `43` status `ready` deltaP `32.6148` edge `0.3449` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6578` n `43` status `ready` deltaP `11.5351` edge `0.2698` maxDD `-1.3507`
- `news_risk_high->commodity_24h` score `3.5094` n `43` status `ready` deltaP `4.4614` edge `0.3444` maxDD `-3.202`
- `news_risk_high->fx_24h` score `3.4419` n `43` status `ready` deltaP `36.0142` edge `0.0652` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.2681` n `115` status `ready` deltaP `13.3349` edge `0.2352` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.3305` n `159` status `ready` deltaP `22.6338` edge `0.1259` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.1904` n `43` status `ready` deltaP `27.8892` edge `0.015` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.1685` n `159` status `ready` deltaP `13.6717` edge `0.2083` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.9071` n `159` status `ready` deltaP `13.8214` edge `0.1862` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.8969` n `159` status `ready` deltaP `17.0128` edge `0.1851` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
