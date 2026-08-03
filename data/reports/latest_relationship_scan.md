# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T12:22:42.487239+00:00`
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

- `market_context_high->crypto_alt_24h` score `11.8527` n `40` status `ready` deltaP `51.4583` edge `0.6844` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8491` n `40` status `ready` deltaP `51.1458` edge `0.5759` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.5652` n `31` status `ready` deltaP `-6.668` edge `0.2433` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9996` n `31` status `ready` deltaP `20.7359` edge `0.0111` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9305` n `31` status `ready` deltaP `12.192` edge `0.0615` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3977` n `47` status `ready` deltaP `8.3131` edge `0.033` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.376` n `31` status `ready` deltaP `14.1621` edge `-0.013` maxDD `-1.6728`
- `market_context_high->commodity_4h` score `0.3216` n `47` status `ready` deltaP `5.0338` edge `0.0923` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.2621` n `31` status `ready` deltaP `0.2409` edge `0.0583` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1422` n `31` status `ready` deltaP `4.8928` edge `0.0359` maxDD `-0.356`
- `news_risk_high->crypto_alt_1h` score `0.0836` n `31` status `ready` deltaP `11.7394` edge `-0.0035` maxDD `-3.1233`
- `news_risk_high->index_1h` score `0.0488` n `31` status `ready` deltaP `4.0902` edge `-0.0012` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0248` n `47` status `ready` deltaP `6.6664` edge `-0.0087` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.1449` n `47` status `ready` deltaP `11.8935` edge `-0.0057` maxDD `-1.8531`
- `news_risk_high->fx_1h` score `-0.2357` n `31` status `ready` deltaP `-0.2656` edge `0.0027` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.4553` n `47` status `ready` deltaP `1.2292` edge `0.024` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.5996` n `31` status `ready` deltaP `-2.3614` edge `-0.0023` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6815` n `40` status `ready` deltaP `0.6597` edge `0.0368` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.7597` n `31` status `ready` deltaP `3.4093` edge `-0.0481` maxDD `-3.762`
- `news_risk_high->equity_1h` score `-0.9214` n `31` status `ready` deltaP `-9.5615` edge `0.0279` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
