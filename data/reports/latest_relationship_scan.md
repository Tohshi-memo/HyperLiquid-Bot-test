# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T01:22:22.481898+00:00`
- Price records: `672`
- Market context records: `3024`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `21.9236` n `99` status `ready` deltaP `10.1168` edge `2.1512` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `12.6164` n `99` status `ready` deltaP `21.8908` edge `0.9519` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.6125` n `99` status `ready` deltaP `42.3769` edge `0.7926` maxDD `-1.2589`
- `market_context_high->equity_24h` score `7.1774` n `99` status `ready` deltaP `20.7702` edge `1.0569` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.027` n `99` status `ready` deltaP `20.3599` edge `0.5754` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6048` n `115` status `ready` deltaP `18.8825` edge `0.1559` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.5877` n `115` status `ready` deltaP `14.2126` edge `0.1715` maxDD `-12.9393`
- `market_context_high->crypto_alt_4h` score `0.3602` n `115` status `ready` deltaP `23.9966` edge `0.441` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.2567` n `115` status `ready` deltaP `17.3515` edge `0.107` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `0.1467` n `127` status `ready` deltaP `3.4325` edge `0.0316` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.339` n `127` status `ready` deltaP `3.9983` edge `0.0395` maxDD `-5.7692`
- `market_context_high->fx_1h` score `-0.5161` n `127` status `ready` deltaP `-4.4804` edge `0.0003` maxDD `-0.2615`
- `market_context_high->crypto_alt_1h` score `-0.5359` n `127` status `ready` deltaP `6.654` edge `0.0999` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.5417` n `127` status `ready` deltaP `4.6301` edge `0.0254` maxDD `-4.1126`
- `market_context_high->unknown_1h` score `-0.6351` n `127` status `ready` deltaP `4.9743` edge `-0.013` maxDD `-3.1801`
- `market_context_high->unknown_4h` score `-0.7493` n `115` status `ready` deltaP `0.2545` edge `0.0412` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-0.977` n `127` status `ready` deltaP `4.6242` edge `0.0702` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1453` n `127` status `ready` deltaP `-1.7139` edge `-0.0036` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.4706` n `115` status `ready` deltaP `-6.4144` edge `-0.0008` maxDD `-0.6521`
- `market_context_high->fx_24h` score `-1.6715` n `99` status `ready` deltaP `-4.2298` edge `-0.0239` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
