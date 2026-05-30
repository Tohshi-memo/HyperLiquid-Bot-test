# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T09:52:19.958255+00:00`
- Price records: `672`
- Market context records: `2337`
- Flow alert records: `8617`
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

- `news_risk_high->crypto_alt_24h` score `20.8729` n `43` status `ready` deltaP `50.0363` edge `1.4647` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.6415` n `43` status `ready` deltaP `43.5077` edge `1.1407` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.3491` n `43` status `ready` deltaP `29.7925` edge `1.0286` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.6298` n `43` status `ready` deltaP `19.7674` edge `0.8121` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.6318` n `133` status `ready` deltaP `18.4211` edge `1.0691` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.3233` n `43` status `ready` deltaP `27.6405` edge `0.4486` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.201` n `133` status `ready` deltaP `24.021` edge `0.4811` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.6158` n `159` status `ready` deltaP `22.9368` edge `0.6663` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.5576` n `159` status `ready` deltaP `25.9299` edge `0.5546` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.382` n `159` status `ready` deltaP `21.8505` edge `0.3638` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.4464` n `43` status `ready` deltaP `11.8823` edge `0.3332` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0049` n `43` status `ready` deltaP `33.9868` edge `0.354` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4174` n `43` status `ready` deltaP `36.1879` edge `0.062` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.4021` n `133` status `ready` deltaP `15.5193` edge `0.2318` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.1085` n `133` status `ready` deltaP `19.3361` edge `0.1995` maxDD `-6.8828`
- `news_risk_high->fx_4h` score `2.0952` n `43` status `ready` deltaP `26.6697` edge `0.0152` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.9858` n `159` status `ready` deltaP `19.585` edge `0.1175` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.8079` n `161` status `ready` deltaP `12.1788` edge `0.1882` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5609` n `161` status `ready` deltaP `12.1788` edge `0.1683` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.3511` n `43` status `ready` deltaP `4.2878` edge `0.1657` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
