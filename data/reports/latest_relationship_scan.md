# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T04:52:25.692415+00:00`
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

- `market_context_high->unknown_24h` score `1098.8026` n `135` status `ready` deltaP `-3.7616` edge `91.6847` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `44.6412` n `148` status `ready` deltaP `5.2406` edge `3.7004` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9303` n `135` status `ready` deltaP `27.1875` edge `0.0484` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2786` n `148` status `ready` deltaP `8.4803` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0714` n `148` status `ready` deltaP `8.7591` edge `0.0074` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0904` n `148` status `ready` deltaP `8.3225` edge `0.0076` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3712` n `148` status `ready` deltaP `7.0521` edge `0.0337` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.3766` n `135` status `ready` deltaP `12.9514` edge `0.0226` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5284` n `148` status `ready` deltaP `6.1717` edge `0.0367` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6645` n `148` status `ready` deltaP `-0.5219` edge `0.0065` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.7038` n `148` status `ready` deltaP `9.5625` edge `0.0001` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7237` n `148` status `ready` deltaP `-3.0749` edge `-0.004` maxDD `-1.4631`
- `market_context_high->equity_24h` score `-1.0446` n `135` status `ready` deltaP `8.0671` edge `0.1556` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5676` n `148` status `ready` deltaP `0.1456` edge `-0.0107` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6618` n `148` status `ready` deltaP `2.4599` edge `0.0069` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.6928` n `135` status `ready` deltaP `10.3704` edge `0.0676` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.018` n `148` status `ready` deltaP `-8.6273` edge `-0.0318` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2314` n `135` status `ready` deltaP `0.544` edge `0.0678` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5515` n `148` status `ready` deltaP `3.2713` edge `-0.0452` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6388` n `148` status `ready` deltaP `-3.9222` edge `-0.1734` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
