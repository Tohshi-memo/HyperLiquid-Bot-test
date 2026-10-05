# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T23:07:32.997481+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7928`

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

- `market_context_high->crypto_major_24h` score `10.4694` n `78` status `ready` deltaP `27.161` edge `0.705` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2263` n `65` status `ready` deltaP `32.1869` edge `0.5746` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.7097` n `65` status `ready` deltaP `19.7281` edge `0.4787` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5153` n `78` status `ready` deltaP `25.8261` edge `0.3494` maxDD `-2.9571`
- `news_risk_high->equity_24h` score `3.2669` n `65` status `ready` deltaP `9.6538` edge `0.2179` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.24` n `65` status `ready` deltaP `22.6804` edge `0.1188` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6252` n `65` status `ready` deltaP `29.261` edge `0.0499` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.3598` n `65` status `ready` deltaP `8.8185` edge `0.1734` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.1169` n `117` status `ready` deltaP `11.6741` edge `0.195` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0625` n `65` status `ready` deltaP `17.518` edge `0.1161` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.95` n `65` status `ready` deltaP `24.2699` edge `0.0157` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7509` n `65` status `ready` deltaP `16.6628` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5211` n `117` status `ready` deltaP `26.4338` edge `0.0262` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2549` n `117` status `ready` deltaP `16.7222` edge `0.0631` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.0558` n `65` status `ready` deltaP `3.0723` edge `0.1194` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9959` n `117` status `ready` deltaP `15.6866` edge `0.0068` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7849` n `117` status `ready` deltaP `12.6542` edge `0.0207` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.732` n `78` status `ready` deltaP `24.5308` edge `0.0678` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.666` n `78` status `ready` deltaP `13.2435` edge `-0.0267` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3191` n `65` status `ready` deltaP `25.4005` edge `0.0747` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
