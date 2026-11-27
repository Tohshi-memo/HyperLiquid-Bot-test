# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T08:22:26.285269+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3420`

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

- `news_risk_high->unknown_1h` score `3224.7613` n `31` status `ready` deltaP `1.6322` edge `268.7368` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3182.7154` n `31` status `ready` deltaP `3.7864` edge `265.2067` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.5458` n `31` status `ready` deltaP `30.3819` edge `1.5096` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.4341` n `31` status `ready` deltaP `29.8611` edge `1.3371` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4363` n `31` status `ready` deltaP `29.5139` edge `1.0896` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.8878` n `31` status `ready` deltaP `21.8823` edge `0.6818` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.7137` n `31` status `ready` deltaP `31.2795` edge `0.399` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.6466` n `31` status `ready` deltaP `14.7964` edge `0.767` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.2473` n `31` status `ready` deltaP `17.798` edge `0.3461` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.3095` n `31` status `ready` deltaP `31.4236` edge `0.0663` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.6748` n `31` status `ready` deltaP `16.5443` edge `0.1313` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.6126` n `31` status `ready` deltaP `30.3649` edge `0.0413` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4278` n `31` status `ready` deltaP `29.2979` edge `0.0155` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.055` n `31` status `ready` deltaP `6.5675` edge `0.2658` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8715` n `31` status `ready` deltaP `9.8609` edge `0.2099` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1613` n `31` status `ready` deltaP `25.0917` edge `0.0095` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4271` n `31` status `ready` deltaP `12.3574` edge `0.0281` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.1201` n `31` status `ready` deltaP `5.3206` edge `-0.0111` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6971` n `31` status `ready` deltaP `-5.2057` edge `0.0028` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
