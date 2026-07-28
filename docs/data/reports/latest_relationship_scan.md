# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T11:22:28.588911+00:00`
- Price records: `672`
- Market context records: `8191`
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

- `news_risk_high->unknown_24h` score `8519.0799` n `43` status `ready` deltaP `36.9792` edge `709.6768` maxDD `0.0`
- `market_context_high->equity_24h` score `20.4313` n `44` status `ready` deltaP `42.7557` edge `1.5086` maxDD `-4.9489`
- `market_context_high->equity_4h` score `11.1153` n `45` status `ready` deltaP `45.3388` edge `0.6283` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.8407` n `44` status `ready` deltaP `45.1389` edge `0.4358` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.9863` n `50` status `ready` deltaP `29.561` edge `0.4978` maxDD `-1.3479`
- `market_context_high->crypto_alt_24h` score `5.6915` n `44` status `ready` deltaP `14.0625` edge `0.8566` maxDD `-10.3206`
- `market_context_high->index_4h` score `4.3232` n `45` status `ready` deltaP `38.3028` edge `0.1092` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.8757` n `45` status `ready` deltaP `37.605` edge `0.0901` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.6867` n `45` status `ready` deltaP `19.0153` edge `0.1951` maxDD `-0.1718`
- `news_risk_high->crypto_major_4h` score `3.0821` n `50` status `ready` deltaP `16.2683` edge `0.3498` maxDD `-2.382`
- `news_risk_high->equity_1h` score `2.9406` n `54` status `ready` deltaP `21.9783` edge `0.1294` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.8861` n `50` status `ready` deltaP `24.9695` edge `0.0931` maxDD `-0.191`
- `market_context_high->crypto_major_24h` score `2.715` n `44` status `ready` deltaP `13.5417` edge `0.6563` maxDD `-24.5466`
- `market_context_high->index_24h` score `2.3307` n `44` status `ready` deltaP `20.7071` edge `0.227` maxDD `-1.2995`
- `news_risk_high->crypto_major_1h` score `1.9685` n `54` status `ready` deltaP `13.4509` edge `0.1141` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8387` n `54` status `ready` deltaP `14.8536` edge `0.0976` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.4714` n `44` status `ready` deltaP `28.346` edge `0.0645` maxDD `-0.5196`
- `news_risk_high->crypto_alt_4h` score `1.4026` n `50` status `ready` deltaP `16.7256` edge `0.2075` maxDD `-5.8012`
- `market_context_high->index_1h` score `1.3767` n `45` status `ready` deltaP `24.3812` edge `0.0278` maxDD `-0.1069`
- `news_risk_high->metal_4h` score `1.32` n `50` status `ready` deltaP `12.4939` edge `0.0735` maxDD `-0.7433`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
