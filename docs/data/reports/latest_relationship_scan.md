# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T04:22:23.894493+00:00`
- Price records: `672`
- Market context records: `2528`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

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

- `market_context_high->crypto_alt_4h` score `4.9946` n `162` status `ready` deltaP `23.3119` edge `0.5287` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.8155` n `119` status `ready` deltaP `19.548` edge `0.3038` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.4795` n `162` status `ready` deltaP `16.6892` edge `0.3597` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1818` n `119` status `ready` deltaP `11.6363` edge `0.5914` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.9586` n `162` status `ready` deltaP `11.2485` edge `0.1932` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0403` n `162` status `ready` deltaP `8.7344` edge `0.1472` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6046` n `162` status `ready` deltaP `7.6495` edge `0.1188` maxDD `-4.2199`
- `market_context_high->index_4h` score `-0.0114` n `162` status `ready` deltaP `7.2004` edge `0.0352` maxDD `-2.3986`
- `market_context_high->index_24h` score `-0.0726` n `119` status `ready` deltaP `3.1994` edge `0.0707` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0824` n `119` status `ready` deltaP `0.3574` edge `0.6828` maxDD `-43.6595`
- `market_context_high->equity_24h` score `-0.3397` n `119` status `ready` deltaP `16.9643` edge `0.0113` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3773` n `162` status `ready` deltaP `4.0586` edge `0.0124` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4255` n `162` status `ready` deltaP `1.2512` edge `0.0056` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.492` n `162` status `ready` deltaP `0.5803` edge `0.009` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.5428` n `162` status `ready` deltaP `0.6358` edge `0.004` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5744` n `162` status `ready` deltaP `1.7391` edge `0.0125` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.7766` n `162` status `ready` deltaP `0.3512` edge `0.0168` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.7816` n `162` status `ready` deltaP `1.2496` edge `0.0125` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8992` n `119` status `ready` deltaP `2.3853` edge `0.0039` maxDD `-2.4729`
- `market_context_high->metal_4h` score `-0.9425` n `162` status `ready` deltaP `2.8663` edge `0.0411` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
