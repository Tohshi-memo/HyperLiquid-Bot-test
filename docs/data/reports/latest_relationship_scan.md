# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T11:22:29.394533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `22314.438` n `63` status `ready` deltaP `0.5061` edge `1859.5493` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `14951.6126` n `63` status `ready` deltaP `4.7522` edge `1245.9499` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1297.6798` n `31` status `ready` deltaP `3.5783` edge `108.1337` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1118.9938` n `31` status `ready` deltaP `4.701` edge `93.2238` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.6825` n `31` status `ready` deltaP `51.0417` edge `3.4666` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0365` n `31` status `ready` deltaP `48.6111` edge `2.7623` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5996` n `31` status `ready` deltaP `48.7847` edge `2.3914` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.5416` n `31` status `ready` deltaP `51.6521` edge `0.8116` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.4668` n `31` status `ready` deltaP `33.4137` edge `0.6977` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1346` n `31` status `ready` deltaP `21.8823` edge `0.7857` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.1771` n `31` status `ready` deltaP `48.9583` edge `0.2717` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.3922` n `31` status `ready` deltaP `54.2115` edge `0.1841` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1851` n `31` status `ready` deltaP `11.4427` edge `0.8584` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6728` n `31` status `ready` deltaP `18.4904` edge `0.2015` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.3095` n `31` status `ready` deltaP `34.7856` edge `0.0699` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6232` n `31` status `ready` deltaP `30.7949` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3745` n `31` status `ready` deltaP `9.1124` edge `0.2898` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9661` n `31` status `ready` deltaP `7.7651` edge `0.236` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5127` n `31` status `ready` deltaP `28.8342` edge `0.0296` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.446` n `31` status `ready` deltaP `20.1318` edge `0.1069` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
