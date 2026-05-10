# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T12:22:18.589711+00:00`
- Price records: `672`
- Market context records: `975`
- Flow alert records: `2730`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.2883` n `150` status `ready` deltaP `35.2084` edge `1.0727` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.756` n `150` status `ready` deltaP `11.8056` edge `0.7343` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2568` n `150` status `ready` deltaP `0.8264` edge `0.3597` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.568` n `150` status `ready` deltaP `-1.118` edge `0.2543` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2056` n `210` status `ready` deltaP `3.7425` edge `0.0387` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.6033` n `210` status `ready` deltaP `1.0194` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.638` n `210` status `ready` deltaP `1.2746` edge `0.0152` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6543` n `199` status `ready` deltaP `2.0185` edge `0.0023` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7186` n `210` status `ready` deltaP `3.071` edge `0.005` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.1082` n `210` status `ready` deltaP `5.6729` edge `-0.0076` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.1704` n `210` status `ready` deltaP `-1.075` edge `-0.0132` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.5159` n `199` status `ready` deltaP `0.9867` edge `0.0823` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.6791` n `199` status `ready` deltaP `-1.3735` edge `0.0215` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8199` n `210` status `ready` deltaP `-1.199` edge `-0.0294` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0505` n `210` status `ready` deltaP `0.134` edge `-0.0278` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.5838` n `199` status `ready` deltaP `8.5626` edge `0.0982` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.9139` n `199` status `ready` deltaP `-0.6695` edge `0.0784` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.0978` n `199` status `ready` deltaP `8.4102` edge `-0.1264` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.2559` n `199` status `ready` deltaP `-1.4869` edge `0.0164` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-3.9967` n `150` status `ready` deltaP `5.1875` edge `0.0036` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
