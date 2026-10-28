# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T07:33:23.962628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8751`

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

- `market_context_high->unknown_24h` score `1260.7678` n `135` status `ready` deltaP `-3.7616` edge `105.1818` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `40.1136` n `148` status `ready` deltaP `5.2406` edge `3.3231` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.8595` n `135` status `ready` deltaP `27.1875` edge `0.0425` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3182` n `148` status `ready` deltaP `8.9294` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1091` n `148` status `ready` deltaP `9.2164` edge `0.0075` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0881` n `148` status `ready` deltaP `8.3225` edge `0.0079` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3236` n `148` status `ready` deltaP `7.5012` edge `0.0368` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4319` n `135` status `ready` deltaP `12.0833` edge `0.0213` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5458` n `148` status `ready` deltaP `5.7144` edge `0.0383` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6715` n `148` status `ready` deltaP `10.0198` edge `0.0012` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.7161` n `148` status `ready` deltaP `-0.971` edge `0.0052` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7595` n `148` status `ready` deltaP `-3.8234` edge `-0.0036` maxDD `-1.4631`
- `market_context_high->equity_24h` score `-1.5534` n `135` status `ready` deltaP `8.0671` edge `0.1132` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5535` n `148` status `ready` deltaP `-0.3035` edge `-0.0059` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5745` n `148` status `ready` deltaP `3.0587` edge `0.0141` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.9536` n `135` status `ready` deltaP `8.4606` edge `0.0586` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0924` n `148` status `ready` deltaP `-9.5419` edge `-0.0319` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.1963` n `135` status `ready` deltaP `0.544` edge `0.0723` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5249` n `148` status `ready` deltaP `3.4237` edge `-0.0428` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7183` n `148` status `ready` deltaP `-4.8368` edge `-0.1775` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
