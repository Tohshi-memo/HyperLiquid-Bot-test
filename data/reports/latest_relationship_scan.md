# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T05:37:27.681217+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8159`

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

- `market_context_high->unknown_24h` score `1264.3383` n `148` status `ready` deltaP `-2.135` edge `105.4685` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `18.937` n `149` status `ready` deltaP `4.2325` edge `1.5651` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.6499` n `148` status `ready` deltaP `19.0269` edge `-0.0039` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2117` n `149` status `ready` deltaP `7.7181` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0275` n `149` status `ready` deltaP `7.8388` edge `0.0053` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.1279` n `149` status `ready` deltaP `10.0978` edge `0.0439` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1525` n `149` status `ready` deltaP `7.4288` edge `0.0056` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4029` n `149` status `ready` deltaP `5.9318` edge `0.0371` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4823` n `149` status `ready` deltaP `1.3061` edge `0.0095` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.8426` n `149` status `ready` deltaP `-5.2707` edge `-0.0046` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8438` n `149` status `ready` deltaP `7.5319` edge `-0.0043` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-1.1296` n `148` status `ready` deltaP `7.5451` edge `0.0128` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5425` n `149` status `ready` deltaP `-0.4079` edge `-0.0038` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6289` n `149` status `ready` deltaP `1.9973` edge `0.0142` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0868` n `149` status `ready` deltaP `-9.6364` edge `-0.0308` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.1908` n `149` status `ready` deltaP `4.119` edge `-0.0046` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.8349` n `148` status `ready` deltaP `-0.2393` edge `-0.016` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.1102` n `148` status `ready` deltaP `-3.6646` edge `-0.0168` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4385` n `149` status `ready` deltaP `-4.2396` edge `-0.1456` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9075` n `148` status `ready` deltaP `2.271` edge `-0.211` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
