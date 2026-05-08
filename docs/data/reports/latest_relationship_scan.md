# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T02:37:16.374110+00:00`
- Price records: `606`
- Market context records: `710`
- Flow alert records: `2006`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.0748` n `146` status `ready` deltaP `26.8788` edge `0.7771` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4891` n `146` status `ready` deltaP `8.1386` edge `0.4913` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2474` n `149` status `ready` deltaP `6.6942` edge `0.0108` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2948` n `149` status `ready` deltaP `2.7014` edge `0.002` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4736` n `149` status `ready` deltaP `2.3378` edge `0.0424` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6255` n `149` status `ready` deltaP `0.3693` edge `0.0027` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.9174` n `146` status `ready` deltaP `-2.3905` edge `0.139` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.1008` n `149` status `ready` deltaP `16.5715` edge `0.119` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.1744` n `149` status `ready` deltaP `-1.6397` edge `-0.0059` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1776` n `149` status `ready` deltaP `-4.1696` edge `-0.01` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3174` n `149` status `ready` deltaP `4.9477` edge `-0.0113` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5691` n `149` status `ready` deltaP `6.3959` edge `-0.0011` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.7441` n `149` status `ready` deltaP `1.9837` edge `-0.0063` maxDD `-6.5149`
- `market_context_high->equity_24h` score `-1.9734` n `146` status `ready` deltaP `-4.3018` edge `0.1247` maxDD `-10.5047`
- `market_context_high->crypto_alt_4h` score `-1.9763` n `149` status `ready` deltaP `3.8528` edge `0.0666` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6731` n `149` status `ready` deltaP `-1.088` edge `-0.0003` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3846` n `149` status `ready` deltaP `-5.1327` edge `-0.0519` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7738` n `149` status `ready` deltaP `-6.2384` edge `0.0772` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2379` n `149` status `ready` deltaP `3.2636` edge `-0.1871` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0782` n `146` status `ready` deltaP `-12.3396` edge `-0.0516` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
