# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T19:22:26.980090+00:00`
- Price records: `672`
- Market context records: `5803`
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

- `market_context_high->equity_24h` score `0.3845` n `248` status `ready` deltaP `15.3954` edge `0.4373` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0975` n `296` status `ready` deltaP `5.7515` edge `0.1174` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2245` n `296` status `ready` deltaP `2.814` edge `0.001` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.6242` n `296` status `ready` deltaP `2.4458` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6351` n `296` status `ready` deltaP `0.2731` edge `0.0036` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6403` n `296` status `ready` deltaP `3.0648` edge `0.0269` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7773` n `296` status `ready` deltaP `-2.108` edge `-0.0054` maxDD `-3.7493`
- `market_context_high->crypto_major_1h` score `-0.9179` n `296` status `ready` deltaP `3.1215` edge `0.0348` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1182` n `296` status `ready` deltaP `1.3595` edge `0.0312` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2408` n `296` status `ready` deltaP `0.0371` edge `0.0094` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.2821` n `248` status `ready` deltaP `11.7383` edge `0.0346` maxDD `-5.1783`
- `market_context_high->fx_4h` score `-1.4278` n `296` status `ready` deltaP `1.1783` edge `0.004` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.1104` n `296` status `ready` deltaP `-2.7439` edge `-0.0221` maxDD `-11.08`
- `market_context_high->metal_4h` score `-2.3718` n `296` status `ready` deltaP `-4.6597` edge `-0.0464` maxDD `-10.7961`
- `market_context_high->crypto_major_4h` score `-2.7971` n `296` status `ready` deltaP `8.0916` edge `0.1502` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.8026` n `248` status `ready` deltaP `3.7131` edge `0.0304` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4425` n `296` status `ready` deltaP `5.6608` edge `0.0929` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.2064` n `248` status `ready` deltaP `-5.9139` edge `-0.2435` maxDD `-23.0213`
- `market_context_high->commodity_24h` score `-9.9218` n `248` status `ready` deltaP `-13.3792` edge `-0.0736` maxDD `-35.7887`
- `market_context_high->crypto_major_24h` score `-10.0354` n `248` status `ready` deltaP `-1.0752` edge `-0.2154` maxDD `-33.097`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
