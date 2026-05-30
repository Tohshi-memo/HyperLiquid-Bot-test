# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T23:07:20.707010+00:00`
- Price records: `672`
- Market context records: `2399`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9201`

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

- `news_risk_high->crypto_alt_24h` score `21.1403` n `43` status `ready` deltaP `48.4738` edge `1.4974` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2402` n `43` status `ready` deltaP `49.9313` edge `1.2311` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3571` n `43` status `ready` deltaP `29.7925` edge `1.1126` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.5586` n `43` status `ready` deltaP `19.7674` edge `0.8895` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3177` n `43` status `ready` deltaP `28.1613` edge `0.528` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4757` n `43` status `ready` deltaP `13.6184` edge `0.4074` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2851` n `116` status `ready` deltaP `22.4677` edge `0.3318` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.8037` n `139` status `ready` deltaP `23.5819` edge `0.4241` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5959` n `43` status `ready` deltaP `37.924` edge `0.0653` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.5197` n `139` status `ready` deltaP `18.0164` edge `0.4411` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.2608` n `43` status `ready` deltaP `30.1758` edge `0.284` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.0287` n `116` status `ready` deltaP `13.7931` edge `0.6856` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.3887` n `139` status `ready` deltaP `13.0232` edge `0.1732` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0879` n `43` status `ready` deltaP `26.5173` edge `0.0156` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6827` n `43` status `ready` deltaP `15.3822` edge `0.11` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2688` n `139` status `ready` deltaP `12.6524` edge `0.1408` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2163` n `116` status `ready` deltaP `8.6865` edge `0.0952` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.0834` n `43` status `ready` deltaP `19.8475` edge `0.0049` maxDD `-1.7548`
- `market_context_high->index_4h` score `0.8079` n `139` status `ready` deltaP `13.7107` edge `0.0585` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `0.7299` n `139` status `ready` deltaP `7.8243` edge `0.1274` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
