# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T20:59:47.824519+00:00`
- Price records: `672`
- Market context records: `4865`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7626`

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

- `market_context_high->unknown_1h` score `13.4382` n `110` status `ready` deltaP `10.0218` edge `1.0948` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.754` n `110` status `ready` deltaP `23.6197` edge `0.7085` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.3022` n `110` status `ready` deltaP `20.4462` edge `0.5241` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.0178` n `110` status `ready` deltaP `17.73` edge `0.5057` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.173` n `91` status `ready` deltaP `25.2957` edge `0.2967` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.301` n `110` status `ready` deltaP `9.8919` edge `0.1087` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8151` n `110` status `ready` deltaP `11.6768` edge `0.1648` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4728` n `110` status `ready` deltaP `10.3159` edge `0.0381` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4648` n `110` status `ready` deltaP `6.6195` edge `0.1193` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4183` n `110` status `ready` deltaP `8.1709` edge `0.1014` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2137` n `110` status `ready` deltaP `4.2352` edge `0.0589` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1394` n `110` status `ready` deltaP `1.2928` edge `0.0315` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2035` n `110` status `ready` deltaP `3.5819` edge `0.016` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4868` n `110` status `ready` deltaP `0.3103` edge `0.011` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6237` n `110` status `ready` deltaP `1.6768` edge `0.0059` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.793` n `110` status `ready` deltaP `6.8819` edge `0.0067` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3585` n `110` status `ready` deltaP `-7.1666` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8814` n `91` status `ready` deltaP `-6.6831` edge `-0.0112` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.7793` n `91` status `ready` deltaP `-8.1865` edge `-0.1496` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.3252` n `91` status `ready` deltaP `11.0271` edge `-0.0064` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
