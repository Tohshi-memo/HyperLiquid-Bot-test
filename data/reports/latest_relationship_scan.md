# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T05:37:27.619356+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8825`

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

- `market_context_high->unknown_24h` score `1147.9606` n `135` status `ready` deltaP `-3.7616` edge `95.7812` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `42.7872` n `148` status `ready` deltaP `5.2406` edge `3.5459` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9243` n `135` status `ready` deltaP `27.1875` edge `0.0479` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3038` n `148` status `ready` deltaP `8.7797` edge `0.0026` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0568` n `148` status `ready` deltaP `8.6066` edge `0.0072` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0585` n `148` status `ready` deltaP `8.7716` edge `0.0087` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3018` n `148` status `ready` deltaP `7.3515` edge `0.0406` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.3896` n `135` status `ready` deltaP `12.7778` edge `0.0221` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5746` n `148` status `ready` deltaP `5.7144` edge `0.0359` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6707` n `148` status `ready` deltaP `10.0198` edge `0.0013` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7074` n `148` status `ready` deltaP `-2.9252` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->commodity_1h` score `-0.7245` n `148` status `ready` deltaP `-0.971` edge `0.0045` maxDD `-1.0053`
- `market_context_high->equity_24h` score `-1.1034` n `135` status `ready` deltaP `8.0671` edge `0.1507` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5005` n `148` status `ready` deltaP `0.2953` edge `-0.0031` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.576` n `148` status `ready` deltaP `2.7593` edge `0.0159` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.7513` n `135` status `ready` deltaP `9.8495` edge `0.0662` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0084` n `148` status `ready` deltaP `-8.6273` edge `-0.031` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.1948` n `135` status `ready` deltaP `0.544` edge `0.0725` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5242` n `148` status `ready` deltaP `3.2713` edge `-0.0417` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6115` n `148` status `ready` deltaP `-3.9222` edge `-0.1699` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
