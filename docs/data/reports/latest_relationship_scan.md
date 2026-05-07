# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T09:07:23.009706+00:00`
- Price records: `536`
- Market context records: `632`
- Flow alert records: `1789`
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

- `market_context_high->crypto_major_24h` score `5.7416` n `146` status `ready` deltaP `16.5535` edge `0.4015` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.3263` n `146` status `ready` deltaP `7.2696` edge `0.4002` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0756` n `146` status `ready` deltaP `9.1882` edge `0.0162` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3258` n `146` status `ready` deltaP `1.9251` edge `0.0032` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5164` n `146` status `ready` deltaP `1.9225` edge `0.0416` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7224` n `146` status `ready` deltaP `-0.5941` edge `-0.0033` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1443` n `146` status `ready` deltaP `-4.0684` edge `-0.0079` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2369` n `146` status `ready` deltaP `5.549` edge `-0.0086` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3058` n `146` status `ready` deltaP `-2.4881` edge `-0.0112` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7604` n `146` status `ready` deltaP `5.2657` edge `-0.0095` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0497` n `146` status `ready` deltaP `4.2255` edge `0.058` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.4027` n `146` status `ready` deltaP `-1.5982` edge `-0.0373` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5175` n `146` status `ready` deltaP `13.4563` edge `0.0711` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0483` n `146` status `ready` deltaP `-8.3574` edge `0.0012` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.4279` n `146` status `ready` deltaP `-4.1175` edge `-0.043` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4355` n `146` status `ready` deltaP `-5.155` edge `-0.056` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.4732` n `146` status `ready` deltaP `-5.6759` edge `0.0985` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3049` n `146` status `ready` deltaP `-2.8843` edge `-0.0155` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7698` n `146` status `ready` deltaP `1.7755` edge `-0.2215` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.9596` n `146` status `ready` deltaP `-11.5841` edge `-0.0756` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
