# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T22:44:21.111859+00:00`
- Price records: `672`
- Market context records: `5820`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10006`

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

- `market_context_high->equity_4h` score `0.3353` n `283` status `ready` deltaP `6.3632` edge `0.1313` maxDD `-6.9958`
- `market_context_high->equity_24h` score `-0.0955` n `248` status `ready` deltaP `15.3954` edge `0.3973` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.1984` n `283` status `ready` deltaP `3.3151` edge `0.001` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.5455` n `283` status `ready` deltaP `-1.0574` edge `-0.002` maxDD `-2.2045`
- `market_context_high->metal_1h` score `-0.6127` n `283` status `ready` deltaP `2.3751` edge `0.0002` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6175` n `283` status `ready` deltaP `0.5544` edge `0.0031` maxDD `-0.8769`
- `market_context_high->equity_1h` score `-0.7067` n `283` status `ready` deltaP `2.3402` edge `0.0262` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9024` n `283` status `ready` deltaP `3.1358` edge `0.036` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0632` n `283` status `ready` deltaP `1.6266` edge `0.034` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1822` n `283` status `ready` deltaP `0.6405` edge `0.0129` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.483` n `283` status `ready` deltaP `0.2667` edge `0.003` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.4847` n `248` status `ready` deltaP `9.4422` edge `0.0285` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1469` n `283` status `ready` deltaP `-4.0571` edge `-0.0423` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.6982` n `283` status `ready` deltaP `-1.2222` edge `-0.0169` maxDD `-8.6511`
- `market_context_high->crypto_major_4h` score `-2.7346` n `283` status `ready` deltaP `7.8531` edge `0.157` maxDD `-25.6458`
- `market_context_high->index_24h` score `-4.3333` n `248` status `ready` deltaP `3.7131` edge `0.0286` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4632` n `283` status `ready` deltaP `5.2826` edge `0.0937` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7802` n `248` status `ready` deltaP `-12.4608` edge `-0.0616` maxDD `-30.3766`
- `market_context_high->metal_24h` score `-7.6071` n `248` status `ready` deltaP `-2.929` edge `-0.2287` maxDD `-17.1893`
- `market_context_high->crypto_alt_24h` score `-12.3669` n `248` status `ready` deltaP `-9.795` edge `-0.4904` maxDD `-61.7173`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
