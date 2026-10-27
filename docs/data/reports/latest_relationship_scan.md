# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T19:22:30.992024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8740`

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

- `market_context_high->unknown_4h` score `75.6986` n `137` status `ready` deltaP `4.6877` edge `6.2922` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9759` n `135` status `ready` deltaP `27.1875` edge `0.0522` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3924` n `148` status `ready` deltaP `9.8276` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3659` n `137` status `ready` deltaP `12.0204` edge `0.0102` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0842` n `148` status `ready` deltaP `8.4722` edge `0.0074` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3276` n `148` status `ready` deltaP `7.9503` edge `0.0333` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3636` n `137` status `ready` deltaP `6.5971` edge `0.0476` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.483` n `135` status `ready` deltaP `11.0417` edge `0.0217` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.5794` n `148` status `ready` deltaP `0.0769` edge `0.0096` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6498` n `148` status `ready` deltaP `-1.7276` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8728` n `137` status `ready` deltaP `7.4094` edge `-0.0072` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.0809` n `135` status `ready` deltaP `14.8843` edge `0.0885` maxDD `-8.2244`
- `market_context_high->unknown_1h` score `-1.1623` n `148` status `ready` deltaP `0.8497` edge `-0.0536` maxDD `-1.5807`
- `market_context_high->equity_1h` score `-1.4429` n `148` status `ready` deltaP `1.6426` edge `-0.0047` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.6578` n `135` status `ready` deltaP `8.0671` edge `0.1045` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.6703` n `148` status `ready` deltaP `2.4599` edge `0.0058` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9569` n `137` status `ready` deltaP `-7.4884` edge `-0.0343` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7626` n `135` status `ready` deltaP `0.544` edge `-0.0003` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.838` n `137` status `ready` deltaP `3.1323` edge `-0.081` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.5131` n `137` status `ready` deltaP `-0.365` edge `-0.181` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
