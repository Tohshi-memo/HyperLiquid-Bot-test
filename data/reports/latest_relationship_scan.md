# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T06:37:27.297454+00:00`
- Price records: `672`
- Market context records: `5745`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8662`

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

- `market_context_high->equity_24h` score `0.8381` n `218` status `ready` deltaP `14.6614` edge `0.5176` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1666` n `285` status `ready` deltaP `7.6728` edge `0.1266` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2061` n `285` status `ready` deltaP `3.0854` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4463` n `285` status `ready` deltaP `1.6352` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6421` n `285` status `ready` deltaP `0.1382` edge `0.0036` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6908` n `285` status `ready` deltaP `2.4635` edge `0.0267` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7714` n `285` status `ready` deltaP `-1.8878` edge `-0.0056` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8476` n `285` status `ready` deltaP `2.7813` edge `0.0343` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.9156` n `285` status `ready` deltaP `1.6352` edge `0.0332` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.0019` n `218` status `ready` deltaP `12.9444` edge `0.0436` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1551` n `285` status `ready` deltaP `1.4752` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2207` n `285` status `ready` deltaP `3.3189` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6051` n `285` status `ready` deltaP `-7.0839` edge `-0.0492` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.6803` n `285` status `ready` deltaP `8.2168` edge `0.1524` maxDD `-25.1094`
- `market_context_high->index_24h` score `-3.048` n `218` status `ready` deltaP `-0.5097` edge `0.0271` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.6993` n `285` status `ready` deltaP `-2.0587` edge `-0.027` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.8502` n `285` status `ready` deltaP `6.2494` edge `0.1065` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-3.8652` n `218` status `ready` deltaP `8.7586` edge `0.0652` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.8191` n `218` status `ready` deltaP `-9.6856` edge `-0.2494` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.8277` n `218` status `ready` deltaP `-13.1785` edge `-0.0838` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
