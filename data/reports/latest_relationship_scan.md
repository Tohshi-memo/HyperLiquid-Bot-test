# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T15:07:32.470818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8012`

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

- `market_context_high->crypto_major_24h` score `10.8296` n `81` status `ready` deltaP `29.8032` edge `0.7174` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.5058` n `65` status `ready` deltaP `33.1614` edge `0.5914` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `5.981` n `81` status `ready` deltaP `25.8874` edge `0.3878` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.877` n `65` status `ready` deltaP `20.2439` edge `0.4892` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4482` n `65` status `ready` deltaP `24.6528` edge `0.123` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1061` n `65` status `ready` deltaP `9.8184` edge `0.2034` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8771` n `65` status `ready` deltaP `31.9137` edge `0.0532` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.6096` n `119` status `ready` deltaP `13.1226` edge `0.2264` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4473` n `65` status `ready` deltaP `9.567` edge `0.1757` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4148` n `65` status `ready` deltaP `20.272` edge `0.1271` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9824` n `65` status `ready` deltaP `24.719` edge `0.0154` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8426` n `65` status `ready` deltaP `17.554` edge `0.0781` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5088` n `119` status `ready` deltaP `26.2951` edge `0.0261` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1157` n `65` status `ready` deltaP `3.5214` edge `0.1214` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9513` n `120` status `ready` deltaP `15.1746` edge `0.0065` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.91` n `81` status `ready` deltaP `13.5031` edge `-0.0081` maxDD `-0.1536`
- `market_context_high->metal_24h` score `0.8217` n `81` status `ready` deltaP `25.7909` edge `0.0725` maxDD `-5.7943`
- `market_context_high->commodity_4h` score `0.7571` n `119` status `ready` deltaP `12.8689` edge `0.0473` maxDD `-1.6002`
- `news_risk_high->commodity_24h` score `0.4037` n `65` status `ready` deltaP `24.9119` edge `0.0888` maxDD `-10.9169`
- `market_context_high->commodity_1h` score `0.252` n `120` status `ready` deltaP `10.1746` edge `0.0129` maxDD `-1.207`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
