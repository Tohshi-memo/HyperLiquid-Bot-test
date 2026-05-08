# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T08:52:15.009188+00:00`
- Price records: `631`
- Market context records: `738`
- Flow alert records: `2084`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.5426` n `146` status `ready` deltaP `29.9116` edge `0.8792` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5701` n `146` status `ready` deltaP `7.7263` edge `0.5008` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.0501` n `146` status `ready` deltaP `1.108` edge `0.1963` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.2935` n `154` status `ready` deltaP `6.0631` edge `0.0091` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3838` n `158` status `ready` deltaP `3.4836` edge `0.0026` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6129` n `158` status `ready` deltaP `1.2405` edge `0.0381` maxDD `-3.7959`
- `market_context_high->equity_24h` score `-0.6559` n `146` status `ready` deltaP `-0.552` edge `0.2095` maxDD `-10.5047`
- `market_context_high->equity_1h` score `-0.6573` n `158` status `ready` deltaP `-0.575` edge `0.0006` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.8609` n `158` status `ready` deltaP `1.3511` edge `0.0046` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.073` n `158` status `ready` deltaP `5.6013` edge `-0.0026` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.442` n `158` status `ready` deltaP `4.1255` edge `-0.0162` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5528` n `158` status `ready` deltaP `-4.6847` edge `-0.021` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5538` n `154` status `ready` deltaP `17.447` edge `0.1248` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7859` n `154` status `ready` deltaP `1.5963` edge `-0.0072` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1573` n `154` status `ready` deltaP `2.325` edge `0.0617` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6268` n `154` status `ready` deltaP `-1.3497` edge `0.0053` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1118` n `158` status `ready` deltaP `-3.6137` edge `-0.0393` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6909` n `154` status `ready` deltaP `-5.6826` edge `0.0804` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.8004` n `154` status `ready` deltaP `4.9382` edge `-0.1618` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.337` n `146` status `ready` deltaP `-15.1124` edge `-0.0663` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
