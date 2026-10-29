# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T06:37:28.661185+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8156`

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

- `market_context_high->unknown_24h` score `1266.1083` n `148` status `ready` deltaP `-2.135` edge `105.616` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `19.5334` n `149` status `ready` deltaP `4.2325` edge `1.6148` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.6113` n `148` status `ready` deltaP `18.6796` edge `-0.0048` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2105` n `149` status `ready` deltaP `7.7181` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0481` n `149` status `ready` deltaP `7.6864` edge `0.0046` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0829` n `149` status `ready` deltaP `10.5551` edge `0.0446` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1322` n `149` status `ready` deltaP `7.7282` edge `0.0062` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4107` n `149` status `ready` deltaP `5.7821` edge `0.0371` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4536` n `149` status `ready` deltaP `1.6055` edge `0.0099` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8375` n `149` status `ready` deltaP `7.5319` edge `-0.0035` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8512` n `149` status `ready` deltaP `-5.4204` edge `-0.0047` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.1971` n `148` status `ready` deltaP `6.8506` edge `0.0118` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5379` n `149` status `ready` deltaP `-0.4079` edge `-0.0032` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6406` n `149` status `ready` deltaP `1.8476` edge `0.0137` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1524` n `149` status `ready` deltaP `-10.2462` edge `-0.0322` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.2818` n `149` status `ready` deltaP `3.5092` edge `-0.0122` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.8493` n `148` status `ready` deltaP `-0.2393` edge `-0.0172` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.0766` n `148` status `ready` deltaP `-3.6646` edge `-0.0125` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.5146` n `149` status `ready` deltaP `-4.8494` edge `-0.1513` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9567` n `148` status `ready` deltaP `2.271` edge `-0.2151` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
