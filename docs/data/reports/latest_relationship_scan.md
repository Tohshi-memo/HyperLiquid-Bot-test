# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T02:37:29.274305+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8270`

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

- `market_context_high->unknown_24h` score `1258.2771` n `148` status `ready` deltaP `-2.135` edge `104.9634` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.0462` n `149` status `ready` deltaP `4.2325` edge `1.8242` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.7594` n `148` status `ready` deltaP `19.7213` edge `0.0006` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3003` n `149` status `ready` deltaP `8.766` edge `0.0024` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0407` n `149` status `ready` deltaP `8.601` edge `0.0059` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1284` n `149` status `ready` deltaP `7.8779` edge `0.0057` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3203` n `149` status `ready` deltaP `6.6803` edge `0.0427` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3403` n `149` status `ready` deltaP `8.2686` edge `0.0384` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.5973` n `149` status `ready` deltaP `0.1085` edge `0.0079` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7632` n `149` status `ready` deltaP `-4.0731` edge `-0.0024` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8555` n `149` status `ready` deltaP `7.5319` edge `-0.0058` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-1.0138` n `148` status `ready` deltaP `8.5867` edge `0.0155` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.435` n `149` status `ready` deltaP `0.4903` edge `0.004` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5314` n `149` status `ready` deltaP `2.7458` edge `0.0217` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0492` n `149` status `ready` deltaP `-9.3315` edge `-0.0297` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3023` n `149` status `ready` deltaP `4.119` edge `-0.0189` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.7425` n `148` status `ready` deltaP `-0.2393` edge `-0.0083` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.2038` n `148` status `ready` deltaP `-3.6646` edge `-0.0288` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4444` n `149` status `ready` deltaP `-3.9347` edge `-0.1484` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.5127` n `148` status `ready` deltaP `2.271` edge `-0.1781` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
