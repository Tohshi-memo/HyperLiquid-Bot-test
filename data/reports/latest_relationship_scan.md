# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T10:22:28.321374+00:00`
- Price records: `672`
- Market context records: `5761`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8668`

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

- `market_context_high->equity_24h` score `0.7428` n `227` status `ready` deltaP `15.2434` edge `0.5015` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1521` n `284` status `ready` deltaP `7.3557` edge `0.1275` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2163` n `296` status `ready` deltaP `2.8908` edge `0.0011` maxDD `-0.5144`
- `market_context_high->index_1h` score `-0.6599` n `296` status `ready` deltaP `-0.2185` edge `0.0037` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6693` n `296` status `ready` deltaP `1.8814` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6749` n `296` status `ready` deltaP `2.723` edge `0.0263` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7854` n `296` status `ready` deltaP `-2.1423` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.9138` n `227` status `ready` deltaP `14.773` edge `0.0427` maxDD `-3.6674`
- `market_context_high->crypto_major_1h` score `-0.9324` n `296` status `ready` deltaP `3.1902` edge `0.0324` maxDD `-6.176`
- `market_context_high->crypto_alt_1h` score `-1.0525` n `296` status `ready` deltaP `1.8429` edge `0.0305` maxDD `-6.4394`
- `market_context_high->index_4h` score `-1.1563` n `284` status `ready` deltaP `1.4235` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2258` n `284` status `ready` deltaP `3.2055` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6245` n `284` status `ready` deltaP `-7.4845` edge `-0.0493` maxDD `-11.649`
- `market_context_high->crypto_major_4h` score `-2.659` n `284` status `ready` deltaP `8.0772` edge `0.1551` maxDD `-25.1094`
- `market_context_high->index_24h` score `-2.9373` n `227` status `ready` deltaP `1.2726` edge `0.0294` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7493` n `284` status `ready` deltaP `-2.5786` edge `-0.0277` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.7635` n `284` status `ready` deltaP `6.7631` edge `0.1103` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.9307` n `227` status `ready` deltaP `6.1506` edge `-0.0062` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6365` n `227` status `ready` deltaP `-9.5172` edge `-0.249` maxDD `-30.3268`
- `market_context_high->commodity_24h` score `-11.6082` n `227` status `ready` deltaP `-12.8893` edge `-0.0837` maxDD `-43.4841`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
