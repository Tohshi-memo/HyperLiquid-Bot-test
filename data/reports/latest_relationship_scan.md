# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T05:22:35.172823+00:00`
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

- `market_context_high->unknown_24h` score `11.9495` n `92` status `ready` deltaP `4.4686` edge `0.9703` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.109` n `109` status `ready` deltaP `-1.0405` edge `0.4489` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.328` n `109` status `ready` deltaP `14.8188` edge `0.0965` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8212` n `92` status `ready` deltaP `2.7626` edge `0.2037` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.6336` n `92` status `ready` deltaP `22.2751` edge `0.0533` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.527` n `109` status `ready` deltaP `8.8076` edge `0.0268` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0045` n `109` status `ready` deltaP `5.6831` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1414` n `109` status `ready` deltaP `9.0093` edge `0.0078` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5752` n `109` status `ready` deltaP `-2.3087` edge `-0.0089` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7611` n `109` status `ready` deltaP `-3.656` edge `-0.0198` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9232` n `109` status `ready` deltaP `1.4126` edge `-0.0043` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3107` n `92` status `ready` deltaP `0.4605` edge `-0.0268` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5385` n `109` status `ready` deltaP `-5.4373` edge `-0.0209` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.5876` n `92` status `ready` deltaP `-4.8384` edge `0.0482` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8751` n `109` status `ready` deltaP `0.6703` edge `-0.0913` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.0849` n `109` status `ready` deltaP `1.5369` edge `-0.045` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1738` n `109` status `ready` deltaP `-13.5825` edge `-0.0627` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3293` n `109` status `ready` deltaP `1.7332` edge `-0.2443` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3714` n `109` status `ready` deltaP `-11.8978` edge `-0.0643` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.286` n `92` status `ready` deltaP `8.1069` edge `-0.0278` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
