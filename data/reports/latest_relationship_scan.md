# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T00:22:27.112481+00:00`
- Price records: `672`
- Market context records: `5827`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10074`

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

- `market_context_high->equity_4h` score `0.4833` n `276` status `ready` deltaP `7.1028` edge `0.1387` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2449` n `276` status `ready` deltaP `2.5124` edge `0.0004` maxDD `-0.5499`
- `market_context_high->equity_24h` score `-0.3631` n `248` status `ready` deltaP `15.3954` edge `0.375` maxDD `-31.6316`
- `market_context_high->commodity_1h` score `-0.5231` n `276` status `ready` deltaP `-0.716` edge `-0.0014` maxDD `-2.2045`
- `market_context_high->equity_1h` score `-0.553` n `276` status `ready` deltaP `3.211` edge `0.0332` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.5856` n `276` status `ready` deltaP `0.7789` edge `0.0045` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.5897` n `276` status `ready` deltaP `2.5276` edge `0.0011` maxDD `-2.0339`
- `market_context_high->crypto_major_1h` score `-0.887` n `276` status `ready` deltaP `3.1025` edge `0.0375` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0599` n `276` status `ready` deltaP `1.5035` edge `0.0351` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1407` n `276` status `ready` deltaP `1.1687` edge `0.0147` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.5073` n `248` status `ready` deltaP `9.4422` edge `0.0256` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.5659` n `276` status `ready` deltaP `-0.9522` edge `0.0005` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2147` n `276` status `ready` deltaP `-4.8957` edge `-0.0454` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.7009` n `276` status `ready` deltaP `-1.2858` edge `-0.0167` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.819` n `248` status `ready` deltaP `3.7131` edge `0.0283` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.0012` n `276` status `ready` deltaP `6.9658` edge `0.1407` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.765` n `276` status `ready` deltaP `4.3147` edge `0.075` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7737` n `248` status `ready` deltaP `-12.4608` edge `-0.0612` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-6.8018` n `248` status `ready` deltaP `-1.5513` edge `-0.2226` maxDD `-15.3767`
- `market_context_high->crypto_alt_24h` score `-12.5935` n `248` status `ready` deltaP `-10.2542` edge `-0.5155` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
