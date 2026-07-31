# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T17:22:30.068739+00:00`
- Price records: `672`
- Market context records: `8534`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5914`

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

- `news_risk_high->unknown_24h` score `6279.8438` n `52` status `ready` deltaP `43.3494` edge `523.0734` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8124` n `64` status `ready` deltaP `21.2652` edge `0.4023` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0483` n `64` status `ready` deltaP `16.8064` edge `0.0777` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7529` n `64` status `ready` deltaP `16.1022` edge `0.0864` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0234` n `64` status `ready` deltaP `6.7454` edge `0.1638` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8355` n `64` status `ready` deltaP `14.939` edge `0.1467` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4921` n `64` status `ready` deltaP `8.561` edge `0.0587` maxDD `-1.8813`
- `market_context_high->crypto_alt_4h` score `0.3956` n `50` status `ready` deltaP `6.439` edge `0.1035` maxDD `-5.323`
- `news_risk_high->crypto_major_1h` score `0.3485` n `64` status `ready` deltaP `6.7646` edge `0.0508` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0714` n `64` status `ready` deltaP `4.9869` edge `0.004` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0479` n `64` status `ready` deltaP `2.782` edge `0.0352` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0278` n `64` status `ready` deltaP `3.9203` edge `0.0091` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0216` n `64` status `ready` deltaP `11.3186` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0856` n `64` status `ready` deltaP `3.7051` edge `0.0085` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2934` n `62` status `ready` deltaP `1.9123` edge `-0.0001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3169` n `62` status `ready` deltaP `3.7087` edge `-0.0028` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4847` n `62` status `ready` deltaP `-2.4773` edge `0.0171` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7405` n `62` status `ready` deltaP `0.9465` edge `-0.0151` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9266` n `62` status `ready` deltaP `-2.5449` edge `-0.0108` maxDD `-1.6224`
- `market_context_high->commodity_4h` score `-1.1013` n `50` status `ready` deltaP `0.6707` edge `0.0058` maxDD `-5.4508`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
