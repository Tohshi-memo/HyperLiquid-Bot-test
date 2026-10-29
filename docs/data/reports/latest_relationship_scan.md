# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T03:07:32.897624+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8255`

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

- `market_context_high->unknown_24h` score `1259.2983` n `148` status `ready` deltaP `-2.135` edge `105.0485` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `18.5758` n `149` status `ready` deltaP `4.2325` edge `1.535` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.7486` n `148` status `ready` deltaP `19.7213` edge `-0.0003` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2871` n `149` status `ready` deltaP `8.6163` edge `0.0023` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0419` n `149` status `ready` deltaP `8.601` edge `0.006` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1291` n `149` status `ready` deltaP `7.8779` edge `0.0056` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3063` n `149` status `ready` deltaP `8.5734` edge `0.0392` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3289` n `149` status `ready` deltaP `6.5306` edge `0.0426` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5829` n `149` status `ready` deltaP `0.2582` edge `0.0081` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7811` n `149` status `ready` deltaP `-4.3725` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8547` n `149` status `ready` deltaP `7.5319` edge `-0.0057` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-1.0325` n `148` status `ready` deltaP `8.4131` edge `0.0151` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.4404` n `149` status `ready` deltaP `0.4903` edge `0.0033` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5268` n `149` status `ready` deltaP `2.7458` edge `0.0223` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0504` n `149` status `ready` deltaP `-9.3315` edge `-0.0298` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.2688` n `149` status `ready` deltaP `4.119` edge `-0.0146` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.7617` n `148` status `ready` deltaP `-0.2393` edge `-0.0099` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.1851` n `148` status `ready` deltaP `-3.6646` edge `-0.0264` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4359` n `149` status `ready` deltaP `-3.9347` edge `-0.1473` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.5967` n `148` status `ready` deltaP `2.271` edge `-0.1851` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
