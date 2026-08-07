# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T03:07:26.250433+00:00`
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

- `market_context_high->unknown_24h` score `2.901` n `109` status `ready` deltaP `3.7571` edge `0.221` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.2497` n `120` status `ready` deltaP `14.0955` edge `0.0948` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8788` n `109` status `ready` deltaP `3.7004` edge `0.1654` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.573` n `109` status `ready` deltaP `21.4854` edge `0.0508` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5063` n `120` status `ready` deltaP `8.0988` edge `0.0298` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0234` n `120` status `ready` deltaP `6.3024` edge `-0.004` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3142` n `120` status `ready` deltaP `6.6768` edge `0.0012` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5467` n `120` status `ready` deltaP `-2.0758` edge `-0.0068` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8097` n `120` status `ready` deltaP `-3.4431` edge `-0.0098` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9808` n `120` status `ready` deltaP `-2.2255` edge `-0.0135` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.134` n `109` status `ready` deltaP `-1.38` edge `0.0833` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2906` n `120` status `ready` deltaP `4.0968` edge `-0.0363` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.3764` n `120` status `ready` deltaP `0.6402` edge `0.0045` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.5753` n `120` status `ready` deltaP `-6.4533` edge `-0.0335` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.878` n `120` status `ready` deltaP `2.1138` edge `-0.0316` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6165` n `120` status `ready` deltaP `-6.6018` edge `-0.0367` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.435` n `109` status `ready` deltaP `-8.3166` edge `-0.0865` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8681` n `120` status `ready` deltaP `0.8028` edge `-0.2288` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3438` n `109` status `ready` deltaP `9.8099` edge `-0.0022` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.1917` n `120` status `ready` deltaP `-5.7317` edge `-0.1399` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
