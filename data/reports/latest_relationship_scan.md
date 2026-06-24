# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T03:37:31.849074+00:00`
- Price records: `672`
- Market context records: `4583`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9993`

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

- `market_context_high->unknown_1h` score `69.9294` n `157` status `ready` deltaP `6.585` edge `5.8336` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.6773` n `157` status `ready` deltaP `8.2171` edge `0.3727` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.6101` n `157` status `ready` deltaP `4.3091` edge `0.0013` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.626` n `157` status `ready` deltaP `1.0994` edge `0.0201` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.7621` n `157` status `ready` deltaP `-0.697` edge `-0.0034` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8206` n `157` status `ready` deltaP `2.5011` edge `-0.0096` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8641` n `157` status `ready` deltaP `-2.0386` edge `0.0015` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.054` n `157` status `ready` deltaP `2.1147` edge `0.0277` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.1915` n `157` status `ready` deltaP `3.6614` edge `0.0336` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5816` n `157` status `ready` deltaP `-2.9749` edge `-0.0111` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.3483` n `155` status `ready` deltaP `1.7014` edge `-0.1147` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.8902` n `157` status `ready` deltaP `-3.6558` edge `-0.081` maxDD `-17.8795`
- `market_context_high->index_24h` score `-5.1828` n `155` status `ready` deltaP `-6.6712` edge `-0.0825` maxDD `-29.3321`
- `market_context_high->fx_24h` score `-5.2589` n `155` status `ready` deltaP `-11.642` edge `-0.0094` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.438` n `157` status `ready` deltaP `-2.2264` edge `-0.1096` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.9109` n `155` status `ready` deltaP `8.3815` edge `0.036` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.6991` n `157` status `ready` deltaP `-5.9365` edge `-0.1434` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0002` n `157` status `ready` deltaP `-3.1876` edge `-0.2669` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.1586` n `157` status `ready` deltaP `-7.0578` edge `-0.3336` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.9136` n `157` status `ready` deltaP `-3.4217` edge `-0.4102` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
