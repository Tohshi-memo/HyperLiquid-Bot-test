# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T11:07:35.230034+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8411`

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

- `market_context_high->unknown_24h` score `1470.3682` n `135` status `ready` deltaP `-3.7616` edge `122.6485` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `32.2086` n `148` status `ready` deltaP `4.7833` edge `2.6674` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.7779` n `135` status `ready` deltaP `27.1875` edge `0.0357` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.281` n `148` status `ready` deltaP `8.4803` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0981` n `148` status `ready` deltaP `9.0639` edge `0.0076` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0959` n `148` status `ready` deltaP `8.1728` edge `0.0079` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3797` n `148` status `ready` deltaP `6.9024` edge `0.0336` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4182` n `148` status `ready` deltaP `6.9339` edge `0.0408` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4436` n `135` status `ready` deltaP `12.0833` edge `0.0198` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6485` n `148` status `ready` deltaP `10.4771` edge `0.0011` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.6921` n `148` status `ready` deltaP `-0.8213` edge `0.0062` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7595` n `148` status `ready` deltaP `-3.8234` edge `-0.0036` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.5667` n `148` status `ready` deltaP `-0.3035` edge `-0.0076` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6259` n `148` status `ready` deltaP `2.6096` edge `0.0105` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.1306` n `135` status `ready` deltaP `8.0671` edge `0.0651` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.3065` n `135` status `ready` deltaP `6.0301` edge `0.0454` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0416` n `148` status `ready` deltaP `-9.237` edge `-0.0297` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2704` n `135` status `ready` deltaP `0.544` edge `0.0628` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5092` n `148` status `ready` deltaP `3.5761` edge `-0.0418` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.5636` n `148` status `ready` deltaP `-4.532` edge `-0.1597` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
