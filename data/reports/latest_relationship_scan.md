# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T06:07:28.306389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8160`

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

- `market_context_high->unknown_24h` score `1265.1987` n `148` status `ready` deltaP `-2.135` edge `105.5402` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `19.3114` n `149` status `ready` deltaP `4.2325` edge `1.5963` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.6161` n `148` status `ready` deltaP `18.6796` edge `-0.0044` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2105` n `149` status `ready` deltaP `7.7181` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0445` n `149` status `ready` deltaP `7.6864` edge `0.0049` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0963` n `149` status `ready` deltaP `10.4027` edge `0.0445` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.133` n `149` status `ready` deltaP `7.7282` edge `0.0061` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4146` n `149` status `ready` deltaP `5.7821` edge `0.0366` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4548` n `149` status `ready` deltaP `1.6055` edge `0.0098` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8383` n `149` status `ready` deltaP `7.5319` edge `-0.0036` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8512` n `149` status `ready` deltaP `-5.4204` edge `-0.0047` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.1633` n `148` status `ready` deltaP `7.1978` edge `0.0123` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5425` n `149` status `ready` deltaP `-0.4079` edge `-0.0038` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6499` n `149` status `ready` deltaP `1.8476` edge `0.0125` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1196` n `149` status `ready` deltaP `-9.9413` edge `-0.0315` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.2386` n `149` status `ready` deltaP `3.8141` edge `-0.0087` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.8385` n `148` status `ready` deltaP `-0.2393` edge `-0.0163` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.0993` n `148` status `ready` deltaP `-3.6646` edge `-0.0154` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4761` n `149` status `ready` deltaP `-4.5445` edge `-0.1484` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9435` n `148` status `ready` deltaP `2.271` edge `-0.214` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
