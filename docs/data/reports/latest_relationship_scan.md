# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T08:37:17.013481+00:00`
- Price records: `672`
- Market context records: `2331`
- Flow alert records: `8601`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9168`

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

- `news_risk_high->crypto_alt_24h` score `20.7865` n `43` status `ready` deltaP `50.0363` edge `1.4575` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.5076` n `43` status `ready` deltaP `43.3341` edge `1.1307` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.2183` n `43` status `ready` deltaP `29.7925` edge `1.0177` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.5086` n `43` status `ready` deltaP `19.7674` edge `0.802` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.3521` n `128` status `ready` deltaP `24.3056` edge `0.4918` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.109` n `43` status `ready` deltaP `27.4669` edge `0.4319` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `6.7696` n `159` status `ready` deltaP `23.0892` edge `0.6781` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.7457` n `159` status `ready` deltaP `26.6921` edge `0.5652` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `5.9539` n `128` status `ready` deltaP `17.1875` edge `1.038` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3361` n `159` status `ready` deltaP `21.5457` edge `0.362` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.3264` n `43` status `ready` deltaP `11.8823` edge `0.3232` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0073` n `43` status `ready` deltaP `33.9868` edge `0.3543` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4308` n `128` status `ready` deltaP `14.8437` edge `0.2387` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4246` n `43` status `ready` deltaP `36.1879` edge `0.0626` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.1598` n `43` status `ready` deltaP `27.4319` edge `0.0155` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.0538` n `159` status `ready` deltaP `20.1948` edge `0.1191` maxDD `-2.2732`
- `market_context_high->equity_24h` score `1.8933` n `128` status `ready` deltaP `18.8369` edge `0.1849` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `1.8759` n `159` status `ready` deltaP `12.1747` edge `0.1939` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.6278` n `159` status `ready` deltaP `12.3244` edge `0.1729` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.6259` n `43` status `ready` deltaP `4.2878` edge `0.1886` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
