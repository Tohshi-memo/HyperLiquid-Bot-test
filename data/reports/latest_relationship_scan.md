# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T06:07:40.608912+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8793`

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

- `market_context_high->unknown_24h` score `1177.6918` n `135` status `ready` deltaP `-3.7616` edge `98.2588` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `42.966` n `148` status `ready` deltaP `5.2406` edge `3.5608` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9087` n `135` status `ready` deltaP `27.1875` edge `0.0466` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.305` n `148` status `ready` deltaP `8.7797` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0556` n `148` status `ready` deltaP `8.6066` edge `0.0071` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0686` n `148` status `ready` deltaP `8.6219` edge `0.0084` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3369` n `148` status `ready` deltaP `7.2018` edge `0.0371` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4092` n `135` status `ready` deltaP `12.4306` edge `0.0219` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5674` n `148` status `ready` deltaP `5.7144` edge `0.0365` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6715` n `148` status `ready` deltaP `10.0198` edge `0.0012` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7175` n `148` status `ready` deltaP `-3.0749` edge `-0.0032` maxDD `-1.4631`
- `market_context_high->commodity_1h` score `-0.7353` n `148` status `ready` deltaP `-1.1207` edge `0.0046` maxDD `-1.0053`
- `market_context_high->equity_24h` score `-1.2078` n `135` status `ready` deltaP `8.0671` edge `0.142` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5161` n `148` status `ready` deltaP `0.1456` edge `-0.0041` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6002` n `148` status `ready` deltaP `2.7593` edge `0.0128` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.7983` n `135` status `ready` deltaP `9.5023` edge `0.0646` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0108` n `148` status `ready` deltaP `-8.6273` edge `-0.0312` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2049` n `135` status `ready` deltaP `0.544` edge `0.0712` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5493` n `148` status `ready` deltaP `3.1188` edge `-0.0439` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6342` n `148` status `ready` deltaP `-4.0747` edge `-0.1718` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
