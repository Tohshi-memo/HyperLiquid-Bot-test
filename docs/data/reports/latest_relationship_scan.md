# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T17:52:24.832617+00:00`
- Price records: `672`
- Market context records: `5688`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8784`

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

- `market_context_high->equity_24h` score `1.7705` n `207` status `ready` deltaP `16.1761` edge `0.5476` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2422` n `257` status `ready` deltaP `12.1003` edge `0.2227` maxDD `-11.6547`
- `market_context_high->crypto_alt_4h` score `0.7699` n `257` status `ready` deltaP `9.1878` edge `0.1648` maxDD `-7.6179`
- `market_context_high->equity_4h` score `0.1815` n `257` status `ready` deltaP `6.059` edge `0.1386` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.252` n `269` status `ready` deltaP `2.117` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.389` n `269` status `ready` deltaP `2.9128` edge `0.0409` maxDD `-4.7522`
- `market_context_high->metal_1h` score `-0.4996` n `269` status `ready` deltaP `0.625` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5463` n `269` status `ready` deltaP `4.3424` edge `0.0416` maxDD `-6.2858`
- `market_context_high->equity_1h` score `-0.5738` n `269` status `ready` deltaP `3.6413` edge `0.0286` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6424` n `269` status `ready` deltaP `0.0262` edge `0.0043` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.9419` n `269` status `ready` deltaP `0.2632` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1384` n `257` status `ready` deltaP `4.5589` edge `0.0071` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2925` n `257` status `ready` deltaP `-0.8767` edge `0.0073` maxDD `-3.04`
- `market_context_high->fx_24h` score `-1.3785` n `207` status `ready` deltaP `13.5115` edge `0.0463` maxDD `-3.1001`
- `market_context_high->index_24h` score `-2.6097` n `207` status `ready` deltaP `5.2159` edge `0.0359` maxDD `-17.42`
- `market_context_high->metal_4h` score `-2.8397` n `257` status `ready` deltaP `-11.0255` edge `-0.053` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.8141` n `257` status `ready` deltaP `-2.7736` edge `-0.0318` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.6933` n `207` status `ready` deltaP `4.3026` edge `0.0259` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.24` n `207` status `ready` deltaP `-11.3828` edge `-0.247` maxDD `-32.6818`
- `market_context_high->commodity_24h` score `-12.034` n `207` status `ready` deltaP `-10.2204` edge `-0.0738` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
