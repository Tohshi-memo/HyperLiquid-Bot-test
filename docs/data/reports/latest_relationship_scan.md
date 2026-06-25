# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T01:07:33.325162+00:00`
- Price records: `672`
- Market context records: `4676`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `76.4062` n `138` status `ready` deltaP `11.6007` edge `6.3316` maxDD `-1.674`
- `market_context_high->unknown_4h` score `4.742` n `138` status `ready` deltaP `10.1869` edge `0.4483` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.4972` n `138` status `ready` deltaP `9.4203` edge `0.1543` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5678` n `138` status `ready` deltaP `1.1672` edge `0.0245` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.8235` n `138` status `ready` deltaP `3.0908` edge `-0.0139` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.8436` n `138` status `ready` deltaP `-0.0023` edge `0.0001` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8758` n `138` status `ready` deltaP `-2.7727` edge `0.0049` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.9546` n `138` status `ready` deltaP `-2.9528` edge `-0.0044` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.3138` n `138` status `ready` deltaP `4.2639` edge `0.0139` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.4107` n `138` status `ready` deltaP `0.0398` edge `-0.0042` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.8055` n `138` status `ready` deltaP `-5.2938` edge `-0.0143` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.7827` n `138` status `ready` deltaP `-3.5039` edge `-0.0766` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7` n `138` status `ready` deltaP `-10.5148` edge `-0.0107` maxDD `-5.536`
- `market_context_high->commodity_24h` score `-5.0375` n `138` status `ready` deltaP `12.7264` edge `0.0458` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.6465` n `138` status `ready` deltaP `-3.3477` edge `-0.1195` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8084` n `138` status `ready` deltaP `-6.2223` edge `-0.1506` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.0716` n `138` status `ready` deltaP `-9.4128` edge `-0.0724` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.5764` n `138` status `ready` deltaP `-2.8986` edge `-0.2145` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.3346` n `138` status `ready` deltaP `-2.5229` edge `-0.2901` maxDD `-64.8531`
- `market_context_high->crypto_major_4h` score `-11.7055` n `138` status `ready` deltaP `-4.73` edge `-0.3748` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
