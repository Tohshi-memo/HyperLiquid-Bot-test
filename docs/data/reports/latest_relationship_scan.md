# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T23:52:16.372614+00:00`
- Price records: `672`
- Market context records: `1790`
- Flow alert records: `7047`
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

- `market_context_high->metal_24h` score `7.3132` n `190` status `ready` deltaP `28.6549` edge `0.661` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.2506` n `30` status `ready` deltaP `28.3435` edge `0.3974` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.7996` n `194` status `ready` deltaP `21.7076` edge `0.5152` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.3249` n `194` status `ready` deltaP `22.6302` edge `0.4501` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.7213` n `194` status `ready` deltaP `15.7546` edge `0.4322` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.217` n `30` status `ready` deltaP `24.7206` edge `0.135` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0189` n `194` status `ready` deltaP `16.4744` edge `0.2512` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.7561` n `190` status `ready` deltaP `14.2069` edge `0.2578` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.5313` n `190` status `ready` deltaP `15.6232` edge `0.5133` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.9067` n `194` status `ready` deltaP `12.4591` edge `0.1014` maxDD `-3.7119`
- `market_context_high->unknown_24h` score `0.8759` n `190` status `ready` deltaP `12.3794` edge `0.5225` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.8087` n `30` status `ready` deltaP `20.2643` edge `-0.0042` maxDD `-0.1774`
- `news_risk_high->unknown_4h` score `0.5282` n `30` status `ready` deltaP `11.0467` edge `0.0664` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3553` n `199` status `ready` deltaP `6.9547` edge `0.0944` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.0361` n `199` status `ready` deltaP `4.3887` edge `0.0811` maxDD `-3.9211`
- `market_context_high->equity_1h` score `-0.0009` n `199` status `ready` deltaP `4.8266` edge `0.0486` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2793` n `199` status `ready` deltaP `3.2551` edge `0.0182` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.3871` n `190` status `ready` deltaP `8.9016` edge `0.0133` maxDD `-1.3925`
- `market_context_high->metal_4h` score `-0.3993` n `194` status `ready` deltaP `12.2548` edge `0.1363` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4294` n `30` status `ready` deltaP `17.006` edge `-0.1212` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
