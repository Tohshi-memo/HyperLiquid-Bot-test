# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T07:07:27.796582+00:00`
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

- `market_context_high->unknown_24h` score `1267.0455` n `148` status `ready` deltaP `-2.135` edge `105.6941` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `19.8538` n `149` status `ready` deltaP `4.2325` edge `1.6415` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.6077` n `148` status `ready` deltaP `18.6796` edge `-0.0051` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2093` n `149` status `ready` deltaP `7.7181` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0639` n `149` status `ready` deltaP `7.534` edge `0.0043` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0829` n `149` status `ready` deltaP `10.5551` edge `0.0446` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1431` n `149` status `ready` deltaP `7.5785` edge `0.0058` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4044` n `149` status `ready` deltaP `5.7821` edge `0.0379` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4524` n `149` status `ready` deltaP `1.6055` edge `0.01` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.836` n `149` status `ready` deltaP `7.5319` edge `-0.0033` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8512` n `149` status `ready` deltaP `-5.4204` edge `-0.0047` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.2285` n `148` status `ready` deltaP `6.5034` edge `0.0115` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5355` n `149` status `ready` deltaP `-0.4079` edge `-0.0029` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6257` n `149` status `ready` deltaP `1.8476` edge `0.0156` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1693` n `149` status `ready` deltaP `-10.3986` edge `-0.0326` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3125` n `149` status `ready` deltaP `3.2043` edge `-0.0141` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.8601` n `148` status `ready` deltaP `-0.2393` edge `-0.0181` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.0462` n `148` status `ready` deltaP `-3.6646` edge `-0.0086` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.5383` n `149` status `ready` deltaP `-5.1542` edge `-0.1523` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9507` n `148` status `ready` deltaP `2.271` edge `-0.2146` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
