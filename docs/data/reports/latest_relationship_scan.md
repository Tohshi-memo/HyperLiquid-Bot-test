# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T07:37:16.751864+00:00`
- Price records: `626`
- Market context records: `732`
- Flow alert records: `2068`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `12.2211` n `146` status `ready` deltaP `29.328` edge `0.8563` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4732` n `146` status `ready` deltaP `7.8057` edge `0.4922` maxDD `-0.0508`
- `market_context_high->index_24h` score `-0.1381` n `146` status `ready` deltaP `0.4349` edge `0.1851` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.3378` n `150` status `ready` deltaP `5.3597` edge `0.0081` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.4254` n `156` status `ready` deltaP `2.9935` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5338` n `156` status `ready` deltaP `1.9604` edge `0.0399` maxDD `-3.7959`
- `market_context_high->equity_24h` score `-0.8804` n `146` status `ready` deltaP `-1.2735` edge `0.1956` maxDD `-10.5047`
- `market_context_high->index_1h` score `-0.9006` n `156` status `ready` deltaP `1.0207` edge `0.0035` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.9981` n `150` status `ready` deltaP `17.541` edge `0.1257` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.0511` n `156` status `ready` deltaP `-0.7592` edge `-0.0015` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0882` n `156` status `ready` deltaP `5.4436` edge `-0.0035` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.474` n `156` status `ready` deltaP `3.9801` edge `-0.0179` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.6155` n `156` status `ready` deltaP `-4.9736` edge `-0.0243` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.8665` n `150` status `ready` deltaP `0.9637` edge `-0.0097` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.0595` n `150` status `ready` deltaP `2.7978` edge `0.0667` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.8258` n `150` status `ready` deltaP `-2.0066` edge `-0.0069` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1998` n `156` status `ready` deltaP `-4.1883` edge `-0.0428` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5684` n `150` status `ready` deltaP `-5.0957` edge `0.0867` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9658` n `150` status `ready` deltaP `4.2951` edge `-0.1713` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2843` n `146` status `ready` deltaP `-14.5789` edge `-0.0631` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
