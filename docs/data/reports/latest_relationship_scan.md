# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T04:22:30.686076+00:00`
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

- `market_context_high->unknown_24h` score `1060.0378` n `135` status `ready` deltaP `-3.7616` edge `88.4543` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `44.5522` n `148` status `ready` deltaP `5.0882` edge `3.694` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9315` n `135` status `ready` deltaP `27.1875` edge `0.0485` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2774` n `148` status `ready` deltaP `8.4803` edge `0.0024` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0738` n `148` status `ready` deltaP `8.7591` edge `0.0076` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1114` n `148` status `ready` deltaP `8.0231` edge `0.0069` maxDD `-1.3073`
- `market_context_high->fx_24h` score `-0.3743` n `135` status `ready` deltaP `12.9514` edge `0.0229` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4359` n `148` status `ready` deltaP `6.7527` edge `0.0274` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.486` n `148` status `ready` deltaP `6.4766` edge `0.0382` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6262` n `148` status `ready` deltaP `-0.2225` edge `0.0077` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.7267` n `148` status `ready` deltaP `9.2576` edge `-0.0008` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7456` n `148` status `ready` deltaP `-3.3743` edge `-0.0048` maxDD `-1.4631`
- `market_context_high->equity_24h` score `-1.0338` n `135` status `ready` deltaP `8.0671` edge `0.1565` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.6198` n `148` status `ready` deltaP `-0.1538` edge `-0.0154` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.6892` n `135` status `ready` deltaP `10.3704` edge `0.0679` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.735` n `148` status `ready` deltaP `2.1605` edge `-0.0005` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0252` n `148` status `ready` deltaP `-8.6273` edge `-0.0324` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2743` n `135` status `ready` deltaP `0.544` edge `0.0623` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5835` n `148` status `ready` deltaP `3.2713` edge `-0.0493` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6622` n `148` status `ready` deltaP `-3.9222` edge `-0.1764` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
