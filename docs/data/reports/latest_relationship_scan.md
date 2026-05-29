# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T17:52:22.953387+00:00`
- Price records: `672`
- Market context records: `2266`
- Flow alert records: `8419`
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

- `news_risk_high->crypto_alt_24h` score `21.5537` n `43` status `ready` deltaP `51.946` edge `1.5087` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7499` n `43` status `ready` deltaP `42.2925` edge `1.0745` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.4766` n `43` status `ready` deltaP `32.5702` edge `1.0207` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.3728` n `43` status `ready` deltaP `22.5452` edge `0.8555` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `8.852` n `115` status `ready` deltaP `28.8043` edge `0.5868` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `8.8001` n `149` status `ready` deltaP `27.6365` edge `0.817` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `8.4218` n `149` status `ready` deltaP `32.7027` edge `0.6648` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `8.4155` n `43` status `ready` deltaP `32.8488` edge `0.5049` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `5.6707` n `115` status `ready` deltaP `16.2561` edge `1.0079` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3829` n `149` status `ready` deltaP `22.0259` edge `0.3627` maxDD `-1.8773`
- `news_risk_high->index_24h` score `3.762` n `43` status `ready` deltaP `12.4031` edge `0.2727` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7437` n `43` status `ready` deltaP `32.1575` edge `0.3327` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6291` n `43` status `ready` deltaP `37.2295` edge `0.0727` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3724` n `115` status `ready` deltaP `14.2029` edge `0.2381` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.214` n `43` status `ready` deltaP `2.8989` edge `0.3302` maxDD `-3.202`
- `market_context_high->index_4h` score `2.7119` n `149` status `ready` deltaP `24.867` edge `0.1416` maxDD `-2.1777`
- `market_context_high->equity_4h` score `2.4542` n `149` status `ready` deltaP `19.0743` edge `0.2178` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.2573` n `159` status `ready` deltaP `13.6717` edge `0.2157` maxDD `-6.1656`
- `market_context_high->equity_24h` score `2.1154` n `115` status `ready` deltaP `20.1132` edge `0.1949` maxDD `-6.8828`
- `news_risk_high->fx_4h` score `2.0589` n `43` status `ready` deltaP `26.3648` edge `0.0142` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
