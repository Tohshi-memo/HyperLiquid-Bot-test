# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T12:52:30.653792+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8465`

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

- `market_context_high->unknown_24h` score `1497.661` n `135` status `ready` deltaP `-3.7616` edge `124.9229` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `24.645` n `148` status `ready` deltaP `4.7833` edge `2.0371` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.6798` n `135` status `ready` deltaP `26.6666` edge `0.031` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2644` n `149` status `ready` deltaP `8.3169` edge `0.0024` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0154` n `148` status `ready` deltaP `8.1493` edge `0.0068` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0824` n `149` status `ready` deltaP `8.4767` edge `0.0076` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3001` n `149` status `ready` deltaP `7.5785` edge `0.0393` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4049` n `148` status `ready` deltaP `7.0863` edge `0.0409` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4907` n `135` status `ready` deltaP `11.3889` edge `0.0184` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6706` n `148` status `ready` deltaP `10.1722` edge `0.0003` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.6728` n `149` status `ready` deltaP `-0.64` edge `0.0066` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7188` n `149` status `ready` deltaP `-3.1749` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.4257` n `149` status `ready` deltaP `0.9394` edge `0.0022` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5486` n `149` status `ready` deltaP `3.0452` edge `0.0175` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.4733` n `135` status `ready` deltaP `4.8148` edge `0.0396` maxDD `-8.2244`
- `market_context_high->equity_24h` score `-2.5196` n `135` status `ready` deltaP `7.7199` edge `0.035` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0308` n `148` status `ready` deltaP `-9.237` edge `-0.0288` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.3196` n `135` status `ready` deltaP `0.544` edge `0.0565` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4739` n `148` status `ready` deltaP `3.7286` edge `-0.0383` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.4352` n `148` status `ready` deltaP `-3.9222` edge `-0.1473` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
