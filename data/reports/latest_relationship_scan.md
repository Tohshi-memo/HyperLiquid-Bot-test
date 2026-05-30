# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T10:52:20.388626+00:00`
- Price records: `672`
- Market context records: `2341`
- Flow alert records: `8629`
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

- `news_risk_high->crypto_alt_24h` score `20.9893` n `43` status `ready` deltaP `50.0363` edge `1.4744` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.7911` n `43` status `ready` deltaP `44.0286` edge `1.1497` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.4547` n `43` status `ready` deltaP `29.7925` edge `1.0374` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.7666` n `43` status `ready` deltaP `19.7674` edge `0.8235` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `10.1099` n `137` status `ready` deltaP `19.3431` edge `1.1028` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.4481` n `43` status `ready` deltaP `27.6405` edge `0.459` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.2179` n `137` status `ready` deltaP `24.2625` edge `0.4809` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.5412` n `159` status `ready` deltaP `22.7843` edge `0.6611` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.4646` n `159` status `ready` deltaP `25.4726` edge `0.5499` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.4326` n `159` status `ready` deltaP `22.003` edge `0.367` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.5544` n `43` status `ready` deltaP `11.8823` edge `0.3422` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0239` n `43` status `ready` deltaP `34.2916` edge `0.3544` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4114` n `43` status `ready` deltaP `36.1879` edge `0.0615` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3921` n `137` status `ready` deltaP `16.0242` edge `0.2276` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.3099` n `137` status `ready` deltaP `19.7093` edge `0.2138` maxDD `-6.8828`
- `news_risk_high->fx_4h` score `2.0429` n `43` status `ready` deltaP `26.0599` edge `0.0149` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.9968` n `159` status `ready` deltaP `19.7375` edge `0.1174` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.7134` n `165` status `ready` deltaP `12.603` edge `0.1775` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5157` n `165` status `ready` deltaP `12.603` edge `0.1617` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.1411` n `43` status `ready` deltaP `4.2878` edge `0.1482` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
