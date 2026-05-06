# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T22:51:56.564967+00:00`
- Price records: `495`
- Market context records: `588`
- Flow alert records: `1663`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.6371` n `146` status `ready` deltaP `7.0845` edge `0.344` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.289` n `146` status `ready` deltaP `10.0765` edge `0.2403` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0984` n `146` status `ready` deltaP `11.9034` edge `0.0204` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2785` n `146` status `ready` deltaP `2.6399` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5919` n `146` status `ready` deltaP `1.744` edge `0.0365` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6332` n `146` status `ready` deltaP `1.0` edge `-0.0025` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1942` n `146` status `ready` deltaP `-4.4527` edge `-0.0095` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2199` n `146` status `ready` deltaP `-1.6694` edge `-0.0095` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.2535` n `146` status `ready` deltaP `5.1168` edge `-0.0071` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.8732` n `146` status `ready` deltaP `4.3955` edge `-0.0131` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1733` n `146` status `ready` deltaP `2.8155` edge `0.0571` maxDD `-15.2248`
- `market_context_high->index_24h` score `-2.2473` n `146` status `ready` deltaP `-6.31` edge `0.0543` maxDD `-5.9609`
- `market_context_high->index_4h` score `-2.2724` n `146` status `ready` deltaP `0.0159` edge `-0.0372` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.9206` n `146` status `ready` deltaP `11.7925` edge `0.0486` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.3051` n `146` status `ready` deltaP `-4.6941` edge `-0.0482` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3596` n `146` status `ready` deltaP `-3.7736` edge `-0.0396` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.6968` n `146` status `ready` deltaP `-6.5955` edge `0.086` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.2679` n `146` status `ready` deltaP `-10.2271` edge `-0.027` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.4375` n `146` status `ready` deltaP `-4.1443` edge `-0.0241` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0915` n `146` status `ready` deltaP `0.8594` edge `-0.2422` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
