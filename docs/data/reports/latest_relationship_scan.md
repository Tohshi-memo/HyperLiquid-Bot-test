# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T20:07:28.535751+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1508.6775` n `117` status `ready` deltaP `11.1819` edge `125.6866` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.6935` n `117` status `ready` deltaP `-0.3583` edge `2.4474` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.2562` n `62` status `ready` deltaP `33.5514` edge `0.568` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4114` n `62` status `ready` deltaP `19.7335` edge `0.4538` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.1335` n `62` status `ready` deltaP `22.069` edge `0.114` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.5913` n `62` status `ready` deltaP `7.1691` edge `0.1781` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.5876` n `62` status `ready` deltaP `29.106` edge `0.0478` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.5114` n `117` status `ready` deltaP `13.4108` edge `0.2163` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.9756` n `62` status `ready` deltaP `7.6299` edge `0.1493` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8869` n `62` status `ready` deltaP `23.9763` edge `0.0124` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.5502` n `62` status `ready` deltaP `15.6422` edge `0.0847` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2064` n `62` status `ready` deltaP `17.437` edge `0.08` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9829` n `62` status `ready` deltaP `29.2548` edge `0.0876` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8812` n `117` status `ready` deltaP `19.3507` edge `0.0201` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8154` n `62` status `ready` deltaP `3.1582` edge `0.0988` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7024` n `117` status `ready` deltaP `12.2435` edge `0.0053` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.6402` n `117` status `ready` deltaP `12.6381` edge `0.0391` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.4266` n `117` status `ready` deltaP `9.2111` edge `0.0138` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.2865` n `117` status `ready` deltaP `-1.1791` edge `0.2041` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0708` n `62` status `ready` deltaP `4.6552` edge `0.0049` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
