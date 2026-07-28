# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T16:48:11.228634+00:00`
- Price records: `672`
- Market context records: `8215`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `7957.8987` n `43` status `ready` deltaP `36.9792` edge `662.9117` maxDD `0.0`
- `market_context_high->equity_24h` score `21.4302` n `30` status `ready` deltaP `37.9166` edge `1.6241` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `18.2905` n `30` status `ready` deltaP `36.875` edge `1.3678` maxDD `-4.8208`
- `market_context_high->crypto_alt_24h` score `17.0449` n `30` status `ready` deltaP `37.3958` edge `1.2381` maxDD `-3.0264`
- `market_context_high->equity_4h` score `8.9487` n `30` status `ready` deltaP `47.5813` edge `0.4328` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.0656` n `30` status `ready` deltaP `45.625` edge `0.3781` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.4236` n `54` status `ready` deltaP `26.8405` edge `0.4994` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.8185` n `30` status `ready` deltaP `29.8679` edge `0.387` maxDD `-0.433`
- `market_context_high->index_24h` score `5.8475` n `30` status `ready` deltaP `37.743` edge `0.275` maxDD `-0.8132`
- `market_context_high->crypto_alt_4h` score `5.0134` n `30` status `ready` deltaP `23.6585` edge `0.2803` maxDD `-0.6195`
- `market_context_high->metal_4h` score `3.8795` n `30` status `ready` deltaP `37.8659` edge `0.0839` maxDD `-0.0438`
- `market_context_high->index_4h` score `3.6145` n `30` status `ready` deltaP `36.4939` edge `0.0622` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.1876` n `54` status `ready` deltaP `23.0262` edge `0.143` maxDD `-1.1366`
- `market_context_high->fx_24h` score `2.7336` n `30` status `ready` deltaP `45.3819` edge `0.081` maxDD `-0.3134`
- `news_risk_high->index_4h` score `2.6749` n `54` status `ready` deltaP `22.4198` edge `0.0925` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.4991` n `54` status `ready` deltaP `12.4605` edge `0.3067` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.8378` n `54` status `ready` deltaP `12.8521` edge `0.1072` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.7787` n `54` status `ready` deltaP `14.7039` edge `0.0936` maxDD `-1.1388`
- `market_context_high->equity_1h` score `1.7524` n `30` status `ready` deltaP `8.9521` edge `0.101` maxDD `-0.1718`
- `market_context_high->crypto_major_1h` score `1.4086` n `30` status `ready` deltaP `13.5928` edge `0.0463` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
