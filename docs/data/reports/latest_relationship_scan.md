# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T22:22:16.127269+00:00`
- Price records: `672`
- Market context records: `1783`
- Flow alert records: `7028`
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

- `market_context_high->metal_24h` score `7.128` n `184` status `ready` deltaP `28.1401` edge `0.649` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `5.995` n `30` status `ready` deltaP `27.4289` edge `0.3822` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.8884` n `194` status `ready` deltaP `21.7076` edge `0.5226` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.4992` n `194` status `ready` deltaP `22.935` edge `0.4626` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.6886` n `194` status `ready` deltaP `15.4497` edge `0.4315` maxDD `-11.1695`
- `market_context_high->index_24h` score `3.1914` n `184` status `ready` deltaP `16.093` edge `0.2815` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.0923` n `30` status `ready` deltaP `23.9721` edge `0.1296` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0635` n `194` status `ready` deltaP `16.6269` edge `0.2539` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.0099` n `184` status `ready` deltaP `16.1156` edge `0.5499` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.573` n `184` status `ready` deltaP `13.4134` edge `0.5737` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9379` n `194` status `ready` deltaP `12.4591` edge `0.104` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8071` n `30` status `ready` deltaP `20.2643` edge `-0.0044` maxDD `-0.1774`
- `market_context_high->crypto_alt_1h` score `0.6095` n `197` status `ready` deltaP `7.8027` edge `0.109` maxDD `-4.8183`
- `news_risk_high->unknown_4h` score `0.5069` n `30` status `ready` deltaP `10.7418` edge `0.0657` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `0.1941` n `197` status `ready` deltaP `4.8482` edge `0.0912` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0824` n `197` status `ready` deltaP `5.1924` edge `0.0531` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1548` n `197` status `ready` deltaP `4.3011` edge `0.0216` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1949` n `194` status `ready` deltaP `13.1695` edge `0.1564` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4271` n `30` status `ready` deltaP `17.1557` edge `-0.1219` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.4343` n `184` status `ready` deltaP `8.5069` edge `0.012` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
