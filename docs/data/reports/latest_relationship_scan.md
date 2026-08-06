# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T22:37:37.527196+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->unknown_24h` score `43.5402` n `109` status `ready` deltaP `3.7571` edge `3.6076` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1653` n `119` status `ready` deltaP `13.1754` edge `0.0939` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.922` n `109` status `ready` deltaP `3.7004` edge `0.169` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5379` n `109` status `ready` deltaP `21.4854` edge `0.0463` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5051` n `120` status `ready` deltaP `8.0988` edge `0.0297` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0085` n `120` status `ready` deltaP `5.7036` edge `-0.0041` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3875` n `119` status `ready` deltaP `5.6124` edge `-0.0011` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5615` n `120` status `ready` deltaP `-2.3752` edge `-0.0067` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8043` n `120` status `ready` deltaP `-3.2934` edge `-0.0101` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0851` n `120` status `ready` deltaP `-3.2734` edge `-0.0152` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.2261` n `119` status `ready` deltaP `1.9797` edge `-0.0314` maxDD `-5.7857`
- `market_context_high->metal_4h` score `-1.3031` n `119` status `ready` deltaP `1.3766` edge `0.0057` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.3748` n `120` status `ready` deltaP `3.498` edge `-0.0431` maxDD `-10.5179`
- `market_context_high->index_24h` score `-1.3784` n `109` status `ready` deltaP `-4.385` edge `0.072` maxDD `-7.8922`
- `market_context_high->index_4h` score `-1.7338` n `119` status `ready` deltaP `-8.5257` edge `-0.04` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.6537` n `120` status `ready` deltaP `-6.9012` edge `-0.0378` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.9549` n `109` status `ready` deltaP `-5.6454` edge `-0.0643` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.2205` n `119` status `ready` deltaP `-0.694` edge `-0.264` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2573` n `109` status `ready` deltaP `9.8099` edge `0.0089` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.296` n `119` status `ready` deltaP `-6.5107` edge `-0.1434` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
