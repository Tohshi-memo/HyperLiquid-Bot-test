# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T06:37:28.825506+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3225.1729` n `31` status `ready` deltaP `1.6322` edge `268.7711` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.1582` n `31` status `ready` deltaP `3.7864` edge `265.2436` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.0326` n `31` status `ready` deltaP `31.5972` edge `1.6254` maxDD `0.0`
- `news_risk_high->equity_24h` score `19.7817` n `31` status `ready` deltaP `31.0764` edge `1.4413` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.6915` n `31` status `ready` deltaP `30.7292` edge `1.1861` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.0944` n `31` status `ready` deltaP `22.9494` edge `0.6919` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.0162` n `31` status `ready` deltaP `32.3466` edge `0.4171` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.819` n `31` status `ready` deltaP `15.8635` edge `0.782` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.5701` n `31` status `ready` deltaP `19.0133` edge `0.3649` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6605` n `31` status `ready` deltaP `38.7601` edge `0.1428` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.5279` n `31` status `ready` deltaP `32.6389` edge `0.0764` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6734` n `31` status `ready` deltaP `30.9747` edge `0.0423` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5813` n `31` status `ready` deltaP `15.9455` edge `0.1275` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3715` n `31` status `ready` deltaP `28.6991` edge `0.0148` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0706` n `31` status `ready` deltaP `6.7172` edge `0.2668` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8372` n `31` status `ready` deltaP `9.4118` edge `0.2085` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1543` n `31` status `ready` deltaP `25.0917` edge `0.0086` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.449` n `31` status `ready` deltaP `12.5098` edge `0.0299` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0752` n `31` status `ready` deltaP `5.9304` edge `-0.0094` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6563` n `31` status `ready` deltaP `-4.9063` edge `0.0042` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
