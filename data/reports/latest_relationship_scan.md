# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T03:52:38.728548+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6630`

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

- `market_context_high->unknown_1h` score `339.1548` n `50` status `ready` deltaP `9.5269` edge `28.2043` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0463` n `50` status `ready` deltaP `8.9939` edge `23.9439` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.0485` n `71` status `ready` deltaP `39.0234` edge `1.1815` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0915` n `50` status `ready` deltaP `36.1667` edge `0.8248` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.8377` n `50` status `ready` deltaP `15.8403` edge `0.7185` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9529` n `50` status `ready` deltaP `17.5427` edge `0.5328` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7681` n `50` status `ready` deltaP `15.5793` edge `0.4228` maxDD `-7.6792`
- `news_risk_high->equity_24h` score `3.9618` n `71` status `ready` deltaP `24.6674` edge `0.4672` maxDD `-5.2314`
- `news_risk_high->crypto_alt_4h` score `3.5406` n `87` status `ready` deltaP `13.3954` edge `0.3401` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.3247` n `50` status `ready` deltaP `16.6111` edge `0.5017` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `2.9136` n `50` status `ready` deltaP `14.1497` edge `0.1935` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8985` n `50` status `ready` deltaP `32.689` edge `0.0371` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.851` n `50` status `ready` deltaP `13.3054` edge `0.2152` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3003` n `87` status `ready` deltaP `22.2736` edge `0.1128` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.434` n `50` status `ready` deltaP `20.1916` edge `0.0113` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.3789` n `71` status `ready` deltaP `22.9484` edge `0.1362` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.0781` n `71` status `ready` deltaP `9.3628` edge `0.2032` maxDD `-2.192`
- `news_risk_high->crypto_major_24h` score `0.9326` n `71` status `ready` deltaP `9.0963` edge `0.3743` maxDD `-15.8971`
- `market_context_high->index_24h` score `0.9268` n `50` status `ready` deltaP `14.7917` edge `0.0773` maxDD `-1.2338`
- `news_risk_high->index_24h` score `0.9003` n `71` status `ready` deltaP `13.8058` edge `0.0308` maxDD `-0.4916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
