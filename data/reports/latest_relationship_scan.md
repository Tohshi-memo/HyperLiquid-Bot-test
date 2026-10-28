# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T07:22:34.353891+00:00`
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

- `market_context_high->unknown_24h` score `1245.8122` n `135` status `ready` deltaP `-3.7616` edge `103.9355` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `39.318` n `148` status `ready` deltaP `5.2406` edge `3.2568` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.8679` n `135` status `ready` deltaP `27.1875` edge `0.0432` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3182` n `148` status `ready` deltaP `8.9294` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0957` n `148` status `ready` deltaP `9.0639` edge `0.0074` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0795` n `148` status `ready` deltaP `8.4722` edge `0.008` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3369` n `148` status `ready` deltaP `7.3515` edge `0.0361` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4311` n `135` status `ready` deltaP `12.0833` edge `0.0214` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5482` n `148` status `ready` deltaP `5.7144` edge `0.0381` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6715` n `148` status `ready` deltaP `10.0198` edge `0.0012` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.7317` n `148` status `ready` deltaP `-1.1207` edge `0.0049` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.751` n `148` status `ready` deltaP `-3.6737` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->equity_24h` score `-1.497` n `135` status `ready` deltaP `8.0671` edge `0.1179` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5426` n `148` status `ready` deltaP `-0.1538` edge `-0.0055` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5893` n `148` status `ready` deltaP `2.909` edge `0.0132` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.9265` n `135` status `ready` deltaP `8.6343` edge `0.0597` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.079` n `148` status `ready` deltaP `-9.3895` edge `-0.0318` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2002` n `135` status `ready` deltaP `0.544` edge `0.0718` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5406` n `148` status `ready` deltaP `3.2713` edge `-0.0438` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7042` n `148` status `ready` deltaP `-4.6844` edge `-0.1767` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
