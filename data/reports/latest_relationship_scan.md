# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T04:22:27.189991+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6632`

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

- `market_context_high->unknown_1h` score `339.9192` n `50` status `ready` deltaP `9.5269` edge `28.268` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0763` n `50` status `ready` deltaP `8.9939` edge `23.9464` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.4781` n `69` status `ready` deltaP `39.2889` edge `1.1322` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.1011` n `50` status `ready` deltaP `36.1667` edge `0.8256` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.0251` n `50` status `ready` deltaP `16.1875` edge `0.7318` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9301` n `50` status `ready` deltaP `17.5427` edge `0.5309` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7837` n `50` status `ready` deltaP `15.5793` edge `0.4241` maxDD `-7.6792`
- `news_risk_high->equity_24h` score `4.264` n `69` status `ready` deltaP `26.5248` edge `0.4774` maxDD `-4.6055`
- `news_risk_high->crypto_alt_4h` score `3.4458` n `87` status `ready` deltaP `13.3954` edge `0.3322` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.2864` n `50` status `ready` deltaP `16.2639` edge `0.4991` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.8997` n `50` status `ready` deltaP `32.689` edge `0.0372` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8692` n `50` status `ready` deltaP `13.8503` edge `0.1918` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8414` n `50` status `ready` deltaP `13.3054` edge `0.2144` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.1377` n `87` status `ready` deltaP `21.2766` edge `0.1059` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.3009` n `69` status `ready` deltaP `21.9278` edge `0.133` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `0.9562` n `69` status `ready` deltaP `7.8729` edge `0.1975` maxDD `-2.192`
- `market_context_high->index_24h` score `0.9292` n `50` status `ready` deltaP `14.7917` edge `0.0776` maxDD `-1.2338`
- `news_risk_high->index_24h` score `0.7901` n `69` status `ready` deltaP `12.9076` edge `0.0276` maxDD `-0.4916`
- `news_risk_high->crypto_major_24h` score `0.6377` n `69` status `ready` deltaP `7.7899` edge `0.3452` maxDD `-15.8971`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
