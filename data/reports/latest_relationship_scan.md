# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T02:52:26.977967+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_4h` score `321.7678` n `50` status `ready` deltaP `12.9573` edge `26.7276` maxDD `0.0`
- `market_context_high->unknown_1h` score `314.2547` n `57` status `ready` deltaP `10.156` edge `26.1251` maxDD `-0.0597`
- `market_context_high->crypto_alt_24h` score `13.0258` n `50` status `ready` deltaP `28.5927` edge `1.0652` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `12.0844` n `59` status `ready` deltaP `31.8685` edge `0.8046` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `10.9368` n `65` status `ready` deltaP `40.1736` edge `0.6639` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.8877` n `50` status `ready` deltaP `34.3397` edge `0.82` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.3257` n `65` status `ready` deltaP `24.2073` edge `0.5835` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0216` n `50` status `ready` deltaP `15.8659` edge `0.5497` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4348` n `50` status `ready` deltaP `14.2073` edge `0.4871` maxDD `-7.6465`
- `news_risk_high->index_24h` score `5.0935` n `59` status `ready` deltaP `35.5286` edge `0.1876` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.872` n `65` status `ready` deltaP `26.6745` edge `0.2061` maxDD `-2.9013`
- `news_risk_high->crypto_major_1h` score `3.0454` n `65` status `ready` deltaP `13.9083` edge `0.1966` maxDD `-1.5096`
- `news_risk_high->index_4h` score `3.0392` n `65` status `ready` deltaP `32.9808` edge `0.0596` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.009` n `50` status `ready` deltaP `33.7561` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->metal_4h` score `2.5902` n `65` status `ready` deltaP `22.2796` edge `0.1089` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.4326` n `57` status `ready` deltaP `10.9124` edge `0.175` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.1111` n `57` status `ready` deltaP `8.2598` edge `0.1955` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.0842` n `65` status `ready` deltaP `25.6172` edge `0.0179` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5726` n `65` status `ready` deltaP `5.3178` edge `0.1475` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.2802` n `50` status `ready` deltaP `6.6482` edge `0.306` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
