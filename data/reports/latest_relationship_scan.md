# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T00:22:26.290968+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.3063` n `152` status `ready` deltaP `15.3081` edge `0.0741` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8204` n `164` status `ready` deltaP `10.72` edge `0.0312` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4238` n `131` status `ready` deltaP `18.0437` edge `0.0207` maxDD `-1.9329`
- `market_context_high->metal_24h` score `-0.0132` n `131` status `ready` deltaP `0.6746` edge `0.0645` maxDD `-2.2743`
- `market_context_high->equity_24h` score `-0.2284` n `131` status `ready` deltaP `2.3033` edge `0.2716` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.2769` n `131` status `ready` deltaP `2.7963` edge `0.099` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4717` n `164` status `ready` deltaP `2.0009` edge `-0.0031` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.6015` n `164` status `ready` deltaP `-3.5709` edge `-0.0056` maxDD `-0.8168`
- `market_context_high->fx_4h` score `-0.6612` n `152` status `ready` deltaP `3.2895` edge `-0.0017` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.723` n `164` status `ready` deltaP `-4.1587` edge `-0.0092` maxDD `-1.4611`
- `market_context_high->index_4h` score `-0.7278` n `152` status `ready` deltaP `-3.3135` edge `-0.0107` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-1.1495` n `164` status `ready` deltaP `-1.2998` edge `-0.0001` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.2609` n `152` status `ready` deltaP `-3.8912` edge `-0.0236` maxDD `-3.6361`
- `market_context_high->crypto_alt_1h` score `-1.6301` n `164` status `ready` deltaP `-9.3252` edge `-0.0447` maxDD `-5.5029`
- `market_context_high->equity_4h` score `-2.8342` n `152` status `ready` deltaP `-4.148` edge `-0.0748` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.7956` n `164` status `ready` deltaP `-11.4028` edge `-0.0669` maxDD `-10.5372`
- `market_context_high->crypto_major_24h` score `-4.4094` n `131` status `ready` deltaP `0.4015` edge `-0.1207` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.6627` n `131` status `ready` deltaP `-12.6525` edge `-0.1599` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7793` n `152` status `ready` deltaP `-10.2536` edge `-0.1374` maxDD `-8.735`
- `market_context_high->unknown_1h` score `-7.5387` n `164` status `ready` deltaP `-4.7283` edge `-0.551` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
