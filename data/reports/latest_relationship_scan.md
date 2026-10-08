# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T05:07:28.111524+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.8404` n `90` status `ready` deltaP `-3.2876` edge `3.3125` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1009` n `62` status `ready` deltaP `39.1197` edge `0.6846` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.249` n `62` status `ready` deltaP `23.3245` edge `0.583` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.6585` n `62` status `ready` deltaP `16.8645` edge `0.4524` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.9848` n `62` status `ready` deltaP `36.2694` edge `0.1736` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.583` n `90` status `ready` deltaP `11.3471` edge `0.8093` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.1102` n `62` status `ready` deltaP `33.763` edge `0.0603` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.5961` n `90` status `ready` deltaP `17.1842` edge `0.1982` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.5379` n `62` status `ready` deltaP `10.4742` edge `0.1772` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4944` n `62` status `ready` deltaP `18.94` edge `0.1414` maxDD `-2.7837`
- `market_context_high->equity_24h` score `2.1539` n `90` status `ready` deltaP `14.4272` edge `0.1262` maxDD `-1.0977`
- `news_risk_high->index_1h` score `2.0128` n `62` status `ready` deltaP `25.1739` edge `0.0149` maxDD `-0.1997`
- `news_risk_high->unknown_4h` score `1.62` n `62` status `ready` deltaP `-6.2626` edge `0.3013` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4478` n `62` status `ready` deltaP `21.0144` edge `0.0871` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2385` n `90` status `ready` deltaP `21.5371` edge `0.1637` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.2282` n `62` status `ready` deltaP `3.6073` edge `0.1302` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0257` n `90` status `ready` deltaP `21.2785` edge `0.0183` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6867` n `90` status `ready` deltaP `11.6467` edge `0.0038` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.2026` n `90` status `ready` deltaP `7.5418` edge `0.5695` maxDD `-34.5048`
- `market_context_high->crypto_major_1h` score `0.1846` n `90` status `ready` deltaP `10.4025` edge `0.0432` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
