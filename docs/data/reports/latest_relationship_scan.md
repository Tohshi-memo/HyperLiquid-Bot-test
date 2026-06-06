# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T03:22:20.628542+00:00`
- Price records: `672`
- Market context records: `3033`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `22.9927` n `99` status `ready` deltaP `10.9848` edge `2.2345` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `12.9799` n `99` status `ready` deltaP `22.7589` edge `0.9764` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.7901` n `99` status `ready` deltaP `42.3769` edge `0.8074` maxDD `-1.2589`
- `market_context_high->equity_24h` score `8.0717` n `99` status `ready` deltaP `22.1591` edge `1.1623` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.827` n `99` status `ready` deltaP `21.7488` edge `0.6328` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.8386` n `123` status `ready` deltaP `19.3598` edge `0.1722` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0421` n `129` status `ready` deltaP `2.4405` edge `0.0295` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.2217` n `123` status `ready` deltaP `2.4391` edge `0.0706` maxDD `-3.7602`
- `market_context_high->index_4h` score `-0.2894` n `123` status `ready` deltaP `14.1768` edge `0.0814` maxDD `-12.7083`
- `market_context_high->index_1h` score `-0.3897` n `129` status `ready` deltaP `4.0872` edge `0.0242` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.4645` n `129` status `ready` deltaP `3.7182` edge `0.0372` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.5252` n `129` status `ready` deltaP `-4.5897` edge `0.0001` maxDD `-0.2801`
- `market_context_high->crypto_alt_4h` score `-0.557` n `123` status `ready` deltaP `20.0203` edge `0.3641` maxDD `-39.8512`
- `market_context_high->crypto_alt_1h` score `-0.5646` n `129` status `ready` deltaP `6.3861` edge `0.098` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.8441` n `129` status `ready` deltaP `3.7715` edge `-0.0224` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9996` n `129` status `ready` deltaP `4.2798` edge `0.0696` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0835` n `123` status `ready` deltaP `-8.2317` edge `-0.0027` maxDD `-0.8397`
- `market_context_high->metal_1h` score `-1.1365` n `129` status `ready` deltaP `-1.7987` edge `-0.0019` maxDD `-6.8783`
- `market_context_high->equity_4h` score `-1.4224` n `123` status `ready` deltaP `11.0772` edge `0.0941` maxDD `-25.0248`
- `market_context_high->fx_24h` score `-1.5183` n `99` status `ready` deltaP `-2.8409` edge `-0.0204` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
