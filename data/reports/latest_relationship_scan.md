# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T05:37:31.035261+00:00`
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

- `market_context_high->unknown_24h` score `11.9339` n `92` status `ready` deltaP `4.4686` edge `0.969` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1042` n `109` status `ready` deltaP `-1.0405` edge `0.4485` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.3268` n `109` status `ready` deltaP `14.8188` edge `0.0964` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8267` n `92` status `ready` deltaP `2.7626` edge `0.2044` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.6328` n `92` status `ready` deltaP `22.2751` edge `0.0532` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5294` n `109` status `ready` deltaP `8.8076` edge `0.027` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0057` n `109` status `ready` deltaP `5.6831` edge `-0.0024` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1327` n `109` status `ready` deltaP `9.1618` edge `0.0079` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5759` n `109` status `ready` deltaP `-2.3087` edge `-0.009` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7611` n `109` status `ready` deltaP `-3.656` edge `-0.0198` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.909` n `109` status `ready` deltaP `1.565` edge `-0.0035` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.297` n `92` status `ready` deltaP `0.6341` edge `-0.0262` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5229` n `109` status `ready` deltaP `-5.2876` edge `-0.0206` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.5552` n `92` status `ready` deltaP `-4.6648` edge `0.0512` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8642` n `109` status `ready` deltaP `0.82` edge `-0.0909` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.0789` n `109` status `ready` deltaP `1.5369` edge `-0.0445` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1738` n `109` status `ready` deltaP `-13.5825` edge `-0.0627` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3353` n `109` status `ready` deltaP `1.7332` edge `-0.2448` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3726` n `109` status `ready` deltaP `-11.8978` edge `-0.0644` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3012` n `92` status `ready` deltaP `7.9333` edge `-0.0286` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
