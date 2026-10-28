# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T19:23:02.774869+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8636`

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

- `market_context_high->unknown_24h` score `1221.3423` n `148` status `ready` deltaP `-2.135` edge `101.8855` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.7692` n `149` status `ready` deltaP `4.385` edge `1.8001` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.3885` n `148` status `ready` deltaP `23.7144` edge `0.0264` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.147` n `149` status `ready` deltaP `6.9696` edge `0.0016` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1104` n `149` status `ready` deltaP `8.0276` edge `0.007` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.21` n `149` status `ready` deltaP `5.8571` edge `0.0033` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.3951` n `149` status `ready` deltaP `6.2312` edge `0.0361` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.444` n `149` status `ready` deltaP `6.8966` edge `0.0389` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4883` n `148` status `ready` deltaP `13.1006` edge `0.0292` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6165` n `149` status `ready` deltaP `-0.0412` edge `0.0073` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7702` n `149` status `ready` deltaP `-4.0731` edge `-0.0033` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7735` n `149` status `ready` deltaP `8.599` edge `-0.0024` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4662` n `149` status `ready` deltaP `0.4903` edge `0.0` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5907` n `149` status `ready` deltaP `2.5961` edge `0.0151` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-3.0812` n `148` status `ready` deltaP `6.264` edge `-0.0021` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.1356` n `149` status `ready` deltaP `-10.2462` edge `-0.0308` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.298` n `148` status `ready` deltaP `0.3285` edge `0.0607` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.4323` n `148` status `ready` deltaP `-0.0657` edge `0.0164` maxDD `-10.1587`
- `market_context_high->crypto_major_4h` score `-3.437` n `149` status `ready` deltaP `3.5092` edge `-0.0321` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.4619` n `149` status `ready` deltaP `-4.2396` edge `-0.1486` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
