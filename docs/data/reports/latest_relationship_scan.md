# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T09:22:28.662348+00:00`
- Price records: `672`
- Market context records: `5757`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8666`

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

- `market_context_high->equity_24h` score `0.7799` n `225` status `ready` deltaP `15.1181` edge `0.5071` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1459` n `285` status `ready` deltaP `7.3679` edge `0.1269` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1954` n `294` status `ready` deltaP `3.2924` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4331` n `294` status `ready` deltaP `1.9044` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6285` n `294` status `ready` deltaP `3.1682` edge `0.0272` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6492` n `294` status `ready` deltaP `-0.0142` edge `0.0037` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7659` n `294` status `ready` deltaP `-1.7822` edge `-0.0056` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.7672` n `294` status `ready` deltaP `3.5918` edge `0.0356` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.85` n `294` status `ready` deltaP `2.2445` edge `0.0346` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-0.9284` n `225` status `ready` deltaP `14.4167` edge `0.0432` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1544` n `285` status `ready` deltaP `1.4752` edge `0.0109` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2199` n `285` status `ready` deltaP `3.3189` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.621` n `285` status `ready` deltaP `-7.3888` edge `-0.0492` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.6841` n `285` status `ready` deltaP `8.0643` edge `0.1531` maxDD `-25.1094`
- `market_context_high->index_24h` score `-2.9588` n `225` status `ready` deltaP `0.8888` edge `0.0292` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7285` n `285` status `ready` deltaP `-2.3636` edge `-0.0274` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.8212` n `285` status `ready` deltaP `6.4019` edge `0.1079` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.6225` n `225` status `ready` deltaP `6.9723` edge `0.014` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.8569` n `225` status `ready` deltaP `-10.1111` edge `-0.2514` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.8446` n `225` status `ready` deltaP `-13.0903` edge `-0.0858` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
