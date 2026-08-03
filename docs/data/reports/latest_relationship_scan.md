# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T14:52:25.717379+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5897`

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

- `market_context_high->unknown_24h` score `181.2378` n `40` status `ready` deltaP `30.3819` edge `14.9006` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.1124` n `40` status `ready` deltaP `50.5903` edge `0.6285` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.7723` n `40` status `ready` deltaP `51.1458` edge `0.5695` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.2178` n `31` status `ready` deltaP `-7.1253` edge `0.2174` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9692` n `31` status `ready` deltaP `20.2868` edge `0.0102` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9425` n `31` status `ready` deltaP `12.192` edge `0.0625` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3673` n `47` status `ready` deltaP `7.864` edge `0.0321` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.3422` n `31` status `ready` deltaP `14.0096` edge `-0.0148` maxDD `-1.6728`
- `market_context_high->commodity_4h` score `0.2996` n `47` status `ready` deltaP `4.8813` edge `0.0905` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1631` n `31` status `ready` deltaP `-0.2164` edge `0.0531` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1383` n `31` status `ready` deltaP `4.8928` edge `0.0354` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.0267` n `31` status `ready` deltaP `3.192` edge `-0.0049` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0326` n `47` status `ready` deltaP `6.5167` edge `-0.0087` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.0785` n `31` status `ready` deltaP `10.6915` edge `-0.0173` maxDD `-3.1233`
- `market_context_high->fx_4h` score `-0.1509` n `47` status `ready` deltaP `11.8935` edge `-0.0062` maxDD `-1.8531`
- `news_risk_high->fx_1h` score `-0.2435` n `31` status `ready` deltaP `-0.4153` edge `0.0027` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.572` n `31` status `ready` deltaP `-2.2117` edge `-0.001` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6695` n `40` status `ready` deltaP `0.6597` edge `0.0378` maxDD `-2.506`
- `market_context_high->crypto_alt_4h` score `-0.7185` n `47` status `ready` deltaP `-0.1427` edge `-0.0006` maxDD `-4.9116`
- `news_risk_high->crypto_major_1h` score `-0.9117` n `31` status `ready` deltaP `2.5111` edge `-0.0616` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
