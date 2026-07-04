# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T22:37:27.060630+00:00`
- Price records: `672`
- Market context records: `5711`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `1.7672` n `268` status `ready` deltaP `11.0984` edge `0.2104` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0219` n `218` status `ready` deltaP `16.9805` edge `0.5257` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.6506` n `268` status `ready` deltaP `8.523` edge `0.1583` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1525` n `268` status `ready` deltaP `6.6414` edge `0.1323` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2188` n `280` status `ready` deltaP `2.8571` edge `0.001` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.388` n `280` status `ready` deltaP `3.7447` edge `0.0383` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4382` n `280` status `ready` deltaP `1.775` edge `-0.0005` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5505` n `280` status `ready` deltaP `2.006` edge `0.0351` maxDD `-3.8812`
- `market_context_high->equity_1h` score `-0.5753` n `280` status `ready` deltaP `3.7126` edge `0.028` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6167` n `280` status `ready` deltaP `0.4619` edge `0.0047` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0944` n `280` status `ready` deltaP `-1.003` edge `-0.0038` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.1468` n `218` status `ready` deltaP `10.4644` edge `0.0411` maxDD `-3.6309`
- `market_context_high->index_4h` score `-1.2214` n `268` status `ready` deltaP `0.1411` edge `0.0112` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2956` n `268` status `ready` deltaP `1.8657` edge `0.0054` maxDD `-1.382`
- `market_context_high->metal_4h` score `-2.623` n `268` status `ready` deltaP `-7.3216` edge `-0.0499` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8565` n `218` status `ready` deltaP `2.3923` edge `0.0323` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8754` n `268` status `ready` deltaP `-4.0339` edge `-0.0285` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.6059` n `218` status `ready` deltaP `5.7706` edge `0.0234` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.9189` n `218` status `ready` deltaP `-7.0559` edge `-0.2406` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.0467` n `218` status `ready` deltaP `-10.7846` edge `-0.0711` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
