# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T00:22:35.636116+00:00`
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

- `market_context_high->unknown_24h` score `1255.1907` n `148` status `ready` deltaP `-2.135` edge `104.7062` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.8784` n `149` status `ready` deltaP `4.385` edge `1.8092` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.8899` n `148` status `ready` deltaP `20.2421` edge `0.008` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2967` n `149` status `ready` deltaP `8.766` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0165` n `149` status `ready` deltaP `8.4486` edge `0.0049` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1073` n `149` status `ready` deltaP `8.1773` edge `0.0064` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3523` n `149` status `ready` deltaP `6.5306` edge `0.0396` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4312` n `149` status `ready` deltaP `7.5064` edge `0.0359` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6261` n `149` status `ready` deltaP `-0.1909` edge `0.0075` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7593` n `149` status `ready` deltaP `-3.9234` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8335` n `149` status `ready` deltaP `7.6844` edge `-0.004` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.8734` n `148` status `ready` deltaP `9.802` edge `0.0191` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.4288` n `149` status `ready` deltaP `0.7897` edge `0.0028` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5767` n `149` status `ready` deltaP `2.5961` edge `0.0169` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0092` n `149` status `ready` deltaP `-9.0267` edge `-0.0284` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3329` n `149` status `ready` deltaP `3.9665` edge `-0.0218` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.6117` n `148` status `ready` deltaP `-0.2393` edge `0.0026` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.9325` n `148` status `ready` deltaP `-3.1437` edge `0.0025` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.7354` n `148` status `ready` deltaP `2.7918` edge `-0.1168` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.3952` n `149` status `ready` deltaP `-3.7823` edge `-0.1431` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
