# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T05:07:23.970558+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.1346` n `91` status `ready` deltaP `4.4567` edge `0.9858` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1174` n `109` status `ready` deltaP `-1.0405` edge `0.4496` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.311` n `109` status `ready` deltaP `14.6664` edge `0.0961` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7996` n `91` status `ready` deltaP `2.3924` edge `0.2034` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.6699` n `91` status `ready` deltaP `22.8843` edge `0.0539` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5234` n `109` status `ready` deltaP `8.8076` edge `0.0265` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0045` n `109` status `ready` deltaP `5.6831` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1414` n `109` status `ready` deltaP `9.0093` edge `0.0078` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5759` n `109` status `ready` deltaP `-2.3087` edge `-0.009` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7619` n `109` status `ready` deltaP `-3.656` edge `-0.0199` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9358` n `109` status `ready` deltaP `1.2601` edge `-0.0049` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3306` n `91` status `ready` deltaP `0.0783` edge `-0.0268` maxDD `-4.5445`
- `market_context_high->index_24h` score `-1.5279` n `91` status `ready` deltaP `-4.3193` edge `0.0524` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.5409` n `109` status `ready` deltaP `-5.4373` edge `-0.0211` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8822` n `109` status `ready` deltaP `0.6703` edge `-0.0922` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.0909` n `109` status `ready` deltaP `1.5369` edge `-0.0455` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1738` n `109` status `ready` deltaP `-13.5825` edge `-0.0627` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3185` n `109` status `ready` deltaP `1.7332` edge `-0.2434` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3702` n `109` status `ready` deltaP `-11.8978` edge `-0.0642` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.231` n `91` status `ready` deltaP `8.5966` edge `-0.0296` maxDD `-51.125`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
