# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T23:52:28.908028+00:00`
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

- `market_context_high->commodity_4h` score `1.2741` n `150` status `ready` deltaP `15.2357` edge `0.0719` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8373` n `162` status `ready` deltaP `10.8856` edge `0.0315` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4193` n `129` status `ready` deltaP `17.882` edge `0.0212` maxDD `-1.9329`
- `market_context_high->metal_24h` score `0.2899` n `129` status `ready` deltaP `1.8936` edge `0.0733` maxDD `-2.2743`
- `market_context_high->equity_24h` score `-0.0824` n `129` status `ready` deltaP `2.0429` edge `0.2855` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.2735` n `129` status `ready` deltaP `2.3821` edge `0.1022` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5241` n `162` status `ready` deltaP `1.4212` edge `-0.0036` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6996` n `162` status `ready` deltaP `-3.8183` edge `-0.0088` maxDD `-1.4345`
- `market_context_high->index_4h` score `-0.7048` n `150` status `ready` deltaP `-2.9167` edge `-0.0104` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.7218` n `150` status `ready` deltaP `2.6667` edge `-0.0026` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.976` n `162` status `ready` deltaP `-4.1731` edge `-0.0058` maxDD `-0.8168`
- `market_context_high->metal_4h` score `-1.17` n `150` status `ready` deltaP `-3.128` edge `-0.0214` maxDD `-3.2863`
- `market_context_high->equity_1h` score `-1.1916` n `162` status `ready` deltaP `-1.7816` edge `-0.0004` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.5801` n `162` status `ready` deltaP `-9.3553` edge `-0.0437` maxDD `-5.0545`
- `market_context_high->equity_4h` score `-2.7776` n `150` status `ready` deltaP `-3.6809` edge `-0.0732` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.7474` n `162` status `ready` deltaP `-11.5232` edge `-0.0665` maxDD `-10.1838`
- `market_context_high->crypto_major_24h` score `-4.2918` n `129` status `ready` deltaP `1.1668` edge `-0.116` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.403` n `150` status `ready` deltaP `-9.7744` edge `-0.13` maxDD `-7.0737`
- `market_context_high->crypto_alt_24h` score `-4.7269` n `129` status `ready` deltaP `-13.1259` edge `-0.1621` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.5435` n `162` status `ready` deltaP `-4.9383` edge `-0.55` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
