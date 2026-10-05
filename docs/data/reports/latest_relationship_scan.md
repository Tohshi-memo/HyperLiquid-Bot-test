# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T23:37:29.850957+00:00`
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

- `market_context_high->crypto_major_24h` score `10.482` n `78` status `ready` deltaP `27.3328` edge `0.7049` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.1781` n `65` status `ready` deltaP `32.0047` edge `0.5718` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6567` n `65` status `ready` deltaP `19.5455` edge `0.4755` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5561` n `78` status `ready` deltaP `25.8261` edge `0.3528` maxDD `-2.9571`
- `news_risk_high->equity_24h` score `3.2873` n `65` status `ready` deltaP `9.6538` edge `0.2196` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2388` n `65` status `ready` deltaP `22.6804` edge `0.1187` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6083` n `65` status `ready` deltaP `29.0793` edge `0.0497` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.3838` n `65` status `ready` deltaP `8.9682` edge `0.1744` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.0687` n `117` status `ready` deltaP `11.4919` edge `0.1922` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0346` n `65` status `ready` deltaP `17.3193` edge `0.1151` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9488` n `65` status `ready` deltaP `24.2699` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7502` n `65` status `ready` deltaP `16.655` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5123` n `117` status `ready` deltaP `26.3093` edge `0.0263` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.257` n `117` status `ready` deltaP `16.7327` edge `0.0632` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.0821` n `65` status `ready` deltaP `3.222` edge `0.1206` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.021` n `117` status `ready` deltaP `15.986` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7837` n `117` status `ready` deltaP `12.6542` edge `0.0206` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7374` n `78` status `ready` deltaP `24.5308` edge `0.0685` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.6864` n `78` status `ready` deltaP `13.2435` edge `-0.025` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3004` n `65` status `ready` deltaP `25.4005` edge `0.0723` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
