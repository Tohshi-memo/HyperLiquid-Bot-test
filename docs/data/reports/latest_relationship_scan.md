# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T07:37:26.535263+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8168`

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

- `market_context_high->unknown_24h` score `1267.9587` n `148` status `ready` deltaP `-2.135` edge `105.7702` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `20.4022` n `149` status `ready` deltaP `4.2325` edge `1.6872` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.6077` n `148` status `ready` deltaP `18.6796` edge `-0.0051` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1841` n `149` status `ready` deltaP `7.4187` edge `0.0017` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.093` n `149` status `ready` deltaP `7.2291` edge `0.0039` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.1121` n `149` status `ready` deltaP `10.2503` edge `0.0442` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1517` n `149` status `ready` deltaP `7.4288` edge `0.0057` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4068` n `149` status `ready` deltaP `5.7821` edge `0.0376` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4643` n `149` status `ready` deltaP `1.4558` edge `0.01` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8375` n `149` status `ready` deltaP `7.5319` edge `-0.0035` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8512` n `149` status `ready` deltaP `-5.4204` edge `-0.0047` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.2611` n `148` status `ready` deltaP `6.1562` edge `0.0111` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5363` n `149` status `ready` deltaP `-0.4079` edge `-0.003` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6211` n `149` status `ready` deltaP `1.8476` edge `0.0162` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1875` n `149` status `ready` deltaP `-10.5511` edge `-0.0331` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3462` n `149` status `ready` deltaP `2.8995` edge `-0.0164` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.8685` n `148` status `ready` deltaP `-0.2393` edge `-0.0188` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.0096` n `148` status `ready` deltaP `-3.6646` edge `-0.0039` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.5604` n `149` status `ready` deltaP `-5.4591` edge `-0.1531` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9303` n `148` status `ready` deltaP `2.271` edge `-0.2129` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
