# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T01:22:27.060970+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7932`

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

- `market_context_high->unknown_24h` score `37.4472` n `46` status `ready` deltaP `26.8192` edge `2.9461` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `10.5963` n `74` status `ready` deltaP `11.6719` edge `0.8526` maxDD `-1.4578`
- `market_context_high->crypto_alt_24h` score `10.3186` n `46` status `ready` deltaP `47.9922` edge `0.5573` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.5087` n `46` status `ready` deltaP `40.6929` edge `0.4557` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0385` n `31` status `ready` deltaP `12.192` edge `0.0705` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8602` n `31` status `ready` deltaP `18.7898` edge `0.0062` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.8055` n `74` status `ready` deltaP `11.573` edge `0.0746` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.4344` n `74` status `ready` deltaP `19.6935` edge `0.0104` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.3735` n `86` status `ready` deltaP `10.1657` edge `-0.0018` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.3641` n `86` status `ready` deltaP `6.8619` edge `0.0262` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0615` n `31` status `ready` deltaP `3.5209` edge `0.0347` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.17` n `31` status `ready` deltaP `0.7968` edge `-0.0073` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2173` n `31` status `ready` deltaP `9.943` edge `-0.0301` maxDD `-3.1233`
- `news_risk_high->commodity_4h` score `-0.2332` n `31` status `ready` deltaP `8.8267` edge `-0.0282` maxDD `-1.6728`
- `news_risk_high->index_4h` score `-0.2719` n `31` status `ready` deltaP `-3.57` edge `0.0392` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3214` n `31` status `ready` deltaP `-1.9123` edge `0.0027` maxDD `-0.1588`
- `news_risk_high->unknown_4h` score `-0.5066` n `31` status `ready` deltaP `-1.3621` edge `-0.007` maxDD `-1.5766`
- `market_context_high->metal_1h` score `-0.541` n `86` status `ready` deltaP `-1.5318` edge `-0.0097` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7066` n `86` status `ready` deltaP `1.7721` edge `-0.0173` maxDD `-1.6054`
- `news_risk_high->equity_4h` score `-0.7396` n `31` status `ready` deltaP `-16.7781` edge `0.1198` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
