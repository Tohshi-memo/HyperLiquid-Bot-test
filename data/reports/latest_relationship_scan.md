# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T21:08:05.580765+00:00`
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

- `market_context_high->unknown_24h` score `1233.7443` n `148` status `ready` deltaP `-2.135` edge `102.919` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.1416` n `149` status `ready` deltaP `4.385` edge `1.7478` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.2108` n `148` status `ready` deltaP `22.4991` edge `0.0197` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1721` n `149` status `ready` deltaP `7.269` edge `0.0017` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1252` n `149` status `ready` deltaP `7.8779` edge `0.0061` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1576` n `149` status `ready` deltaP `6.4669` edge `0.0036` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.3496` n `149` status `ready` deltaP `7.5064` edge `0.0427` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4123` n `149` status `ready` deltaP `6.0815` edge `0.0349` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5769` n `149` status `ready` deltaP `0.2582` edge `0.0086` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.6088` n `148` status `ready` deltaP `12.059` edge `0.0261` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.7671` n `149` status `ready` deltaP `-4.0731` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8469` n `149` status `ready` deltaP `7.5319` edge `-0.0047` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4101` n `149` status `ready` deltaP `0.9394` edge `0.0042` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6429` n `149` status `ready` deltaP `2.147` edge `0.0114` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1647` n `149` status `ready` deltaP `-10.5511` edge `-0.0312` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.486` n `148` status `ready` deltaP `-0.8868` edge `0.0447` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4893` n `149` status `ready` deltaP `3.5092` edge `-0.0388` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5157` n `148` status `ready` deltaP `-0.2393` edge `0.0106` maxDD `-10.1587`
- `market_context_high->equity_24h` score `-3.6884` n `148` status `ready` deltaP `5.0488` edge `-0.0446` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.5317` n `149` status `ready` deltaP `-4.6969` edge `-0.1545` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
