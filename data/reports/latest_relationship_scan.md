# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T02:07:20.000141+00:00`
- Price records: `508`
- Market context records: `602`
- Flow alert records: `1703`
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

- `market_context_high->crypto_alt_24h` score `4.6739` n `146` status `ready` deltaP `6.8394` edge `0.3487` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.8469` n `146` status `ready` deltaP `11.441` edge `0.2777` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0206` n `146` status `ready` deltaP `10.6782` edge `0.0186` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3147` n `146` status `ready` deltaP `2.0493` edge `0.0038` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6142` n `146` status `ready` deltaP `1.3452` edge `0.0373` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6473` n `146` status `ready` deltaP `0.7589` edge `-0.0027` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.0867` n `146` status `ready` deltaP `5.8519` edge `0.0019` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.136` n `146` status `ready` deltaP `-3.8595` edge `-0.0086` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2069` n `146` status `ready` deltaP `-1.6411` edge `-0.0086` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7154` n `146` status `ready` deltaP `5.4223` edge `-0.0068` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.8468` n `146` status `ready` deltaP `4.0316` edge `0.0762` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2101` n `146` status `ready` deltaP `0.3144` edge `-0.034` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.5104` n `146` status `ready` deltaP `-7.0038` edge `0.037` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.5751` n `146` status `ready` deltaP `13.3812` edge `0.0668` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.194` n `146` status `ready` deltaP `-2.9643` edge `-0.0312` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3666` n `146` status `ready` deltaP `-4.9984` edge `-0.0513` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8053` n `146` status `ready` deltaP `-7.3518` edge `0.082` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3112` n `146` status `ready` deltaP `-3.0956` edge `-0.0149` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.5567` n `146` status `ready` deltaP `-10.6869` edge `-0.048` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9885` n `146` status `ready` deltaP `1.097` edge `-0.2352` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
