# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T01:37:28.088154+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8775`

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

- `market_context_high->unknown_24h` score `785.8714` n `135` status `ready` deltaP `-3.7616` edge `65.6071` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `47.4454` n `148` status `ready` deltaP `5.0882` edge `3.9351` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9351` n `135` status `ready` deltaP `27.1875` edge `0.0488` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3158` n `148` status `ready` deltaP `8.9294` edge `0.0026` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0882` n `148` status `ready` deltaP `8.7591` edge `0.0088` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1566` n `148` status `ready` deltaP `7.2746` edge `0.0061` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.1851` n `148` status `ready` deltaP `8.1534` edge `0.0521` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.3704` n `135` status `ready` deltaP `12.9514` edge `0.0234` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.439` n `148` status `ready` deltaP `6.7527` edge `0.027` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5591` n `148` status `ready` deltaP `0.3763` edge `0.0093` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7222` n `148` status `ready` deltaP `-2.9252` edge `-0.0048` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8599` n `148` status `ready` deltaP `7.5807` edge `-0.0067` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.1754` n `135` status `ready` deltaP `8.0671` edge `0.1447` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5474` n `148` status `ready` deltaP `0.7444` edge `-0.0121` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.6393` n `135` status `ready` deltaP `10.544` edge `0.0709` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.7724` n `148` status `ready` deltaP `1.7114` edge `-0.0023` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0576` n `148` status `ready` deltaP `-8.6273` edge `-0.0351` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.5536` n `135` status `ready` deltaP `0.544` edge `0.0265` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7605` n `148` status `ready` deltaP `3.4237` edge `-0.073` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.8002` n `148` status `ready` deltaP `-3.9222` edge `-0.1941` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
