# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T22:07:39.930754+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8464`

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

- `market_context_high->unknown_24h` score `1241.7387` n `148` status `ready` deltaP `-2.135` edge `103.5852` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.006` n `149` status `ready` deltaP `4.385` edge `1.7365` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.1121` n `148` status `ready` deltaP `21.8046` edge `0.0161` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1961` n `149` status `ready` deltaP `7.5684` edge `0.0017` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.1052` n `149` status `ready` deltaP `7.0767` edge `0.0039` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1174` n `149` status `ready` deltaP `8.0276` edge `0.0061` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3181` n `149` status `ready` deltaP `7.8112` edge `0.0433` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4014` n `149` status `ready` deltaP `6.2312` edge `0.0353` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.632` n `149` status `ready` deltaP `-0.3406` edge `0.008` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.6884` n `148` status `ready` deltaP `11.3645` edge `0.0241` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.7499` n `149` status `ready` deltaP `-3.7737` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8785` n `149` status `ready` deltaP `7.0746` edge `-0.0057` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4077` n `149` status `ready` deltaP `0.9394` edge `0.0045` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6273` n `149` status `ready` deltaP `2.2967` edge `0.0124` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1501` n `149` status `ready` deltaP `-10.3986` edge `-0.031` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4986` n `149` status `ready` deltaP `3.5092` edge `-0.04` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5433` n `148` status `ready` deltaP `-0.2393` edge `0.0083` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.5986` n `148` status `ready` deltaP `-1.5812` edge `0.0349` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.0104` n `148` status `ready` deltaP `4.3543` edge `-0.0668` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.5402` n `149` status `ready` deltaP `-4.6969` edge `-0.1556` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
