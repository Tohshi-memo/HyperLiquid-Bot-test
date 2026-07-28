# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T07:22:27.292420+00:00`
- Price records: `672`
- Market context records: `8173`
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

- `news_risk_high->unknown_24h` score `8829.5206` n `42` status `ready` deltaP `37.1528` edge `735.5457` maxDD `0.0`
- `market_context_high->equity_24h` score `18.8908` n `57` status `ready` deltaP `44.1246` edge `1.3711` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.2068` n `58` status `ready` deltaP `38.0256` edge `0.5372` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.786` n `45` status `ready` deltaP `33.313` edge `0.5337` maxDD `-0.8896`
- `market_context_high->metal_24h` score `8.1133` n `57` status `ready` deltaP `42.3611` edge `0.3937` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.4125` n `45` status `ready` deltaP `20.1728` edge `0.3771` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0525` n `58` status `ready` deltaP `36.8534` edge `0.0963` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.4457` n `58` status `ready` deltaP `19.5695` edge `0.177` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.3724` n `50` status `ready` deltaP `25.1557` edge `0.1442` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.8402` n `45` status `ready` deltaP `23.75` edge `0.0974` maxDD `-0.191`
- `news_risk_high->metal_4h` score `1.9519` n `45` status `ready` deltaP `18.3672` edge `0.087` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.8335` n `58` status `ready` deltaP `21.1388` edge `0.0257` maxDD `-0.1069`
- `news_risk_high->crypto_major_1h` score `1.8103` n `50` status `ready` deltaP `11.2934` edge `0.1153` maxDD `-1.1783`
- `market_context_high->index_24h` score `1.7677` n `57` status `ready` deltaP `15.6524` edge `0.1893` maxDD `-1.3621`
- `news_risk_high->crypto_alt_1h` score `1.5969` n `50` status `ready` deltaP `12.0419` edge `0.0962` maxDD `-1.1388`
- `market_context_high->metal_4h` score `1.4927` n `58` status `ready` deltaP `19.6699` edge `0.0555` maxDD `-0.979`
- `news_risk_high->crypto_alt_4h` score `1.3195` n `45` status `ready` deltaP `14.5732` edge `0.2112` maxDD `-5.8012`
- `market_context_high->fx_24h` score `0.8268` n `57` status `ready` deltaP `18.549` edge `0.0527` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `0.7473` n `57` status `ready` deltaP `25.9868` edge `0.2111` maxDD `-15.7497`
- `market_context_high->crypto_alt_24h` score `0.6125` n `57` status `ready` deltaP `2.659` edge `0.4958` maxDD `-23.1336`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
