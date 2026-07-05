# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T19:07:26.480088+00:00`
- Price records: `672`
- Market context records: `5802`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9058`

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

- `market_context_high->equity_24h` score `0.4241` n `248` status `ready` deltaP `15.3954` edge `0.4406` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0881` n `297` status `ready` deltaP `5.8687` edge `0.1174` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2232` n `297` status `ready` deltaP `2.8247` edge `0.0011` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.6119` n `297` status `ready` deltaP `2.5994` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.627` n `297` status `ready` deltaP `0.429` edge `0.0036` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6287` n `297` status `ready` deltaP `3.1957` edge `0.027` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7876` n `297` status `ready` deltaP `-2.2627` edge `-0.0054` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9022` n `297` status `ready` deltaP `3.2728` edge `0.0351` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1034` n `297` status `ready` deltaP `1.5142` edge `0.0314` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2314` n `297` status `ready` deltaP `0.1884` edge `0.0096` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.2566` n `248` status `ready` deltaP `11.968` edge `0.0351` maxDD `-5.0787`
- `market_context_high->fx_4h` score `-1.4378` n `297` status `ready` deltaP `1.0009` edge `0.0039` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.1553` n `297` status `ready` deltaP `-2.7178` edge `-0.0228` maxDD `-11.4992`
- `market_context_high->metal_4h` score `-2.4015` n `297` status `ready` deltaP `-4.8303` edge `-0.0467` maxDD `-10.9852`
- `market_context_high->index_24h` score `-2.8011` n `248` status `ready` deltaP `3.7131` edge `0.0306` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.8202` n `297` status `ready` deltaP `8.028` edge `0.1487` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.4624` n `297` status `ready` deltaP `5.6074` edge `0.0916` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.3105` n `248` status `ready` deltaP `-6.1436` edge `-0.2448` maxDD `-23.529`
- `market_context_high->crypto_major_24h` score `-9.7554` n `248` status `ready` deltaP `-0.8456` edge `-0.2067` maxDD `-32.3821`
- `market_context_high->commodity_24h` score `-10.0485` n `248` status `ready` deltaP `-13.6089` edge `-0.0751` maxDD `-36.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
