# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T00:22:27.534670+00:00`
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

- `market_context_high->unknown_24h` score `262.5058` n `135` status `ready` deltaP `-3.7616` edge `21.9933` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `49.1986` n `148` status `ready` deltaP `5.0882` edge `4.0812` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9411` n `135` status `ready` deltaP `27.1875` edge `0.0493` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3553` n `148` status `ready` deltaP `9.3785` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0894` n `148` status `ready` deltaP `8.7591` edge `0.0089` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0917` n `148` status `ready` deltaP `8.9156` edge `0.0548` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1652` n `148` status `ready` deltaP `7.1249` edge `0.006` maxDD `-1.3073`
- `market_context_high->fx_24h` score `-0.3892` n `135` status `ready` deltaP `12.6042` edge `0.0233` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.446` n `148` status `ready` deltaP `6.603` edge `0.0271` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5267` n `148` status `ready` deltaP `0.6757` edge `0.01` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7027` n `148` status `ready` deltaP `-2.6258` edge `-0.0043` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8615` n `148` status `ready` deltaP `7.5807` edge `-0.0069` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.263` n `135` status `ready` deltaP `8.0671` edge `0.1374` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.499` n `148` status `ready` deltaP `1.1935` edge `-0.0089` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.5267` n `135` status `ready` deltaP `11.412` edge `0.0745` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.7685` n `148` status `ready` deltaP `1.7114` edge `-0.0018` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0552` n `148` status `ready` deltaP `-8.6273` edge `-0.0349` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.6503` n `135` status `ready` deltaP `0.544` edge `0.0141` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8027` n `148` status `ready` deltaP `3.2713` edge `-0.0774` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.761` n `148` status `ready` deltaP `-3.6173` edge `-0.1911` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
