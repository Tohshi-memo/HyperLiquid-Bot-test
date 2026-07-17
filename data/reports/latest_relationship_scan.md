# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T20:22:29.577364+00:00`
- Price records: `672`
- Market context records: `7064`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.6513` n `185` status `ready` deltaP `16.9017` edge `0.0116` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1907` n `185` status `ready` deltaP `4.0541` edge `0.0022` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3244` n `185` status `ready` deltaP `1.7171` edge `0.0334` maxDD `-4.5815`
- `market_context_high->unknown_1h` score `-0.4035` n `185` status `ready` deltaP `-0.4863` edge `0.0283` maxDD `-1.6946`
- `market_context_high->crypto_major_1h` score `-0.595` n `185` status `ready` deltaP `3.9375` edge `0.0327` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.7803` n `185` status `ready` deltaP `-0.7688` edge `-0.0038` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8224` n `185` status `ready` deltaP `-3.9537` edge `-0.0023` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.8714` n `185` status `ready` deltaP `-4.6779` edge `-0.0189` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-0.9129` n `185` status `ready` deltaP `-5.3304` edge `0.1229` maxDD `-4.742`
- `market_context_high->commodity_4h` score `-1.6225` n `185` status `ready` deltaP `-7.0327` edge `-0.0451` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.863` n `185` status `ready` deltaP `4.6698` edge `-0.0277` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3291` n `185` status `ready` deltaP `0.81` edge `-0.0341` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4415` n `185` status `ready` deltaP `-2.4569` edge `-0.0562` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.9033` n `185` status `ready` deltaP `0.7827` edge `0.0011` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.06` n `185` status `ready` deltaP `2.7373` edge `0.0179` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5368` n `185` status `ready` deltaP `-0.0178` edge `-0.0119` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.6024` n `185` status `ready` deltaP `0.1986` edge `-0.0032` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-3.9611` n `185` status `ready` deltaP `-15.4129` edge `0.1096` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9052` n `185` status `ready` deltaP `4.3721` edge `-0.1556` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.5148` n `185` status `ready` deltaP `-20.6917` edge `-0.0956` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
