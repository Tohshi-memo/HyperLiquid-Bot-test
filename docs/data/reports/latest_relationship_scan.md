# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T01:07:12.038463+00:00`
- Price records: `504`
- Market context records: `598`
- Flow alert records: `1691`
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

- `market_context_high->crypto_alt_24h` score `4.5454` n `146` status `ready` deltaP `6.9131` edge `0.3375` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.5823` n `146` status `ready` deltaP `10.6533` edge `0.2609` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0486` n `146` status `ready` deltaP `11.1118` edge `0.0193` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3272` n `146` status `ready` deltaP `1.809` edge `0.0038` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.6283` n `146` status `ready` deltaP `1.0799` edge `-0.0024` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.6706` n `146` status `ready` deltaP `0.9694` edge `0.0351` maxDD `-3.7959`
- `market_context_high->unknown_1h` score `-1.1164` n `146` status `ready` deltaP `-3.8849` edge `-0.0068` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1709` n `146` status `ready` deltaP `5.3836` edge `-0.002` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.1905` n `146` status `ready` deltaP `-1.5411` edge `-0.0079` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7789` n `146` status `ready` deltaP `4.989` edge `-0.0092` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0341` n `146` status `ready` deltaP `3.4752` edge `0.0643` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.188` n `146` status `ready` deltaP `0.6057` edge `-0.0341` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.4589` n `146` status `ready` deltaP `-6.7951` edge `0.0399` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.7143` n `146` status `ready` deltaP `12.9014` edge `0.0584` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.2143` n `146` status `ready` deltaP `-3.1133` edge `-0.0319` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2976` n `146` status `ready` deltaP `-4.6603` edge `-0.0478` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8484` n `146` status `ready` deltaP `-7.6955` edge `0.0807` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3401` n `146` status `ready` deltaP `-3.4111` edge `-0.0165` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.4856` n `146` status `ready` deltaP `-10.5486` edge `-0.043` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-5.0087` n `146` status `ready` deltaP `0.9937` edge `-0.2362` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
