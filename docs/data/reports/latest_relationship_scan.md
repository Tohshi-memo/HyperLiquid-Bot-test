# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T05:37:29.878410+00:00`
- Price records: `672`
- Market context records: `5849`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9866` n `30` status `ready` deltaP `24.0818` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8667` n `30` status `ready` deltaP `11.5369` edge `0.0809` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.75` n `255` status `ready` deltaP `7.9777` edge `0.1551` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2403` n `30` status `ready` deltaP `5.1697` edge `0.0425` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3091` n `255` status `ready` deltaP `1.3367` edge `0.0` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.3962` n `30` status `ready` deltaP `1.8363` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4506` n `255` status `ready` deltaP `4.1764` edge `0.0353` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.4955` n `255` status `ready` deltaP `3.405` edge `0.0031` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5308` n `255` status `ready` deltaP `-0.9381` edge `-0.0017` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.5915` n `255` status `ready` deltaP `0.6957` edge `0.0043` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8446` n `255` status `ready` deltaP `3.4977` edge `0.0384` maxDD `-6.2348`
- `market_context_high->equity_24h` score `-0.8813` n `227` status `ready` deltaP `17.1531` edge `0.3201` maxDD `-31.6316`
- `market_context_high->crypto_alt_1h` score `-1.0031` n `255` status `ready` deltaP `2.2285` edge `0.035` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.186` n `255` status `ready` deltaP `0.4161` edge `0.0139` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2229` n `30` status `ready` deltaP `-12.2455` edge `-0.0237` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7455` n `255` status `ready` deltaP `-3.9862` edge `-0.0023` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.8285` n `227` status `ready` deltaP `4.6301` edge `0.0165` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0938` n `255` status `ready` deltaP `-4.4202` edge `-0.0386` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.3305` n `255` status `ready` deltaP `-0.266` edge `-0.0132` maxDD `-7.0053`
- `market_context_high->crypto_major_4h` score `-2.7705` n `255` status `ready` deltaP `7.3446` edge `0.1574` maxDD `-25.6458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
