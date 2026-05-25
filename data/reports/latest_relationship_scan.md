# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T00:22:18.994244+00:00`
- Price records: `672`
- Market context records: `1792`
- Flow alert records: `7053`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8882`

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

- `market_context_high->metal_24h` score `7.3731` n `192` status `ready` deltaP `28.8194` edge `0.6649` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.3194` n `30` status `ready` deltaP `28.6484` edge `0.4011` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.7742` n `194` status `ready` deltaP `21.5551` edge `0.5141` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.2621` n `194` status `ready` deltaP `22.3253` edge `0.4469` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.6766` n `194` status `ready` deltaP `15.4497` edge `0.4305` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.2254` n `30` status `ready` deltaP `24.7206` edge `0.1357` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9984` n `194` status `ready` deltaP `16.322` edge `0.2505` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.5906` n `192` status `ready` deltaP `13.3681` edge `0.2496` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.3892` n `192` status `ready` deltaP `15.4514` edge `0.5026` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.9055` n `194` status `ready` deltaP `12.4591` edge `0.1013` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8277` n `30` status `ready` deltaP `20.5691` edge `-0.0038` maxDD `-0.1774`
- `market_context_high->unknown_24h` score `0.5948` n `192` status `ready` deltaP `11.8056` edge `0.5029` maxDD `-35.8966`
- `news_risk_high->unknown_4h` score `0.4991` n `30` status `ready` deltaP `10.7418` edge `0.0647` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3097` n `199` status `ready` deltaP `6.805` edge `0.0916` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.0026` n `199` status `ready` deltaP `4.239` edge `0.0793` maxDD `-3.9211`
- `market_context_high->equity_1h` score `-0.062` n `199` status `ready` deltaP `4.5272` edge `0.0455` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3044` n `199` status `ready` deltaP `3.1054` edge `0.0171` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.4072` n `192` status `ready` deltaP `8.6806` edge `0.0131` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4255` n `30` status `ready` deltaP `17.006` edge `-0.1207` maxDD `-2.1115`
- `market_context_high->metal_4h` score `-0.4697` n `194` status `ready` deltaP `11.95` edge `0.1293` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
