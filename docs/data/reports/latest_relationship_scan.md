# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T08:07:16.644987+00:00`
- Price records: `532`
- Market context records: `628`
- Flow alert records: `1777`
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

- `market_context_high->crypto_major_24h` score `5.4595` n `146` status `ready` deltaP `15.8634` edge `0.3826` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.2338` n `146` status `ready` deltaP `7.3426` edge `0.392` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0635` n `146` status `ready` deltaP `9.3911` edge `0.0164` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3032` n `146` status `ready` deltaP `2.2691` edge `0.0038` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4759` n `146` status `ready` deltaP `2.1437` edge `0.0435` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7408` n `146` status `ready` deltaP `-0.8732` edge `-0.0038` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.13` n `146` status `ready` deltaP `-3.9046` edge `-0.0078` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2706` n `146` status `ready` deltaP `5.2927` edge `-0.0097` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.377` n `146` status `ready` deltaP `-2.9724` edge `-0.0139` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.8057` n `146` status `ready` deltaP `5.0435` edge `-0.0118` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9348` n `146` status `ready` deltaP `4.4759` edge `0.0659` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3735` n `146` status `ready` deltaP `-1.3377` edge `-0.0366` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4377` n `146` status `ready` deltaP `13.7783` edge `0.0756` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9737` n `146` status `ready` deltaP `-8.1748` edge `0.0062` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.393` n `146` status `ready` deltaP `-3.8768` edge `-0.0417` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4451` n `146` status `ready` deltaP `-5.2148` edge `-0.0564` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5618` n `146` status `ready` deltaP `-5.9878` edge `0.0932` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2603` n `146` status `ready` deltaP `-2.2514` edge `-0.014` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.727` n `146` status `ready` deltaP `2.0707` edge `-0.2199` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.9428` n `146` status `ready` deltaP `-11.4631` edge `-0.075` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
