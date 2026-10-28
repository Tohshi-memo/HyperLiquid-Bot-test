# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T06:52:27.778387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8769`

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

- `market_context_high->unknown_24h` score `1217.509` n `135` status `ready` deltaP `-3.7616` edge `101.5769` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `38.9412` n `148` status `ready` deltaP `5.2406` edge `3.2254` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.8835` n `135` status `ready` deltaP `27.1875` edge `0.0445` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3062` n `148` status `ready` deltaP `8.7797` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0702` n `148` status `ready` deltaP `8.7591` edge `0.0073` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0702` n `148` status `ready` deltaP `8.6219` edge `0.0082` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3665` n `148` status `ready` deltaP `7.0521` edge `0.0343` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4296` n `135` status `ready` deltaP `12.0833` edge `0.0216` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.553` n `148` status `ready` deltaP `5.7144` edge `0.0377` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6723` n `148` status `ready` deltaP `10.0198` edge `0.0011` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.7317` n `148` status `ready` deltaP `-1.1207` edge `0.0049` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7432` n `148` status `ready` deltaP `-3.524` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->equity_24h` score `-1.3962` n `135` status `ready` deltaP `8.0671` edge `0.1263` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5457` n `148` status `ready` deltaP `-0.1538` edge `-0.0059` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6282` n `148` status `ready` deltaP `2.6096` edge `0.0102` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.8747` n `135` status `ready` deltaP `8.9815` edge `0.0617` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0534` n `148` status `ready` deltaP `-9.0846` edge `-0.0317` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2166` n `135` status `ready` deltaP `0.544` edge `0.0697` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5713` n `148` status `ready` deltaP `2.9664` edge `-0.0457` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6884` n `148` status `ready` deltaP `-4.532` edge `-0.1757` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
