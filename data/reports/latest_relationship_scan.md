# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T05:22:22.071280+00:00`
- Price records: `672`
- Market context records: `2317`
- Flow alert records: `8561`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9291`

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

- `news_risk_high->crypto_alt_24h` score `20.7241` n `43` status `ready` deltaP `50.0363` edge `1.4523` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.1027` n `43` status `ready` deltaP `42.2925` edge `1.1039` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.8667` n `43` status `ready` deltaP `29.7925` edge `0.9884` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3778` n `43` status `ready` deltaP `19.7674` edge `0.7911` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.2539` n `115` status `ready` deltaP `23.4224` edge `0.4895` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.1709` n `159` status `ready` deltaP `23.5465` edge `0.7085` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.1653` n `159` status `ready` deltaP `28.2165` edge `0.59` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `6.8174` n `43` status `ready` deltaP `27.4669` edge `0.4076` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.4388` n `159` status `ready` deltaP `22.1554` edge `0.3665` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.0239` n `115` status `ready` deltaP `13.4783` edge `0.9435` maxDD `-25.1408`
- `news_risk_high->index_24h` score `4.0173` n `43` status `ready` deltaP `11.7087` edge `0.2986` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.96` n `43` status `ready` deltaP `33.377` edge `0.3523` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.6276` n `115` status `ready` deltaP `13.5085` edge `0.264` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4119` n `43` status `ready` deltaP `36.0142` edge `0.0627` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `2.2835` n `43` status `ready` deltaP `4.2878` edge `0.2434` maxDD `-3.202`
- `market_context_high->index_4h` score `2.2601` n `159` status `ready` deltaP `22.024` edge `0.1241` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.2086` n `43` status `ready` deltaP `28.0416` edge `0.0155` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9934` n `159` status `ready` deltaP `12.9232` edge `0.1987` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.7428` n `159` status `ready` deltaP `13.0729` edge `0.1775` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.5217` n `159` status `ready` deltaP `14.5738` edge `0.1701` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
