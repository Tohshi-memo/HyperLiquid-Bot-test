# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T12:52:22.248562+00:00`
- Price records: `672`
- Market context records: `2351`
- Flow alert records: `8640`
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

- `news_risk_high->crypto_alt_24h` score `21.3601` n `43` status `ready` deltaP `50.0363` edge `1.5053` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.0917` n `43` status `ready` deltaP `45.0702` edge `1.1678` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.6719` n `43` status `ready` deltaP `29.7925` edge `1.0555` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.1182` n `43` status `ready` deltaP `19.7674` edge `0.8528` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.9153` n `140` status `ready` deltaP `20.0` edge `1.0822` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.6821` n `43` status `ready` deltaP `27.6405` edge `0.4785` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.8525` n `140` status `ready` deltaP `24.4346` edge `0.4493` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `6.514` n `156` status `ready` deltaP `25.2502` edge `0.5555` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `6.4928` n `156` status `ready` deltaP `22.4047` edge `0.6596` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.7431` n `156` status `ready` deltaP `23.2293` edge `0.3847` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.8705` n `43` status `ready` deltaP `12.924` edge `0.3616` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.9915` n `43` status `ready` deltaP `33.8343` edge `0.3533` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4066` n `43` status `ready` deltaP `36.1879` edge `0.0611` maxDD `-0.1442`
- `market_context_high->index_24h` score `2.6537` n `140` status `ready` deltaP `13.1399` edge `0.1853` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.0996` n `140` status `ready` deltaP `19.9752` edge `0.1945` maxDD `-6.8828`
- `market_context_high->index_4h` score `2.0122` n `156` status `ready` deltaP `19.8249` edge `0.1181` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.0003` n `43` status `ready` deltaP `25.6026` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.6022` n `163` status `ready` deltaP `11.5435` edge `0.1753` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5973` n `163` status `ready` deltaP `13.249` edge `0.1642` maxDD `-4.2199`
- `market_context_high->metal_4h` score `1.1438` n `156` status `ready` deltaP `16.0296` edge `0.1272` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
