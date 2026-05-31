# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T04:52:15.130335+00:00`
- Price records: `672`
- Market context records: `2424`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `19.689` n `43` status `ready` deltaP `45.0016` edge `1.3996` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.6307` n `43` status `ready` deltaP `50.973` edge `1.2567` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0271` n `43` status `ready` deltaP `29.7925` edge `1.0851` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3327` n `43` status `ready` deltaP `18.3785` edge `0.7966` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.7203` n `43` status `ready` deltaP `26.078` edge `0.4921` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9632` n `101` status `ready` deltaP `24.7886` edge `0.3645` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.0952` n `43` status `ready` deltaP `9.9726` edge `0.4` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.7025` n `124` status `ready` deltaP `22.8855` edge `0.5072` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.581` n `124` status `ready` deltaP `21.2333` edge `0.4212` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.4884` n `43` status `ready` deltaP `36.5351` edge `0.0656` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2085` n `43` status `ready` deltaP `29.2612` edge `0.2834` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.6962` n `124` status `ready` deltaP `13.8376` edge `0.1934` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.5958` n `101` status `ready` deltaP `14.0711` edge `0.1482` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.595` n `101` status `ready` deltaP `10.9873` edge `0.6487` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.111` n `43` status `ready` deltaP `26.8221` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7665` n `43` status `ready` deltaP `16.1444` edge `0.1119` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2132` n `124` status `ready` deltaP `11.2227` edge `0.1457` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1325` n `43` status `ready` deltaP `20.596` edge `0.004` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0353` n `124` status `ready` deltaP `8.8372` edge `0.1461` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.59` n `101` status `ready` deltaP `1.1379` edge `0.7638` maxDD `-43.6595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
