# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T19:57:02.091025+00:00`
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

- `market_context_high->unknown_24h` score `67.1918` n `109` status `ready` deltaP `3.8123` edge `5.5782` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1772` n `119` status `ready` deltaP `13.3237` edge `0.0939` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8357` n `109` status `ready` deltaP `2.9522` edge `0.1668` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5754` n `109` status `ready` deltaP `22.2059` edge `0.0463` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4823` n `119` status `ready` deltaP `7.8892` edge `0.0292` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0003` n `119` status `ready` deltaP `5.8936` edge `-0.0043` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3883` n `119` status `ready` deltaP `5.6115` edge `-0.0012` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5429` n `119` status `ready` deltaP `-2.0783` edge `-0.0063` maxDD `-1.6224`
- `market_context_high->index_1h` score `-1.0504` n `119` status `ready` deltaP `-2.8246` edge `-0.0153` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.2481` n `119` status `ready` deltaP `1.6919` edge `-0.0323` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2583` n `119` status `ready` deltaP `-3.4053` edge `-0.0111` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-1.331` n `119` status `ready` deltaP `1.1175` edge `0.0051` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.397` n `119` status `ready` deltaP `3.1908` edge `-0.0439` maxDD `-10.5179`
- `market_context_high->index_24h` score `-1.4965` n `109` status `ready` deltaP `-5.7417` edge `0.0659` maxDD `-7.8922`
- `market_context_high->index_4h` score `-1.7536` n `119` status `ready` deltaP `-8.8009` edge `-0.0407` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.7057` n `119` status `ready` deltaP `-7.3862` edge `-0.0389` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.7731` n `109` status `ready` deltaP `-4.6026` edge `-0.0561` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-6.0861` n `109` status `ready` deltaP `10.8821` edge `0.0237` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.2684` n `119` status `ready` deltaP `-0.9557` edge `-0.2684` maxDD `-34.9766`
- `market_context_high->crypto_major_4h` score `-7.3286` n `119` status `ready` deltaP `-6.6788` edge `-0.145` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
