# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T00:22:18.402368+00:00`
- Price records: `672`
- Market context records: `2296`
- Flow alert records: `8500`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9289`

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

- `news_risk_high->crypto_alt_24h` score `20.5405` n `43` status `ready` deltaP `50.0363` edge `1.437` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5779` n `43` status `ready` deltaP `40.3827` edge `1.0729` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5487` n `43` status `ready` deltaP `29.7925` edge `0.9619` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.343` n `43` status `ready` deltaP `19.7674` edge `0.7882` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.6915` n `159` status `ready` deltaP `25.2233` edge `0.7407` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.645` n `159` status `ready` deltaP `29.8933` edge `0.6188` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.4128` n `115` status `ready` deltaP `24.464` edge `0.4958` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `6.9763` n `43` status `ready` deltaP `28.5085` edge `0.4139` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.707` n `159` status `ready` deltaP `22.6127` edge `0.3858` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.0013` n `115` status `ready` deltaP `13.4783` edge `0.9406` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8759` n `43` status `ready` deltaP `32.6148` edge `0.3466` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.689` n `43` status `ready` deltaP `11.5351` edge `0.2724` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.4347` n `43` status `ready` deltaP `36.0142` edge `0.0646` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.3798` n `43` status `ready` deltaP `4.4614` edge `0.3336` maxDD `-3.202`
- `market_context_high->index_24h` score `3.2993` n `115` status `ready` deltaP `13.3349` edge `0.2378` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.2929` n `159` status `ready` deltaP `22.3289` edge `0.1248` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.2062` n `43` status `ready` deltaP `28.0416` edge `0.0153` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.1445` n `159` status `ready` deltaP `13.522` edge `0.2073` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.9047` n `159` status `ready` deltaP `13.8214` edge `0.186` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.8523` n `159` status `ready` deltaP `16.8604` edge `0.1824` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
