# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T12:37:25.174767+00:00`
- Price records: `672`
- Market context records: `5772`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8674`

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

- `market_context_high->equity_24h` score `0.6853` n `230` status `ready` deltaP `15.4273` edge `0.4929` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1526` n `287` status `ready` deltaP `7.5566` edge `0.1262` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2457` n `299` status `ready` deltaP `2.3236` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4159` n `299` status `ready` deltaP `2.2345` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6192` n `299` status `ready` deltaP `3.3145` edge `0.027` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.8022` n `299` status `ready` deltaP `-2.4989` edge `-0.0057` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.8975` n `299` status `ready` deltaP `3.362` edge `0.0349` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-0.908` n `230` status `ready` deltaP `15.0347` edge `0.0417` maxDD `-3.6674`
- `market_context_high->index_1h` score `-0.9619` n `299` status `ready` deltaP `0.4476` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.1098` n `299` status `ready` deltaP `1.6452` edge `0.03` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1907` n `287` status `ready` deltaP `0.8058` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2461` n `287` status `ready` deltaP `2.831` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5399` n `287` status `ready` deltaP `-6.2065` edge `-0.0483` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.8064` n `287` status `ready` deltaP `7.7962` edge `0.1514` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.9081` n `230` status `ready` deltaP `1.8357` edge `0.0294` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7753` n `287` status `ready` deltaP `-2.9181` edge `-0.0276` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-4.3861` n `287` status `ready` deltaP `5.4661` edge `0.0989` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-5.5095` n `230` status `ready` deltaP `4.8248` edge `-0.0331` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0309` n `230` status `ready` deltaP `-7.8849` edge `-0.2419` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.8537` n `230` status `ready` deltaP `-13.3892` edge `-0.0776` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
