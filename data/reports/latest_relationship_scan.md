# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T13:37:30.915491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8465`

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

- `market_context_high->unknown_24h` score `1504.3222` n `135` status `ready` deltaP `-3.7616` edge `125.478` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `24.5487` n `148` status `ready` deltaP `4.4784` edge `2.0311` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.607` n `135` status `ready` deltaP `26.1458` edge `0.0284` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2524` n `149` status `ready` deltaP `8.1672` edge `0.0024` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.013` n `148` status `ready` deltaP `8.1493` edge `0.0066` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0832` n `149` status `ready` deltaP `8.4767` edge `0.0075` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2806` n `149` status `ready` deltaP `7.7282` edge `0.0408` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4085` n `148` status `ready` deltaP `7.0863` edge `0.0406` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5232` n `135` status `ready` deltaP `10.8681` edge `0.0177` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6824` n `148` status `ready` deltaP `10.0198` edge `-0.0002` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.7003` n `149` status `ready` deltaP `-0.9394` edge `0.0063` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7188` n `149` status `ready` deltaP `-3.1749` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.3976` n `149` status `ready` deltaP `1.2388` edge `0.0038` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.544` n `149` status `ready` deltaP `3.0452` edge `0.0181` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.5413` n `135` status `ready` deltaP `4.294` edge `0.0374` maxDD `-8.2244`
- `market_context_high->equity_24h` score `-2.7364` n `135` status `ready` deltaP `7.1991` edge `0.0204` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0308` n `148` status `ready` deltaP `-9.237` edge `-0.0288` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.3165` n `135` status `ready` deltaP `0.544` edge `0.0569` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.423` n `148` status `ready` deltaP `4.0334` edge `-0.0338` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3865` n `148` status `ready` deltaP `-3.4649` edge `-0.1441` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
