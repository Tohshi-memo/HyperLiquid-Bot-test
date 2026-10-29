# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T05:07:29.222968+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8165`

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

- `market_context_high->unknown_24h` score `1263.5499` n `148` status `ready` deltaP `-2.135` edge `105.4028` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `18.7426` n `149` status `ready` deltaP `4.2325` edge `1.5489` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.6884` n `148` status `ready` deltaP `19.3741` edge `-0.003` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2248` n `149` status `ready` deltaP `7.8678` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0005` n `149` status `ready` deltaP `8.1437` edge `0.0056` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1533` n `149` status `ready` deltaP `7.4288` edge `0.0055` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.1607` n `149` status `ready` deltaP `9.7929` edge `0.0432` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3686` n `149` status `ready` deltaP `6.2312` edge `0.0395` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5099` n `149` status `ready` deltaP `1.0067` edge `0.0092` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.8317` n `149` status `ready` deltaP `-5.121` edge `-0.0042` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8453` n `149` status `ready` deltaP `7.5319` edge `-0.0045` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-1.0958` n `148` status `ready` deltaP `7.8923` edge `0.0133` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5207` n `149` status `ready` deltaP `-0.2582` edge `-0.002` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5805` n `149` status `ready` deltaP `2.2967` edge `0.0184` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.054` n `149` status `ready` deltaP `-9.3315` edge `-0.0301` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.1744` n `149` status `ready` deltaP `4.119` edge `-0.0025` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.8193` n `148` status `ready` deltaP `-0.2393` edge `-0.0147` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.1086` n `148` status `ready` deltaP `-3.6646` edge `-0.0166` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4047` n `149` status `ready` deltaP `-3.9347` edge `-0.1433` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.8475` n `148` status `ready` deltaP `2.271` edge `-0.206` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
