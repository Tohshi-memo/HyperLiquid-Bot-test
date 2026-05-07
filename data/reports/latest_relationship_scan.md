# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T07:22:21.488673+00:00`
- Price records: `529`
- Market context records: `625`
- Flow alert records: `1768`
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

- `market_context_high->crypto_major_24h` score `5.3083` n `146` status `ready` deltaP `15.3374` edge `0.3735` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.225` n `146` status `ready` deltaP `7.3982` edge `0.3909` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0815` n `146` status `ready` deltaP `9.1033` edge `0.016` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3104` n `146` status `ready` deltaP `2.1468` edge `0.0037` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.527` n `146` status `ready` deltaP `1.8799` edge `0.041` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.727` n `146` status `ready` deltaP `-0.6534` edge `-0.0035` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1002` n `146` status `ready` deltaP `-3.6373` edge `-0.0071` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2279` n `146` status `ready` deltaP `5.5265` edge `-0.0077` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.346` n `146` status `ready` deltaP `-2.7647` edge `-0.0127` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7562` n `146` status `ready` deltaP `5.3033` edge `-0.0094` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.79` n `146` status `ready` deltaP `4.6663` edge `0.0767` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.3378` n `146` status `ready` deltaP `14.0231` edge `0.0823` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.348` n `146` status `ready` deltaP `-1.1398` edge `-0.0358` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.887` n `146` status `ready` deltaP `-8.0356` edge `0.0125` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.3376` n `146` status `ready` deltaP `-3.6938` edge `-0.0383` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3971` n `146` status `ready` deltaP `-4.9746` edge `-0.054` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6359` n `146` status `ready` deltaP `-6.2249` edge `0.0886` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2571` n `146` status `ready` deltaP `-2.2352` edge `-0.0137` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6886` n `146` status `ready` deltaP `2.2951` edge `-0.2182` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.867` n `146` status `ready` deltaP `-11.3708` edge `-0.0693` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
