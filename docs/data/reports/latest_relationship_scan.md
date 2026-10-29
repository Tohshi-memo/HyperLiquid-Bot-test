# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T04:52:29.309868+00:00`
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

- `market_context_high->unknown_24h` score `1263.1455` n `148` status `ready` deltaP `-2.135` edge `105.3691` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `18.7342` n `149` status `ready` deltaP `4.2325` edge `1.5482` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.7083` n `148` status `ready` deltaP `19.5477` edge `-0.0025` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2368` n `149` status `ready` deltaP `8.0175` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0151` n `149` status `ready` deltaP `8.2962` edge `0.0058` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1431` n `149` status `ready` deltaP `7.5785` edge `0.0058` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.1789` n `149` status `ready` deltaP `9.6405` edge `0.0427` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3444` n `149` status `ready` deltaP `6.3809` edge `0.0416` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5123` n `149` status `ready` deltaP `1.0067` edge `0.009` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.8208` n `149` status `ready` deltaP `-4.9713` edge `-0.0038` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8461` n `149` status `ready` deltaP `7.5319` edge `-0.0046` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-1.0795` n `148` status `ready` deltaP `8.0659` edge `0.0135` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.4989` n `149` status `ready` deltaP `-0.1085` edge `-0.0002` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5548` n `149` status `ready` deltaP `2.4464` edge `0.0207` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0528` n `149` status `ready` deltaP `-9.3315` edge `-0.03` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.1689` n `149` status `ready` deltaP `4.119` edge `-0.0018` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.8097` n `148` status `ready` deltaP `-0.2393` edge `-0.0139` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.1055` n `148` status `ready` deltaP `-3.6646` edge `-0.0162` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4031` n `149` status `ready` deltaP `-3.9347` edge `-0.1431` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.8055` n `148` status `ready` deltaP `2.271` edge `-0.2025` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
