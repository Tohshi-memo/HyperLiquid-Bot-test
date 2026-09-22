# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T19:37:29.548342+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `45.8634` n `46` status `ready` deltaP `7.0122` edge `3.7752` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4652` n `46` status `ready` deltaP `12.6661` edge `2.3866` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2313` n `46` status `ready` deltaP `12.1453` edge `1.2817` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.0658` n `46` status `ready` deltaP `11.6319` edge `1.0946` maxDD `0.0`
- `market_context_high->index_24h` score `5.5275` n `46` status `ready` deltaP `19.6105` edge `0.3386` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.3141` n `96` status `ready` deltaP `39.4097` edge `0.298` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.7717` n `96` status `ready` deltaP `-10.0694` edge `1.1506` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `3.0163` n `96` status `ready` deltaP `14.939` edge `0.2095` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.9911` n `96` status `ready` deltaP `11.7378` edge `0.2708` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.233` n `96` status `ready` deltaP `12.5811` edge `0.1376` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8656` n `46` status `ready` deltaP `22.2494` edge `0.0205` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5518` n `96` status `ready` deltaP `13.9284` edge `0.0758` maxDD `-1.8141`
- `news_risk_high->crypto_alt_24h` score `1.1748` n `96` status `ready` deltaP `-8.1598` edge `0.6404` maxDD `-32.7147`
- `news_risk_high->fx_4h` score `1.171` n `96` status `ready` deltaP `18.2673` edge `0.0394` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.0448` n `46` status `ready` deltaP `22.2676` edge `-0.038` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.7274` n `46` status `ready` deltaP `6.6129` edge `0.0408` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6303` n `46` status `ready` deltaP `10.2057` edge `0.0098` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5957` n `96` status `ready` deltaP `14.7268` edge `0.0108` maxDD `-0.7468`
- `news_risk_high->fx_24h` score `0.5527` n `96` status `ready` deltaP `19.9653` edge `0.0967` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `0.5101` n `96` status `ready` deltaP `19.0973` edge `0.0225` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
