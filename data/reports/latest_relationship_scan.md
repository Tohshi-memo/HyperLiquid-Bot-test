# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T11:37:19.099951+00:00`
- Price records: `672`
- Market context records: `2240`
- Flow alert records: `8343`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.7892` n `38` status `ready` deltaP `55.6743` edge `1.8368` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.9246` n `38` status `ready` deltaP `45.6323` edge `1.0668` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9901` n `38` status `ready` deltaP `36.6045` edge `1.0366` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.6657` n `131` status `ready` deltaP `34.7259` edge `0.9176` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.4633` n `131` status `ready` deltaP `40.9909` edge `0.735` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.711` n `38` status `ready` deltaP `36.5771` edge `0.588` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `8.6857` n `38` status `ready` deltaP `22.9076` edge `1.0189` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.4073` n `122` status `ready` deltaP `27.9059` edge `0.5976` maxDD `-10.976`
- `market_context_high->unknown_4h` score `6.2554` n `131` status `ready` deltaP `24.5043` edge `0.4033` maxDD `-1.6306`
- `market_context_high->crypto_major_24h` score `5.2251` n `122` status `ready` deltaP `16.9542` edge `0.9798` maxDD `-27.8357`
- `market_context_high->equity_4h` score `4.3453` n `131` status `ready` deltaP `24.3705` edge `0.2507` maxDD `-1.7513`
- `market_context_high->index_4h` score `4.0888` n `131` status `ready` deltaP `30.93` edge `0.1719` maxDD `-0.3228`
- `news_risk_high->commodity_4h` score `3.9255` n `43` status `ready` deltaP `33.2246` edge `0.3489` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4016` n `38` status `ready` deltaP `34.4755` edge `0.0721` maxDD `-0.1442`
- `news_risk_high->index_24h` score `3.0577` n `38` status `ready` deltaP `12.2533` edge `0.215` maxDD `-1.3507`
- `market_context_high->index_24h` score `3.0171` n `122` status `ready` deltaP `12.167` edge `0.224` maxDD `-1.6283`
- `market_context_high->crypto_alt_1h` score `2.7399` n `143` status `ready` deltaP `15.7343` edge `0.2098` maxDD `-4.9097`
- `market_context_high->crypto_major_1h` score `2.6951` n `143` status `ready` deltaP `14.0855` edge `0.1784` maxDD `-1.817`
- `news_risk_high->fx_4h` score `2.1512` n `43` status `ready` deltaP `27.2794` edge `0.0158` maxDD `-0.1382`
- `news_risk_high->commodity_24h` score `1.5895` n `38` status `ready` deltaP `-1.0691` edge `0.2926` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
