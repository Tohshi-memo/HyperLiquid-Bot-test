# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T00:52:26.179437+00:00`
- Price records: `672`
- Market context records: `6339`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.3107` n `32` status `ready` deltaP `43.0556` edge `1.0036` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0968` n `32` status `ready` deltaP `50.6944` edge `0.1701` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3731` n `32` status `ready` deltaP `16.6667` edge `0.5275` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2033` n `32` status `ready` deltaP `43.8262` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.5224` n `32` status `ready` deltaP `31.0764` edge `0.1069` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3883` n `32` status `ready` deltaP `28.7425` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5255` n `32` status `ready` deltaP `14.8765` edge `0.1431` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9696` n `32` status `ready` deltaP `12.0696` edge `0.09` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5212` n `196` status `ready` deltaP `12.2232` edge `0.0416` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.0826` n `207` status `ready` deltaP `-7.5154` edge `0.1578` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0653` n `196` status `ready` deltaP `6.4118` edge `0.022` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.3617` n `207` status `ready` deltaP `4.3782` edge `0.0022` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.5375` n `138` status `ready` deltaP `15.9043` edge `0.0819` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.5662` n `207` status `ready` deltaP `-0.6567` edge `0.0001` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.7003` n `32` status `ready` deltaP `0.5208` edge `-0.0061` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.7184` n `196` status `ready` deltaP `4.9621` edge `0.0447` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.7312` n `207` status `ready` deltaP `-0.8469` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7714` n `32` status `ready` deltaP `-3.5928` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.8007` n `32` status `ready` deltaP `5.4828` edge `-0.0688` maxDD `-0.7581`
- `market_context_high->index_1h` score `-1.0145` n `207` status `ready` deltaP `-2.8884` edge `0.0025` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
