# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T11:07:38.963653+00:00`
- Price records: `672`
- Market context records: `8190`
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

- `news_risk_high->unknown_24h` score `8544.6051` n `43` status `ready` deltaP `36.9792` edge `711.8039` maxDD `0.0`
- `market_context_high->equity_24h` score `20.3118` n `44` status `ready` deltaP `42.5821` edge `1.4998` maxDD `-4.9489`
- `market_context_high->equity_4h` score `11.0767` n `45` status `ready` deltaP `45.1863` edge `0.6261` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.8076` n `44` status `ready` deltaP `44.9653` edge `0.4342` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.9477` n `50` status `ready` deltaP `29.4085` edge `0.4956` maxDD `-1.3479`
- `market_context_high->crypto_alt_24h` score `5.6509` n `44` status `ready` deltaP `14.0625` edge `0.8514` maxDD `-10.3206`
- `market_context_high->index_4h` score `4.3063` n `45` status `ready` deltaP `38.1504` edge `0.1088` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.8721` n `45` status `ready` deltaP `37.605` edge `0.0898` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.6843` n `45` status `ready` deltaP `19.0153` edge `0.1949` maxDD `-0.1718`
- `news_risk_high->crypto_major_4h` score `3.079` n `50` status `ready` deltaP `16.2683` edge `0.3494` maxDD `-2.382`
- `news_risk_high->equity_1h` score `2.9382` n `54` status `ready` deltaP `21.9783` edge `0.1292` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.8691` n `50` status `ready` deltaP `24.8171` edge `0.0927` maxDD `-0.191`
- `market_context_high->crypto_major_24h` score `2.6815` n `44` status `ready` deltaP `13.5417` edge `0.652` maxDD `-24.5466`
- `market_context_high->index_24h` score `2.319` n `44` status `ready` deltaP `20.7071` edge `0.2255` maxDD `-1.2995`
- `news_risk_high->crypto_major_1h` score `1.9685` n `54` status `ready` deltaP `13.4509` edge `0.1141` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8387` n `54` status `ready` deltaP `14.8536` edge `0.0976` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.4691` n `44` status `ready` deltaP `28.346` edge `0.0642` maxDD `-0.5196`
- `news_risk_high->crypto_alt_4h` score `1.4018` n `50` status `ready` deltaP `16.7256` edge `0.2074` maxDD `-5.8012`
- `market_context_high->index_1h` score `1.3767` n `45` status `ready` deltaP `24.3812` edge `0.0278` maxDD `-0.1069`
- `news_risk_high->metal_4h` score `1.3164` n `50` status `ready` deltaP `12.4939` edge `0.0732` maxDD `-0.7433`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
