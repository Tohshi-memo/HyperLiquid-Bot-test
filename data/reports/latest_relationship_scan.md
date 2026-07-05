# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T14:52:25.362179+00:00`
- Price records: `672`
- Market context records: `5782`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8718`

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

- `market_context_high->equity_24h` score `0.5219` n `239` status `ready` deltaP `15.2567` edge `0.4731` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.0809` n `296` status `ready` deltaP `7.3212` edge `0.1218` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2637` n `305` status `ready` deltaP `2.0742` edge `0.0009` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.5862` n `305` status `ready` deltaP `3.7411` edge `0.0269` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6203` n `305` status `ready` deltaP `2.5086` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7609` n `305` status `ready` deltaP `-1.7959` edge `-0.0051` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.8947` n `305` status `ready` deltaP `3.3214` edge `0.0354` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.9509` n `305` status `ready` deltaP `0.5699` edge `0.0038` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9528` n `239` status `ready` deltaP `14.3378` edge `0.0406` maxDD `-3.6674`
- `market_context_high->crypto_alt_1h` score `-1.0076` n `305` status `ready` deltaP `2.2166` edge `0.0347` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1998` n `296` status `ready` deltaP `0.6469` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3534` n `296` status `ready` deltaP `1.3307` edge `0.0046` maxDD `-1.625`
- `market_context_high->commodity_4h` score `-2.4613` n `296` status `ready` deltaP `-3.3001` edge `-0.026` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8576` n `239` status `ready` deltaP `2.7458` edge `0.0298` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9075` n `296` status `ready` deltaP `7.6425` edge `0.144` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8765` n `296` status `ready` deltaP `-5.8792` edge `-0.0479` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.4867` n `296` status `ready` deltaP `5.3642` edge `0.0912` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-6.794` n `239` status `ready` deltaP `2.5395` edge `-0.0874` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0717` n `239` status `ready` deltaP `-7.8757` edge `-0.2472` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.9314` n `239` status `ready` deltaP `-13.8344` edge `-0.0811` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
