# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T00:07:26.458207+00:00`
- Price records: `672`
- Market context records: `5826`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10024`

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

- `market_context_high->equity_4h` score `0.4741` n `277` status `ready` deltaP `7.0629` edge `0.1382` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2463` n `277` status `ready` deltaP `2.4698` edge `0.0005` maxDD `-0.5499`
- `market_context_high->equity_24h` score `-0.3151` n `248` status `ready` deltaP `15.3954` edge `0.379` maxDD `-31.6316`
- `market_context_high->commodity_1h` score `-0.5185` n `277` status `ready` deltaP `-0.6734` edge `-0.0011` maxDD `-2.2045`
- `market_context_high->index_1h` score `-0.5761` n `277` status `ready` deltaP `0.9463` edge `0.0046` maxDD `-0.7819`
- `market_context_high->equity_1h` score `-0.5792` n `277` status `ready` deltaP `2.9886` edge `0.0325` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5911` n `277` status `ready` deltaP `2.5401` edge `0.0009` maxDD `-2.0339`
- `market_context_high->crypto_major_1h` score `-0.8958` n `277` status `ready` deltaP `3.1124` edge `0.0367` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0659` n `277` status `ready` deltaP `1.5186` edge `0.0345` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1429` n `277` status `ready` deltaP `1.1105` edge `0.0148` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.505` n `248` status `ready` deltaP `9.4422` edge `0.0259` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.5535` n `277` status `ready` deltaP `-0.7743` edge `0.0009` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2026` n `277` status `ready` deltaP `-4.7217` edge `-0.045` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.694` n `277` status `ready` deltaP `-1.2146` edge `-0.0166` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.819` n `248` status `ready` deltaP `3.7131` edge `0.0283` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9704` n `277` status `ready` deltaP `7.0953` edge `0.1424` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.7297` n `277` status `ready` deltaP `4.4559` edge `0.077` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7729` n `248` status `ready` deltaP `-12.4608` edge `-0.0611` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-6.9097` n `248` status `ready` deltaP `-1.7809` edge `-0.2232` maxDD `-15.5925`
- `market_context_high->crypto_alt_24h` score `-12.5527` n `248` status `ready` deltaP `-10.0246` edge `-0.5118` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
