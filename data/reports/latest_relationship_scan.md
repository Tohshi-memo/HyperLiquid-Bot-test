# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T03:52:29.204104+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.1647` n `65` status `ready` deltaP `31.9418` edge `0.5711` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `6.2801` n `89` status `ready` deltaP `16.1493` edge `0.5266` maxDD `-5.2072`
- `news_risk_high->crypto_alt_4h` score `5.6108` n `65` status `ready` deltaP `19.4817` edge `0.4721` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.6056` n `65` status `ready` deltaP `11.0283` edge `0.2369` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.252` n `65` status `ready` deltaP `22.6804` edge `0.1198` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5512` n `65` status `ready` deltaP `28.5601` edge `0.0484` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4161` n `65` status `ready` deltaP `9.4173` edge `0.1741` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.0553` n `117` status `ready` deltaP `11.429` edge `0.1915` maxDD `-4.047`
- `news_risk_high->index_1h` score `1.9967` n `65` status `ready` deltaP `24.8687` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8645` n `65` status `ready` deltaP `16.7659` edge `0.1034` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.7368` n `65` status `ready` deltaP `16.4869` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3681` n `117` status `ready` deltaP `24.686` edge `0.0251` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.3097` n `117` status `ready` deltaP `17.2113` edge `0.0644` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1552` n `65` status `ready` deltaP `3.9705` edge `0.1217` maxDD `-2.4854`
- `market_context_high->crypto_alt_24h` score `1.0483` n `89` status `ready` deltaP `16.1087` edge `0.17` maxDD `-11.5358`
- `market_context_high->fx_1h` score `0.9695` n `117` status `ready` deltaP `15.3872` edge `0.0066` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7094` n `117` status `ready` deltaP `11.756` edge `0.0204` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.484` n `89` status `ready` deltaP `20.2575` edge `0.0645` maxDD `-5.6663`
- `news_risk_high->commodity_24h` score `0.0907` n `65` status `ready` deltaP `24.7132` edge `0.05` maxDD `-10.9169`
- `news_risk_high->metal_1h` score `0.0829` n `65` status `ready` deltaP `5.9166` edge `0.0093` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
