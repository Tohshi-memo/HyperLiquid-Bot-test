# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T18:22:18.637920+00:00`
- Price records: `672`
- Market context records: `2376`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.9128` n `43` status `ready` deltaP `50.2099` edge `1.5502` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.9256` n `43` status `ready` deltaP `48.3688` edge `1.2153` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2179` n `43` status `ready` deltaP `29.7925` edge `1.101` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8862` n `43` status `ready` deltaP `19.7674` edge `0.9168` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2193` n `43` status `ready` deltaP `28.1613` edge `0.5198` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `7.313` n `134` status `ready` deltaP `18.6567` edge `0.8743` maxDD `-25.1408`
- `market_context_high->crypto_major_4h` score `5.6319` n `147` status `ready` deltaP `24.0336` edge `0.4901` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `5.4923` n `134` status `ready` deltaP `23.8573` edge `0.3398` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3238` n `43` status `ready` deltaP `13.4448` edge `0.3959` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6128` n `147` status `ready` deltaP `19.0943` edge `0.525` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.5702` n `147` status `ready` deltaP `19.6221` edge `0.311` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7373` n `43` status `ready` deltaP `32.0051` edge `0.3329` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4639` n `43` status `ready` deltaP `36.7087` edge `0.0624` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9857` n `43` status `ready` deltaP `25.4502` edge `0.0142` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.644` n `155` status `ready` deltaP `14.1028` edge `0.1624` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.5679` n `134` status `ready` deltaP `11.9869` edge `0.1025` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.5636` n `147` status `ready` deltaP `17.3376` edge `0.0973` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.251` n `155` status `ready` deltaP `9.943` edge `0.1567` maxDD `-6.1656`
- `news_risk_high->unknown_4h` score `1.1166` n `43` status `ready` deltaP `13.7053` edge `0.074` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `0.985` n `43` status `ready` deltaP `19.5481` edge `-0.0013` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
