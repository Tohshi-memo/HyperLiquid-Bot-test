# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T22:52:28.257846+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9520`

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

- `market_context_high->unknown_4h` score `45.469` n `46` status `ready` deltaP `6.4024` edge `3.7464` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6571` n `46` status `ready` deltaP `13.5341` edge `2.3968` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2277` n `46` status `ready` deltaP `12.1453` edge `1.2814` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.4035` n `46` status `ready` deltaP `10.7639` edge `1.0452` maxDD `0.0`
- `market_context_high->index_24h` score `5.5035` n `46` status `ready` deltaP `19.6105` edge `0.3366` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9635` n `96` status `ready` deltaP `-9.2014` edge `1.1608` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.9248` n `96` status `ready` deltaP `37.1528` edge `0.2806` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9291` n `96` status `ready` deltaP `14.3293` edge `0.2063` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.5941` n `96` status `ready` deltaP `10.061` edge `0.2489` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9649` n `97` status `ready` deltaP `11.0702` edge `0.1295` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8206` n `46` status `ready` deltaP `21.7921` edge `0.0198` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.4452` n `97` status `ready` deltaP `13.0163` edge `0.073` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.356` n `96` status `ready` deltaP `20.249` edge `0.0416` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.7371` n `96` status `ready` deltaP `22.2222` edge `0.1053` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.7106` n `46` status `ready` deltaP `20.0106` edge `-0.0508` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.6531` n `46` status `ready` deltaP `5.8644` edge `0.0396` maxDD `-0.2751`
- `news_risk_high->metal_1h` score `0.6492` n `97` status `ready` deltaP `15.3806` edge `0.0109` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6195` n `46` status `ready` deltaP `10.056` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->crypto_alt_24h` score `0.5126` n `96` status `ready` deltaP `-9.0278` edge `0.591` maxDD `-32.7147`
- `news_risk_high->metal_24h` score `0.2929` n `96` status `ready` deltaP `16.8403` edge `0.0097` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
