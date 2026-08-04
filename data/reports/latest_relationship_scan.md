# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T20:06:19.339287+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `22.236` n `69` status `ready` deltaP `19.9049` edge `1.7246` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3615` n `90` status `ready` deltaP `1.5955` edge `0.5357` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.3889` n `90` status `ready` deltaP `16.1654` edge `0.0926` maxDD `-2.7703`
- `market_context_high->crypto_alt_24h` score `0.4545` n `69` status `ready` deltaP `9.6014` edge `0.1303` maxDD `-3.8833`
- `market_context_high->fx_24h` score `0.2839` n `69` status `ready` deltaP `14.4852` edge `0.0604` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.2086` n `69` status `ready` deltaP `-6.2122` edge `0.185` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.1719` n `90` status `ready` deltaP `4.8935` edge `0.0233` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1392` n `90` status `ready` deltaP `14.3767` edge `0.008` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1231` n `90` status `ready` deltaP `7.3054` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->metal_1h` score `-0.541` n `90` status `ready` deltaP `-1.6068` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.583` n `90` status `ready` deltaP `-0.306` edge `-0.0193` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7265` n `90` status `ready` deltaP `-2.3087` edge `-0.0067` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7764` n `90` status `ready` deltaP `2.2696` edge `0.0088` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8453` n `90` status `ready` deltaP `4.2479` edge `0.0023` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6939` n `90` status `ready` deltaP `4.6507` edge `-0.0946` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0098` n `90` status `ready` deltaP `-11.6734` edge `-0.0544` maxDD `-4.7021`
- `market_context_high->commodity_24h` score `-2.3993` n `69` status `ready` deltaP `13.0661` edge `0.0231` maxDD `-25.7577`
- `market_context_high->index_24h` score `-2.5098` n `69` status `ready` deltaP `-11.3074` edge `-0.0269` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.3857` n `90` status `ready` deltaP `2.4983` edge `-0.2541` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.42` n `90` status `ready` deltaP `-11.7099` edge `-0.0696` maxDD `-7.6533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
