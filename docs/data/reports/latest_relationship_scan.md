# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T09:07:32.546234+00:00`
- Price records: `672`
- Market context records: `7863`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `11.6361` n `126` status `ready` deltaP `28.9745` edge `0.9107` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.7014` n `127` status `ready` deltaP `6.4328` edge `0.335` maxDD `-6.4476`
- `market_context_high->metal_24h` score `1.6285` n `127` status `ready` deltaP `10.9799` edge `0.2449` maxDD `-2.2578`
- `market_context_high->commodity_24h` score `1.4027` n `126` status `ready` deltaP `21.9959` edge `0.1286` maxDD `-7.0012`
- `market_context_high->crypto_major_4h` score `1.3681` n `127` status `ready` deltaP `15.8872` edge `0.1799` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0754` n `127` status `ready` deltaP `12.5041` edge `0.0462` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `1.0102` n `127` status `ready` deltaP `10.0201` edge `0.1291` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.919` n `126` status `ready` deltaP `26.7274` edge `0.0484` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.5531` n `127` status `ready` deltaP `8.3043` edge `0.0973` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4662` n `127` status `ready` deltaP `8.5651` edge `0.0411` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.365` n `127` status `ready` deltaP `8.4947` edge `0.0168` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2471` n `127` status `ready` deltaP `4.5523` edge `0.0335` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1257` n `127` status `ready` deltaP `6.3122` edge `0.0143` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1872` n `127` status `ready` deltaP `10.6528` edge `0.0508` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.33` n `127` status `ready` deltaP `-0.5036` edge `-0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9277` n `127` status `ready` deltaP `0.3489` edge `0.0207` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.1392` n `127` status `ready` deltaP `3.1124` edge `0.0814` maxDD `-1.4332`
- `market_context_high->index_24h` score `-1.1442` n `126` status `ready` deltaP `-5.0573` edge `0.0967` maxDD `-2.1079`
- `market_context_high->fx_4h` score `-1.4118` n `127` status `ready` deltaP `-2.8546` edge `0.0007` maxDD `-1.68`
- `market_context_high->crypto_alt_24h` score `-1.5355` n `127` status `ready` deltaP `15.4601` edge `0.2296` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
