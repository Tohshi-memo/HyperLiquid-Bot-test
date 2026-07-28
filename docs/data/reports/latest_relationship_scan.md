# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T11:52:36.358911+00:00`
- Price records: `672`
- Market context records: `8193`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8468.0319` n `43` status `ready` deltaP `36.9792` edge `705.4228` maxDD `0.0`
- `market_context_high->equity_24h` score `20.6751` n `44` status `ready` deltaP `43.1029` edge `1.5266` maxDD `-4.9489`
- `market_context_high->equity_4h` score `11.2021` n `45` status `ready` deltaP `45.6437` edge `0.6335` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.9093` n `44` status `ready` deltaP `45.4861` edge `0.4392` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.0731` n `50` status `ready` deltaP `29.8659` edge `0.503` maxDD `-1.3479`
- `market_context_high->crypto_alt_24h` score `5.7804` n `44` status `ready` deltaP `14.0625` edge `0.868` maxDD `-10.3206`
- `market_context_high->index_4h` score `4.3548` n `45` status `ready` deltaP `38.6077` edge `0.1098` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.8963` n `45` status `ready` deltaP `37.7574` edge `0.0908` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.713` n `45` status `ready` deltaP `19.165` edge `0.1963` maxDD `-0.1718`
- `news_risk_high->crypto_major_4h` score `3.1081` n `50` status `ready` deltaP `16.5732` edge `0.3511` maxDD `-2.382`
- `news_risk_high->equity_1h` score `2.9669` n `54` status `ready` deltaP `22.128` edge `0.1306` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.9177` n `50` status `ready` deltaP `25.2744` edge `0.0937` maxDD `-0.191`
- `market_context_high->crypto_major_24h` score `2.7907` n `44` status `ready` deltaP `13.5417` edge `0.666` maxDD `-24.5466`
- `market_context_high->index_24h` score `2.3556` n `44` status `ready` deltaP `20.7071` edge `0.2302` maxDD `-1.2995`
- `news_risk_high->crypto_major_1h` score `2.0057` n `54` status `ready` deltaP `13.7503` edge `0.1152` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8698` n `54` status `ready` deltaP `15.153` edge `0.0982` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.4753` n `44` status `ready` deltaP `28.346` edge `0.065` maxDD `-0.5196`
- `news_risk_high->crypto_alt_4h` score `1.405` n `50` status `ready` deltaP `16.7256` edge `0.2078` maxDD `-5.8012`
- `market_context_high->index_1h` score `1.3767` n `45` status `ready` deltaP `24.3812` edge `0.0278` maxDD `-0.1069`
- `news_risk_high->metal_4h` score `1.3406` n `50` status `ready` deltaP `12.6463` edge `0.0742` maxDD `-0.7433`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
