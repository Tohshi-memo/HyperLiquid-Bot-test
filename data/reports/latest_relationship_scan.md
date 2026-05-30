# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T05:37:19.024362+00:00`
- Price records: `672`
- Market context records: `2318`
- Flow alert records: `8564`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9292`

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

- `news_risk_high->crypto_alt_24h` score `20.7217` n `43` status `ready` deltaP `50.0363` edge `1.4521` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.1267` n `43` status `ready` deltaP `42.2925` edge `1.1059` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.8895` n `43` status `ready` deltaP `29.7925` edge `0.9903` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3814` n `43` status `ready` deltaP `19.7674` edge `0.7914` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.3379` n `116` status `ready` deltaP `23.4974` edge `0.496` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.1649` n `159` status `ready` deltaP `23.5465` edge `0.708` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.1471` n `159` status `ready` deltaP `28.0641` edge `0.5895` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `6.8174` n `43` status `ready` deltaP `27.4669` edge `0.4076` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.4134` n `159` status `ready` deltaP `22.003` edge `0.3654` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.1199` n `116` status `ready` deltaP `13.7931` edge `0.9537` maxDD `-25.1408`
- `news_risk_high->index_24h` score `4.0413` n `43` status `ready` deltaP `11.7087` edge `0.3006` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.9718` n `43` status `ready` deltaP `33.5294` edge `0.3528` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.606` n `116` status `ready` deltaP `13.6734` edge `0.2611` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4107` n `43` status `ready` deltaP `36.0142` edge `0.0626` maxDD `-0.1442`
- `market_context_high->index_4h` score `2.2589` n `159` status `ready` deltaP `22.024` edge `0.124` maxDD `-2.2732`
- `news_risk_high->commodity_24h` score `2.2343` n `43` status `ready` deltaP `4.2878` edge `0.2393` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.2208` n `43` status `ready` deltaP `28.1941` edge `0.0155` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9838` n `159` status `ready` deltaP `12.9232` edge `0.1979` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.7332` n `159` status `ready` deltaP `13.0729` edge `0.1767` maxDD `-4.2199`
- `market_context_high->equity_24h` score `1.5446` n `116` status `ready` deltaP `17.4629` edge `0.165` maxDD `-6.8828`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
