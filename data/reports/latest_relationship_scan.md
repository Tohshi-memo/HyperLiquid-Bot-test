# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T02:22:37.951015+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3899`

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

- `market_context_high->unknown_1h` score `32939.3365` n `44` status `ready` deltaP `1.1159` edge `2744.9467` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `11050.7451` n `44` status `ready` deltaP `2.0094` edge `920.8959` maxDD `-0.7765`
- `news_risk_high->unknown_4h` score `2393.3513` n `31` status `ready` deltaP `3.3291` edge `199.4294` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `889.8733` n `31` status `ready` deltaP `1.4825` edge `74.1638` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `66.5737` n `31` status `ready` deltaP `6.0764` edge `5.5073` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.0819` n `31` status `ready` deltaP `50.1736` edge `3.339` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.0817` n `31` status `ready` deltaP `51.0417` edge `3.0832` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.991` n `31` status `ready` deltaP `50.3472` edge `2.6636` maxDD `0.0`
- `news_risk_high->metal_24h` score `10.9323` n `31` status `ready` deltaP `36.7216` edge `0.6937` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8451` n `31` status `ready` deltaP `26.6079` edge `0.8134` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.1761` n `31` status `ready` deltaP `37.2247` edge `0.6479` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.1946` n `31` status `ready` deltaP `51.5625` edge `0.2558` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.739` n `31` status `ready` deltaP `17.2354` edge `0.8908` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3028` n `31` status `ready` deltaP `45.1837` edge `0.1535` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5503` n `31` status `ready` deltaP `19.688` edge `0.1833` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3136` n `31` status `ready` deltaP `36.1576` edge `0.0611` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6375` n `31` status `ready` deltaP `31.3937` edge `0.019` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.532` n `44` status `ready` deltaP `31.1946` edge `0.0315` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.3698` n `31` status `ready` deltaP `9.5615` edge `0.2862` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1731` n `31` status `ready` deltaP `12.2561` edge `0.2326` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
