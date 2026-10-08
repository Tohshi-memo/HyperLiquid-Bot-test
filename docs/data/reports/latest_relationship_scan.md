# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T04:07:26.226123+00:00`
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

- `market_context_high->unknown_4h` score `38.7752` n `90` status `ready` deltaP `-3.592` edge `3.3091` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9118` n `62` status `ready` deltaP `38.5108` edge `0.6729` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0263` n `62` status `ready` deltaP `22.7157` edge `0.5685` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.4232` n `62` status `ready` deltaP `16.1736` edge `0.4374` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.8995` n `62` status `ready` deltaP `35.5786` edge `0.1711` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.4137` n `90` status `ready` deltaP `10.6563` edge `0.7922` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.0435` n `62` status `ready` deltaP `33.1541` edge `0.0588` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4683` n `62` status `ready` deltaP `10.1748` edge `0.1734` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.407` n `90` status `ready` deltaP `16.5753` edge `0.1865` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.3353` n `62` status `ready` deltaP `18.3312` edge `0.1322` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9972` n `62` status `ready` deltaP `25.0242` edge `0.0146` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.9186` n `90` status `ready` deltaP `13.7363` edge `0.1112` maxDD `-1.0977`
- `news_risk_high->unknown_4h` score `1.5548` n `62` status `ready` deltaP `-6.567` edge `0.2979` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4486` n `62` status `ready` deltaP `21.0144` edge `0.0872` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2377` n `90` status `ready` deltaP `21.5371` edge `0.1636` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0939` n `62` status `ready` deltaP `3.0085` edge `0.123` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0792` n `90` status `ready` deltaP `21.8873` edge `0.0187` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7118` n `90` status `ready` deltaP `11.9461` edge `0.0039` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1393` n `90` status `ready` deltaP `10.1031` edge `0.0394` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.1269` n `90` status `ready` deltaP `7.1964` edge `0.5621` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
