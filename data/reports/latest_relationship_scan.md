# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T17:07:55.027865+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11668`

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

- `market_context_high->unknown_24h` score `13.2625` n `90` status `ready` deltaP `6.1806` edge `1.0683` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.2833` n `99` status `ready` deltaP `0.5836` edge `0.4526` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.524` n `99` status `ready` deltaP `16.1894` edge `0.1037` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.9606` n `90` status `ready` deltaP `25.0695` edge `0.0766` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9476` n `90` status `ready` deltaP `2.0139` edge `0.2249` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.5268` n `105` status `ready` deltaP `8.3405` edge `0.0299` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0381` n `105` status `ready` deltaP `6.1491` edge `-0.0028` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.041` n `99` status `ready` deltaP `10.9864` edge `0.0075` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.603` n `105` status `ready` deltaP `-2.8585` edge `-0.0088` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7493` n `105` status `ready` deltaP `-3.4445` edge `-0.0197` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7924` n `99` status `ready` deltaP `2.4129` edge `0.0058` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9426` n `105` status `ready` deltaP `-4.2729` edge `-0.0213` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4078` n `90` status `ready` deltaP `0.9027` edge `-0.0422` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.6992` n `99` status `ready` deltaP `-1.8385` edge `-0.0666` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7372` n `105` status `ready` deltaP `2.5278` edge `-0.086` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0301` n `99` status `ready` deltaP `-11.3283` edge `-0.0593` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5334` n `90` status `ready` deltaP `-11.5973` edge `-0.028` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.3274` n `105` status `ready` deltaP `-11.0479` edge `-0.0663` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4169` n `105` status `ready` deltaP `3.1423` edge `-0.261` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0397` n `90` status `ready` deltaP `10.8334` edge `-0.0251` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
