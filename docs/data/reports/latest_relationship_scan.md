# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T01:22:26.965704+00:00`
- Price records: `672`
- Market context records: `5831`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10076`

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

- `market_context_high->equity_4h` score `0.5474` n `272` status `ready` deltaP `7.4695` edge `0.1416` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2658` n `272` status `ready` deltaP `2.1244` edge `0.0003` maxDD `-0.5499`
- `market_context_high->equity_24h` score `-0.5024` n `244` status `ready` deltaP `15.1838` edge `0.3648` maxDD `-31.6316`
- `market_context_high->equity_1h` score `-0.5047` n `272` status `ready` deltaP `3.6809` edge `0.0341` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.535` n `272` status `ready` deltaP `-0.9004` edge `-0.0017` maxDD `-2.2045`
- `market_context_high->metal_1h` score `-0.5813` n `272` status `ready` deltaP `2.6022` edge `0.0013` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.5836` n `272` status `ready` deltaP `0.8322` edge `0.0044` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.9348` n `272` status `ready` deltaP `2.8201` edge `0.0354` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0842` n `272` status `ready` deltaP `1.3495` edge `0.0341` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1629` n `272` status `ready` deltaP `0.7711` edge `0.0145` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.568` n `244` status `ready` deltaP `8.5894` edge `0.0235` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.6122` n `272` status `ready` deltaP `-1.6768` edge `-0.0006` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.194` n `272` status `ready` deltaP `-4.9587` edge `-0.0451` maxDD `-8.9164`
- `market_context_high->commodity_4h` score `-2.6474` n `272` status `ready` deltaP `-1.1568` edge `-0.0156` maxDD `-8.4513`
- `market_context_high->index_24h` score `-2.8722` n `244` status `ready` deltaP `3.0653` edge `0.0258` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.0766` n `272` status `ready` deltaP `6.6535` edge `0.1365` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.855` n `272` status `ready` deltaP `3.9545` edge `0.0699` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7235` n `244` status `ready` deltaP `-11.78` edge `-0.0593` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-6.0916` n `244` status `ready` deltaP `-1.0559` edge `-0.216` maxDD `-12.7678`
- `market_context_high->crypto_alt_24h` score `-12.691` n `244` status `ready` deltaP `-11.0343` edge `-0.5228` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
