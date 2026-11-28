# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T19:22:34.477532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7506`

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

- `news_risk_high->unknown_4h` score `3266.7625` n `31` status `ready` deltaP `3.0242` edge `272.2157` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `2757.2976` n `31` status `ready` deltaP `2.231` edge `229.7775` maxDD `-0.7395`
- `news_risk_high->crypto_major_24h` score `25.5138` n `31` status `ready` deltaP `39.7569` edge `1.8611` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.8386` n `31` status `ready` deltaP `37.8472` edge `1.4009` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.3312` n `31` status `ready` deltaP `30.0347` edge `0.9107` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.5491` n `31` status `ready` deltaP `24.7787` edge `0.7176` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.0342` n `31` status `ready` deltaP `33.871` edge `0.3251` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9972` n `31` status `ready` deltaP `19.0647` edge `0.7835` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2004` n `31` status `ready` deltaP `43.274` edge `0.1577` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8679` n `31` status `ready` deltaP `16.7563` edge `0.2381` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.7557` n `31` status `ready` deltaP `33.4137` edge `0.0329` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.5947` n `31` status `ready` deltaP `27.6042` edge `0.0322` maxDD `0.0`
- `news_risk_high->index_1h` score `2.4062` n `31` status `ready` deltaP `29.4476` edge `0.0127` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.3282` n `31` status `ready` deltaP `15.6461` edge `0.1084` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.1391` n `31` status `ready` deltaP `7.6154` edge `0.2696` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9759` n `31` status `ready` deltaP `10.7591` edge `0.2173` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1792` n `31` status `ready` deltaP `25.3911` edge `0.0098` maxDD `-0.2315`
- `market_context_high->fx_4h` score `0.5986` n `65` status `ready` deltaP `11.9817` edge `0.0096` maxDD `-0.1673`
- `news_risk_high->commodity_4h` score `0.585` n `31` status `ready` deltaP `12.7901` edge `0.0295` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.4983` n `69` status `ready` deltaP `12.6182` edge `0.0019` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
