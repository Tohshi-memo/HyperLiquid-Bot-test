# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T08:52:29.391400+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3998`

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

- `news_risk_high->equity_4h` score `1.3173` n `62` status `ready` deltaP `12.5983` edge `0.1588` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7287` n `62` status `ready` deltaP `13.0802` edge `0.0213` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.296` n `62` status `ready` deltaP `9.235` edge `0.1432` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.1713` n `62` status `ready` deltaP `-1.3553` edge `0.0675` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0621` n `62` status `ready` deltaP `7.4995` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.1041` n `62` status `ready` deltaP `-0.7485` edge `0.0466` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1083` n `62` status `ready` deltaP `3.3079` edge `0.0026` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.212` n `62` status `ready` deltaP `1.9669` edge `0.0043` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5719` n `62` status `ready` deltaP `-4.5731` edge `-0.0071` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9982` n `62` status `ready` deltaP `0.5065` edge `-0.0408` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2429` n `62` status `ready` deltaP `-2.7429` edge `-0.0255` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.3328` n `62` status `ready` deltaP `-3.7716` edge `0.0147` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5967` n `62` status `ready` deltaP `-11.1744` edge `-0.0026` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-2.0422` n `62` status `ready` deltaP `-8.4798` edge `-0.0319` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2709` n `62` status `ready` deltaP `-3.4667` edge `-0.006` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8251` n `62` status `ready` deltaP `-5.774` edge `-0.2623` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5287` n `62` status `ready` deltaP `-31.2795` edge `-0.0117` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.9369` n `62` status `ready` deltaP `20.5197` edge `0.3889` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.575` n `62` status `ready` deltaP `-28.4442` edge `-0.1256` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5663` n `62` status `ready` deltaP `-31.4908` edge `-0.1536` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
