# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T14:22:36.753510+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8475`

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

- `market_context_high->unknown_4h` score `40.6305` n `90` status `ready` deltaP `-2.6456` edge `3.4574` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.245` n `49` status `ready` deltaP `42.6829` edge `0.8192` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.0266` n `49` status `ready` deltaP `43.9367` edge `0.7994` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `6.9703` n `49` status `ready` deltaP `21.1977` edge `0.4495` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.6937` n `90` status `ready` deltaP `17.7374` edge `1.0373` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.6026` n `49` status `ready` deltaP `41.2781` edge `0.1917` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.0484` n `49` status `ready` deltaP `29.794` edge `0.2426` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.3355` n `49` status `ready` deltaP `43.6909` edge `0.0745` maxDD `-0.025`
- `market_context_high->equity_24h` score `4.3019` n `90` status `ready` deltaP `20.4721` edge `0.2649` maxDD `-1.0977`
- `news_risk_high->commodity_24h` score `3.4585` n `49` status `ready` deltaP `35.1239` edge `0.0625` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `2.9873` n `49` status `ready` deltaP `12.3121` edge `0.2024` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.8992` n `90` status `ready` deltaP `18.0183` edge `0.2179` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.4893` n `49` status `ready` deltaP `6.9382` edge `0.1929` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.417` n `49` status `ready` deltaP `29.986` edge `0.0155` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.3993` n `90` status `ready` deltaP `23.2642` edge `0.1728` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1896` n `49` status `ready` deltaP `18.4482` edge `0.0711` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `0.8427` n `90` status `ready` deltaP `9.787` edge `0.6366` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.6459` n `90` status `ready` deltaP `17.1002` edge `0.0145` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.559` n `91` status `ready` deltaP `10.1402` edge `0.0032` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2303` n `91` status `ready` deltaP `10.7423` edge `0.0468` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
