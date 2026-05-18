# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T15:37:20.614467+00:00`
- Price records: `672`
- Market context records: `1130`
- Flow alert records: `5158`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8733`

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

- `market_context_high->crypto_major_24h` score `19.6218` n `150` status `ready` deltaP `41.8959` edge `1.4022` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `9.4333` n `150` status `ready` deltaP `18.2569` edge `0.7878` maxDD `-9.5387`
- `market_context_high->equity_24h` score `7.3485` n `150` status `ready` deltaP `17.7361` edge `0.5438` maxDD `-3.6396`
- `market_context_high->index_24h` score `5.7154` n `150` status `ready` deltaP `16.3472` edge `0.3981` maxDD `-2.1308`
- `market_context_high->metal_24h` score `5.5895` n `150` status `ready` deltaP `-1.8889` edge `0.6451` maxDD `-6.3373`
- `market_context_high->equity_4h` score `1.7778` n `168` status `ready` deltaP `10.032` edge `0.1476` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.7844` n `168` status `ready` deltaP `7.3751` edge `0.0845` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4486` n `168` status `ready` deltaP `7.0466` edge `0.0221` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.34` n `168` status `ready` deltaP `2.7302` edge `0.0479` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1603` n `168` status `ready` deltaP `8.6149` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0921` n `168` status `ready` deltaP `7.1322` edge `0.0367` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0135` n `168` status `ready` deltaP `8.1518` edge `0.1395` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.246` n `168` status `ready` deltaP `6.651` edge `-0.0038` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2514` n `168` status `ready` deltaP `2.9441` edge `0.0437` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7199` n `168` status `ready` deltaP `0.9364` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7435` n `168` status `ready` deltaP `-1.775` edge `-0.0027` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0708` n `168` status `ready` deltaP `5.3862` edge `0.1233` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.5154` n `168` status `ready` deltaP `5.9378` edge `-0.0538` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1092` n `168` status `ready` deltaP `-11.2732` edge `-0.0067` maxDD `-13.0076`
- `market_context_high->unknown_24h` score `-3.1509` n `150` status `ready` deltaP `2.3681` edge `-0.0054` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
