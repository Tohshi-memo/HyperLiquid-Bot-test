# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T03:22:31.645552+00:00`
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

- `market_context_high->unknown_24h` score `1259.8107` n `148` status `ready` deltaP `-2.135` edge `105.0912` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `18.5806` n `149` status `ready` deltaP `4.2325` edge `1.5354` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.7438` n `148` status `ready` deltaP `19.7213` edge `-0.0007` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2871` n `149` status `ready` deltaP `8.6163` edge `0.0023` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0431` n `149` status `ready` deltaP `8.601` edge `0.0061` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1284` n `149` status `ready` deltaP `7.8779` edge `0.0057` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.2881` n `149` status `ready` deltaP `8.7259` edge `0.0397` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3273` n `149` status `ready` deltaP `6.5306` edge `0.0428` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.571` n `149` status `ready` deltaP `0.4079` edge `0.0081` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7819` n `149` status `ready` deltaP `-4.3725` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8531` n `149` status `ready` deltaP `7.5319` edge `-0.0055` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-1.0361` n `148` status `ready` deltaP `8.4131` edge `0.0148` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.4428` n `149` status `ready` deltaP `0.4903` edge `0.003` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5236` n `149` status `ready` deltaP `2.7458` edge `0.0227` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0504` n `149` status `ready` deltaP `-9.3315` edge `-0.0298` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.2501` n `149` status `ready` deltaP `4.119` edge `-0.0122` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.7689` n `148` status `ready` deltaP `-0.2393` edge `-0.0105` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.1734` n `148` status `ready` deltaP `-3.6646` edge `-0.0249` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4296` n `149` status `ready` deltaP `-3.9347` edge `-0.1465` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.6327` n `148` status `ready` deltaP `2.271` edge `-0.1881` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
