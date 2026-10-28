# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T01:22:33.750744+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8775`

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

- `market_context_high->unknown_24h` score `682.6714` n `135` status `ready` deltaP `-3.7616` edge `57.0071` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `47.4826` n `148` status `ready` deltaP `5.0882` edge `3.9382` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9375` n `135` status `ready` deltaP `27.1875` edge `0.049` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3289` n `148` status `ready` deltaP `9.0791` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0894` n `148` status `ready` deltaP `8.7591` edge `0.0089` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1566` n `148` status `ready` deltaP `7.2746` edge `0.0061` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.1633` n `148` status `ready` deltaP `8.3058` edge `0.0529` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.3704` n `135` status `ready` deltaP `12.9514` edge `0.0234` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4351` n `148` status `ready` deltaP `6.7527` edge `0.0275` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5579` n `148` status `ready` deltaP `0.3763` edge `0.0094` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7129` n `148` status `ready` deltaP `-2.7755` edge `-0.0046` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8694` n `148` status `ready` deltaP `7.4283` edge `-0.0069` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.1874` n `135` status `ready` deltaP `8.0671` edge `0.1437` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5294` n `148` status `ready` deltaP `0.8941` edge `-0.0108` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.6183` n `135` status `ready` deltaP `10.7176` edge `0.0715` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.7693` n `148` status `ready` deltaP `1.7114` edge `-0.0019` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0588` n `148` status `ready` deltaP `-8.6273` edge `-0.0352` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.5668` n `135` status `ready` deltaP `0.544` edge `0.0248` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7926` n `148` status `ready` deltaP `3.2713` edge `-0.0761` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.8049` n `148` status `ready` deltaP `-3.9222` edge `-0.1947` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
