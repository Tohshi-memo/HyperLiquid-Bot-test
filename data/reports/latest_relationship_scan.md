# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T13:22:25.563375+00:00`
- Price records: `672`
- Market context records: `5775`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8674`

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

- `market_context_high->equity_24h` score `0.6681` n `233` status `ready` deltaP `15.6064` edge `0.4895` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1536` n `290` status `ready` deltaP `7.7503` edge `0.125` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2762` n `302` status `ready` deltaP `1.8053` edge `0.0008` maxDD `-0.5266`
- `market_context_high->equity_1h` score `-0.5863` n `302` status `ready` deltaP `3.7098` edge `0.0271` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6166` n `302` status `ready` deltaP `2.54` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7909` n `302` status `ready` deltaP `-2.3268` edge `-0.0054` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.8449` n `302` status `ready` deltaP `3.6741` edge `0.0372` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-0.9242` n `233` status `ready` deltaP `14.7831` edge `0.0413` maxDD `-3.6674`
- `market_context_high->index_1h` score `-0.9629` n `302` status `ready` deltaP `0.4352` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.0471` n `302` status `ready` deltaP `1.964` edge `0.0331` maxDD `-6.6758`
- `market_context_high->fx_4h` score `-1.2705` n `290` status `ready` deltaP `2.4211` edge `0.0055` maxDD `-1.4288`
- `market_context_high->index_4h` score `-1.8482` n `290` status `ready` deltaP `0.6318` edge `0.0105` maxDD `-3.165`
- `market_context_high->commodity_4h` score `-2.4434` n `290` status `ready` deltaP `-2.8501` edge `-0.0267` maxDD `-14.071`
- `market_context_high->metal_4h` score `-2.5355` n `290` status `ready` deltaP `-6.1375` edge `-0.0482` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.847` n `290` status `ready` deltaP `7.7533` edge `0.1483` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.8764` n `233` status `ready` deltaP `2.3843` edge `0.0298` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4228` n `290` status `ready` deltaP `5.4121` edge `0.0962` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-5.9005` n `233` status `ready` deltaP `4.1533` edge `-0.0487` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0378` n `233` status `ready` deltaP `-7.8684` edge `-0.2429` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.9083` n `233` status `ready` deltaP `-13.8762` edge `-0.0789` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
