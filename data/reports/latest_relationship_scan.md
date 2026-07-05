# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T14:37:24.675876+00:00`
- Price records: `672`
- Market context records: `5781`
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

- `market_context_high->equity_24h` score `0.5507` n `238` status `ready` deltaP `15.374` edge `0.476` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1076` n `295` status `ready` deltaP `7.5491` edge `0.1225` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2637` n `305` status `ready` deltaP `2.0742` edge `0.0009` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.5862` n `305` status `ready` deltaP `3.7411` edge `0.0269` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6215` n `305` status `ready` deltaP `2.5086` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7609` n `305` status `ready` deltaP `-1.7959` edge `-0.0051` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.8947` n `305` status `ready` deltaP `3.3214` edge `0.0354` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.9389` n `305` status `ready` deltaP `0.7196` edge `0.0038` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9469` n `238` status `ready` deltaP `14.4068` edge `0.0409` maxDD `-3.6674`
- `market_context_high->crypto_alt_1h` score `-1.0076` n `305` status `ready` deltaP `2.2166` edge `0.0347` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1998` n `295` status `ready` deltaP `0.647` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3358` n `295` status `ready` deltaP `1.5094` edge `0.0048` maxDD `-1.5565`
- `market_context_high->commodity_4h` score `-2.4557` n `295` status `ready` deltaP `-3.1764` edge `-0.0261` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8575` n `238` status `ready` deltaP `2.7471` edge `0.0298` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.8974` n `295` status `ready` deltaP `7.6632` edge `0.1447` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8911` n `295` status `ready` deltaP `-6.0464` edge `-0.048` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.4714` n `295` status `ready` deltaP `5.3746` edge `0.0924` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-6.6404` n `238` status `ready` deltaP `2.8595` edge `-0.0809` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.066` n `238` status `ready` deltaP `-7.8708` edge `-0.2465` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.9138` n `238` status `ready` deltaP `-13.6744` edge `-0.0807` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
