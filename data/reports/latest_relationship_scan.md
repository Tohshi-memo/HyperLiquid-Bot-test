# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T00:37:21.530617+00:00`
- Price records: `502`
- Market context records: `596`
- Flow alert records: `1685`
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

- `market_context_high->crypto_alt_24h` score `4.5376` n `146` status `ready` deltaP `6.9506` edge `0.3366` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.4784` n `146` status `ready` deltaP `10.2537` edge `0.2549` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0639` n `146` status `ready` deltaP `11.3312` edge `0.0198` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3161` n `146` status `ready` deltaP `1.991` edge `0.004` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.6433` n `146` status `ready` deltaP `0.8374` edge `-0.0027` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.6487` n `146` status `ready` deltaP `1.1841` edge `0.0355` maxDD `-3.7959`
- `market_context_high->unknown_1h` score `-1.1443` n `146` status `ready` deltaP `-4.0986` edge `-0.0077` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2311` n `146` status `ready` deltaP `-1.7941` edge `-0.0096` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.2319` n `146` status `ready` deltaP `5.1467` edge `-0.0055` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.8276` n `146` status `ready` deltaP `4.7697` edge `-0.0118` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0986` n `146` status `ready` deltaP `3.1935` edge `0.0608` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1988` n `146` status `ready` deltaP `0.5457` edge `-0.0346` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.4349` n `146` status `ready` deltaP `-6.6892` edge `0.0412` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.7721` n `146` status `ready` deltaP `12.6585` edge `0.0552` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.2634` n `146` status `ready` deltaP `-3.3962` edge `-0.0341` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3023` n `146` status `ready` deltaP `-4.69` edge `-0.048` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8219` n `146` status `ready` deltaP `-7.4546` edge `0.0813` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3539` n `146` status `ready` deltaP `-3.5712` edge `-0.0172` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.4548` n `146` status `ready` deltaP `-10.4784` edge `-0.0409` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-5.051` n `146` status `ready` deltaP `0.7356` edge `-0.238` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
