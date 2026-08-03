# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T04:37:27.686394+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `2849.0431` n `44` status `ready` deltaP `21.291` edge `237.3204` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.6491` n `40` status `ready` deltaP `51.4583` edge `0.8341` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0922` n `40` status `ready` deltaP `51.3194` edge `0.595` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `2.3105` n `44` status `ready` deltaP `1.8016` edge `0.2569` maxDD `-3.4427`
- `news_risk_high->index_4h` score `0.946` n `44` status `ready` deltaP `8.9246` edge `0.0574` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.365` n `47` status `ready` deltaP `7.5646` edge `0.0338` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3317` n `47` status `ready` deltaP `5.0338` edge `0.0936` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.1077` n `44` status `ready` deltaP `11.3364` edge `-0.0139` maxDD `-1.496`
- `news_risk_high->metal_4h` score `0.101` n `44` status `ready` deltaP `5.9036` edge `0.0087` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.0919` n `44` status `ready` deltaP `5.1715` edge `0.0093` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.0596` n `47` status `ready` deltaP `14.1801` edge `-0.0039` maxDD `-1.8531`
- `market_context_high->fx_1h` score `-0.0007` n `47` status `ready` deltaP `7.1155` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->index_1h` score `-0.1051` n `44` status `ready` deltaP `2.3` edge `0.0035` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.2014` n `44` status `ready` deltaP `1.7964` edge `0.0035` maxDD `-0.2475`
- `news_risk_high->crypto_alt_1h` score `-0.2053` n `44` status `ready` deltaP `5.7431` edge `0.0036` maxDD `-3.1233`
- `market_context_high->crypto_alt_4h` score `-0.2063` n `47` status `ready` deltaP `2.2963` edge `0.0488` maxDD `-4.9116`
- `news_risk_high->equity_1h` score `-0.3255` n `44` status `ready` deltaP `0.5036` edge `0.0518` maxDD `-2.916`
- `news_risk_high->fx_4h` score `-0.4589` n `44` status `ready` deltaP `1.6075` edge `0.0262` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.6228` n `44` status `ready` deltaP `1.7964` edge `-0.0198` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6935` n `40` status `ready` deltaP `0.6597` edge `0.0358` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
