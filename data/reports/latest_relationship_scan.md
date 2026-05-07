# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T14:37:13.645470+00:00`
- Price records: `558`
- Market context records: `654`
- Flow alert records: `1857`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `7.6625` n `146` status `ready` deltaP `20.1358` edge `0.5377` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.0898` n `146` status `ready` deltaP `8.6225` edge `0.4548` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1439` n `146` status `ready` deltaP `8.2192` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3463` n `146` status `ready` deltaP `1.5766` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4073` n `146` status `ready` deltaP `2.4907` edge `0.0469` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6223` n `146` status `ready` deltaP `0.5953` edge `0.0016` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.1549` n `146` status `ready` deltaP `5.7193` edge `-0.0029` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.1865` n `146` status `ready` deltaP `-4.4755` edge `-0.0087` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1953` n `146` status `ready` deltaP `-1.5866` edge `-0.008` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.5893` n `146` status `ready` deltaP `5.9789` edge `0.0` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0576` n `146` status `ready` deltaP `4.0211` edge `0.0587` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.0799` n `146` status `ready` deltaP `0.7562` edge `-0.0261` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.2254` n `146` status `ready` deltaP `14.7222` edge `0.087` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9219` n `146` status `ready` deltaP `-9.0866` edge `0.0166` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.0594` n `146` status `ready` deltaP `-4.0434` edge `0.1221` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.2864` n `146` status `ready` deltaP `-3.5189` edge `-0.0352` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4477` n `146` status `ready` deltaP `-5.2025` edge `-0.0567` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.563` n `146` status `ready` deltaP `-6.1674` edge `-0.0267` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7367` n `146` status `ready` deltaP `-11.5571` edge `-0.0572` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8963` n `146` status `ready` deltaP `0.599` edge `-0.2242` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
