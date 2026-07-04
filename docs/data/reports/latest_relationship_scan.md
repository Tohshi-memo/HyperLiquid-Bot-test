# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T11:07:25.314446+00:00`
- Price records: `672`
- Market context records: `5656`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.3774` n `187` status `ready` deltaP `15.1515` edge `0.605` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8536` n `237` status `ready` deltaP `11.157` edge `0.226` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.5159` n `237` status `ready` deltaP `7.8387` edge `0.1546` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.4503` n `187` status `ready` deltaP `18.2199` edge `0.0556` maxDD `-2.1631`
- `market_context_high->crypto_alt_4h` score `0.0689` n `237` status `ready` deltaP `6.9839` edge `0.1441` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2822` n `247` status `ready` deltaP `1.5667` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3874` n `247` status `ready` deltaP `5.3565` edge `0.0327` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5566` n `247` status `ready` deltaP `-0.5461` edge `-0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6909` n `247` status `ready` deltaP `1.1073` edge `0.0312` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.8556` n `247` status `ready` deltaP `2.5873` edge `0.036` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.9073` n `247` status `ready` deltaP `0.6958` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9272` n `247` status `ready` deltaP `0.6412` edge `0.0053` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2511` n `237` status `ready` deltaP `2.4377` edge `0.0067` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0355` n `237` status `ready` deltaP `-1.689` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3668` n `187` status `ready` deltaP `8.8866` edge `0.036` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0686` n `237` status `ready` deltaP `-14.9789` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8009` n `237` status `ready` deltaP `-2.1875` edge `-0.0346` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.6178` n `187` status `ready` deltaP `3.9912` edge `0.0426` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4285` n `187` status `ready` deltaP `-13.7682` edge `-0.2527` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.7011` n `187` status `ready` deltaP `-14.2547` edge `-0.1025` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
