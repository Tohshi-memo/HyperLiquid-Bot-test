# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T15:53:11.935967+00:00`
- Price records: `672`
- Market context records: `8528`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6280.0555` n `52` status `ready` deltaP `44.391` edge `523.0841` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7392` n `64` status `ready` deltaP `21.2652` edge `0.3962` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0531` n `64` status `ready` deltaP `16.8064` edge `0.0781` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8081` n `64` status `ready` deltaP `16.2519` edge `0.09` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9428` n `64` status `ready` deltaP `6.4405` edge `0.1555` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8481` n `64` status `ready` deltaP `15.0915` edge `0.1473` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5334` n `64` status `ready` deltaP `9.1598` edge `0.06` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3563` n `64` status `ready` deltaP `6.7646` edge `0.0518` maxDD `-2.0972`
- `market_context_high->crypto_alt_4h` score `0.2365` n `44` status `ready` deltaP `4.8642` edge `0.0936` maxDD `-5.323`
- `news_risk_high->fx_1h` score `0.1142` n `64` status `ready` deltaP `5.7354` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0675` n `64` status `ready` deltaP `2.9345` edge `0.0367` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0667` n `64` status `ready` deltaP `4.5191` edge `0.0101` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0326` n `64` status `ready` deltaP `11.471` edge `0.022` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.082` n `64` status `ready` deltaP `3.7051` edge `0.0088` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.279` n `56` status `ready` deltaP `4.0312` edge `-0.0001` maxDD `-2.0038`
- `market_context_high->metal_1h` score `-0.408` n `56` status `ready` deltaP `1.0265` edge `-0.0097` maxDD `-1.6224`
- `market_context_high->commodity_4h` score `-0.6326` n `44` status `ready` deltaP `5.5155` edge `0.0336` maxDD `-5.4508`
- `market_context_high->fx_1h` score `-0.8482` n `56` status `ready` deltaP `-2.5235` edge `-0.0036` maxDD `-0.6874`
- `market_context_high->crypto_alt_1h` score `-0.8819` n `56` status `ready` deltaP `-7.5813` edge `0.0002` maxDD `-3.0178`
- `market_context_high->fx_4h` score `-0.888` n `44` status `ready` deltaP `-1.4551` edge `-0.0051` maxDD `-1.0691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
