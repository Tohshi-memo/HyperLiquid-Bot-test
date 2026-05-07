# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T13:37:14.858930+00:00`
- Price records: `554`
- Market context records: `650`
- Flow alert records: `1845`
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

- `market_context_high->crypto_major_24h` score `7.3833` n `146` status `ready` deltaP `19.5101` edge `0.5186` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.0543` n `146` status `ready` deltaP `8.7037` edge `0.4513` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1634` n `146` status `ready` deltaP `7.8447` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3578` n `146` status `ready` deltaP `1.3548` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.3963` n `146` status `ready` deltaP `2.524` edge `0.0476` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6522` n `146` status `ready` deltaP `0.3362` edge `-0.0005` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.2248` n `146` status `ready` deltaP `-4.6849` edge `-0.0105` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2608` n `146` status `ready` deltaP `-2.0448` edge `-0.0104` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.273` n `146` status `ready` deltaP `5.2927` edge `-0.0099` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.7009` n `146` status `ready` deltaP `5.589` edge `-0.0067` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1215` n `146` status `ready` deltaP `3.7022` edge `0.0555` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1605` n `146` status `ready` deltaP `0.2745` edge `-0.0296` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3386` n `146` status `ready` deltaP `14.297` edge `0.0804` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9265` n `146` status `ready` deltaP `-8.9192` edge `0.0151` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.1472` n `146` status `ready` deltaP `-4.3302` edge `0.1167` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.3791` n `146` status `ready` deltaP `-4.0326` edge `-0.0395` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4716` n `146` status `ready` deltaP `-5.2603` edge `-0.0583` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.5191` n `146` status `ready` deltaP `-5.5941` edge `-0.0249` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6806` n `146` status `ready` deltaP `-11.4416` edge `-0.0533` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9161` n `146` status `ready` deltaP `0.5016` edge `-0.2252` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
