# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T09:22:20.320207+00:00`
- Price records: `672`
- Market context records: `2443`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.2266` n `43` status `ready` deltaP `43.0919` edge `1.3738` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.9967` n `43` status `ready` deltaP `53.4036` edge `1.271` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7943` n `43` status `ready` deltaP `29.7925` edge `1.0657` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.5153` n `43` status `ready` deltaP `16.816` edge `0.7389` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.0367` n `43` status `ready` deltaP `23.4738` edge `0.4525` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.905` n `105` status `ready` deltaP `22.4107` edge `0.3755` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9639` n `43` status `ready` deltaP `8.9309` edge `0.396` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.9624` n `124` status `ready` deltaP `22.9102` edge `0.4418` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.812` n `124` status `ready` deltaP `23.1904` edge `0.5143` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.1976` n `43` status `ready` deltaP `33.4101` edge `0.0622` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1871` n `43` status `ready` deltaP `28.8038` edge `0.2837` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.6512` n `124` status `ready` deltaP `13.3802` edge `0.1927` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.4003` n `105` status `ready` deltaP `10.8581` edge `0.6246` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1098` n `43` status `ready` deltaP `26.8221` edge `0.0154` maxDD `-0.1382`
- `market_context_high->index_24h` score `2.0106` n `105` status `ready` deltaP `9.8611` edge `0.1275` maxDD `-0.3888`
- `news_risk_high->unknown_4h` score `1.7215` n `43` status `ready` deltaP `15.687` edge `0.1112` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0425` n `43` status `ready` deltaP `20.1469` edge `-0.0005` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `0.9873` n `132` status `ready` deltaP `10.3339` edge `0.1328` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.7654` n `132` status `ready` deltaP `7.7436` edge `0.1309` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5903` n `124` status `ready` deltaP `13.0606` edge `0.0447` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
