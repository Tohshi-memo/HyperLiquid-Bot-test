# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T14:52:27.838829+00:00`
- Price records: `672`
- Market context records: `6401`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11091`

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

- `news_risk_high->crypto_alt_24h` score `13.5733` n `32` status `ready` deltaP `35.2431` edge `0.9109` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6557` n `32` status `ready` deltaP `56.0764` edge `0.1808` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3399` n `32` status `ready` deltaP `37.5` edge `0.1322` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.1348` n `32` status `ready` deltaP `16.8403` edge `0.4958` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0754` n `32` status `ready` deltaP `42.3018` edge `0.0622` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.491` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_24h` score `1.4875` n `146` status `ready` deltaP `8.036` edge `0.4351` maxDD `-17.8437`
- `news_risk_high->crypto_major_1h` score `1.432` n `32` status `ready` deltaP `13.6789` edge `0.1391` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8349` n `32` status `ready` deltaP `10.2732` edge `0.0847` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.4621` n `216` status `ready` deltaP `-5.4724` edge `0.1758` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3865` n `216` status `ready` deltaP `11.3144` edge `0.0406` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.044` n `216` status `ready` deltaP `7.5147` edge `0.0212` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2285` n `32` status `ready` deltaP `6.6804` edge `-0.0291` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3293` n `146` status `ready` deltaP `19.6205` edge `0.0986` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4637` n `216` status `ready` deltaP `2.3564` edge `0.0026` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.515` n `216` status `ready` deltaP `8.0793` edge `0.05` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6531` n `32` status `ready` deltaP `-1.3473` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.691` n `216` status `ready` deltaP `-2.8998` edge `0.0027` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7462` n `216` status `ready` deltaP `-1.0646` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.7504` n `216` status `ready` deltaP `-3.7037` edge `-0.0032` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
