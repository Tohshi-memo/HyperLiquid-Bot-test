# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T06:52:17.956340+00:00`
- Price records: `672`
- Market context records: `2433`
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

- `news_risk_high->crypto_alt_24h` score `19.3019` n `43` status `ready` deltaP `43.6127` edge `1.3766` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.7841` n `43` status `ready` deltaP `51.8411` edge `1.2637` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9323` n `43` status `ready` deltaP `29.7925` edge `1.0772` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.7956` n `43` status `ready` deltaP `16.9896` edge `0.7611` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.4316` n `43` status `ready` deltaP `24.6891` edge `0.4773` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6745` n `101` status `ready` deltaP `23.3997` edge `0.3497` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.985` n `43` status `ready` deltaP `9.1045` edge `0.3966` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.6076` n `124` status `ready` deltaP `21.3858` edge `0.4224` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.5741` n `124` status `ready` deltaP `21.9708` edge `0.5026` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.3617` n `43` status `ready` deltaP `35.1462` edge `0.0643` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1738` n `43` status `ready` deltaP `28.8038` edge `0.282` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7382` n `124` status `ready` deltaP `13.8376` edge `0.1969` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4855` n `101` status `ready` deltaP `13.203` edge `0.1448` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.2458` n `101` status `ready` deltaP `9.5984` edge `0.6132` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1232` n `43` status `ready` deltaP `26.9746` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8085` n `43` status `ready` deltaP `16.1444` edge `0.1154` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2192` n `124` status `ready` deltaP `11.2227` edge `0.1462` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1109` n `43` status `ready` deltaP `20.596` edge `0.0022` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0138` n `124` status `ready` deltaP `8.6875` edge `0.1453` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.532` n `43` status `ready` deltaP `9.1178` edge `0.0754` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
