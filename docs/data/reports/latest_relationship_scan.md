# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T22:22:30.545606+00:00`
- Price records: `672`
- Market context records: `5710`
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

- `market_context_high->crypto_major_4h` score `1.824` n `267` status `ready` deltaP `11.3444` edge `0.2135` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0323` n `217` status `ready` deltaP `16.9107` edge `0.5275` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.7` n `267` status `ready` deltaP `8.7661` edge `0.1608` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1611` n `267` status `ready` deltaP `6.6582` edge `0.1329` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2283` n `279` status `ready` deltaP `2.6882` edge `0.0009` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.3567` n `279` status `ready` deltaP `3.9405` edge `0.0396` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4275` n `279` status `ready` deltaP `1.967` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5179` n `279` status `ready` deltaP `2.2031` edge `0.0365` maxDD `-3.8812`
- `market_context_high->equity_1h` score `-0.5545` n `279` status `ready` deltaP `3.9277` edge `0.0283` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6301` n `279` status `ready` deltaP `0.293` edge `0.0041` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1095` n `279` status `ready` deltaP `-1.1912` edge `-0.0038` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.1261` n `217` status `ready` deltaP `10.7287` edge `0.0417` maxDD `-3.6079`
- `market_context_high->index_4h` score `-1.2334` n `267` status `ready` deltaP `-0.0308` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.283` n `267` status `ready` deltaP `2.0599` edge `0.0055` maxDD `-1.3643`
- `market_context_high->metal_4h` score `-2.6349` n `267` status `ready` deltaP `-7.5215` edge `-0.0501` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8745` n `217` status `ready` deltaP `2.181` edge `0.0314` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.9031` n `267` status `ready` deltaP `-4.2757` edge `-0.0292` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5166` n `217` status `ready` deltaP `5.866` edge `0.0302` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.9236` n `217` status `ready` deltaP `-7.1148` edge `-0.2408` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.0669` n `217` status `ready` deltaP `-10.9175` edge `-0.0719` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
