# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T00:37:28.524828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8273`

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

- `market_context_high->unknown_24h` score `1254.7143` n `148` status `ready` deltaP `-2.135` edge `104.6665` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1136` n `149` status `ready` deltaP `4.385` edge `1.8288` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.8604` n `148` status `ready` deltaP `20.0685` edge `0.0067` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3099` n `149` status `ready` deltaP `8.9157` edge `0.0022` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0311` n `149` status `ready` deltaP `8.601` edge `0.0051` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1065` n `149` status `ready` deltaP `8.1773` edge `0.0065` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3414` n `149` status `ready` deltaP `6.6803` edge `0.04` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4179` n `149` status `ready` deltaP `7.6588` edge `0.036` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6261` n `149` status `ready` deltaP `-0.1909` edge `0.0075` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7601` n `149` status `ready` deltaP `-3.9234` edge `-0.003` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8335` n `149` status `ready` deltaP `7.6844` edge `-0.004` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.8921` n `148` status `ready` deltaP `9.6284` edge `0.0187` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.428` n `149` status `ready` deltaP `0.7897` edge `0.0029` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.565` n `149` status `ready` deltaP `2.7458` edge `0.0174` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.008` n `149` status `ready` deltaP `-9.0267` edge `-0.0283` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3234` n `149` status `ready` deltaP `4.119` edge `-0.0216` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.6237` n `148` status `ready` deltaP `-0.2393` edge `0.0016` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.9954` n `148` status `ready` deltaP `-3.3174` edge `-0.0044` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.8465` n `148` status `ready` deltaP `2.6182` edge `-0.1249` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.3921` n `149` status `ready` deltaP `-3.7823` edge `-0.1427` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
