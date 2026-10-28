# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T05:07:29.005482+00:00`
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

- `market_context_high->unknown_24h` score `1118.095` n `135` status `ready` deltaP `-3.7616` edge `93.2924` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `44.238` n `148` status `ready` deltaP `5.2406` edge `3.6668` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9303` n `135` status `ready` deltaP `27.1875` edge `0.0484` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2918` n `148` status `ready` deltaP `8.63` edge `0.0026` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0702` n `148` status `ready` deltaP `8.7591` edge `0.0073` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0787` n `148` status `ready` deltaP `8.4722` edge `0.0081` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3361` n `148` status `ready` deltaP `7.2018` edge `0.0372` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.3782` n `135` status `ready` deltaP `12.9514` edge `0.0224` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5442` n `148` status `ready` deltaP `6.0192` edge `0.0364` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6861` n `148` status `ready` deltaP `-0.6716` edge `0.0057` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.6928` n `148` status `ready` deltaP `9.7149` edge `0.0005` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7121` n `148` status `ready` deltaP `-2.9252` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->equity_24h` score `-1.0506` n `135` status `ready` deltaP `8.0671` edge `0.1551` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.534` n `148` status `ready` deltaP `0.2953` edge `-0.0074` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6189` n `148` status `ready` deltaP `2.6096` edge `0.0114` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.7115` n `135` status `ready` deltaP `10.1968` edge `0.0672` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0144` n `148` status `ready` deltaP `-8.6273` edge `-0.0315` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2104` n `135` status `ready` deltaP `0.544` edge `0.0705` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5375` n `148` status `ready` deltaP `3.2713` edge `-0.0434` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6263` n `148` status `ready` deltaP `-3.9222` edge `-0.1718` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
