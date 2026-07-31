# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T15:37:37.169285+00:00`
- Price records: `672`
- Market context records: `8527`
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

- `news_risk_high->unknown_24h` score `6280.1042` n `52` status `ready` deltaP `44.5646` edge `523.087` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7056` n `64` status `ready` deltaP `21.2652` edge `0.3934` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0495` n `64` status `ready` deltaP `16.8064` edge `0.0778` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7685` n `64` status `ready` deltaP `16.1022` edge `0.0877` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9224` n `64` status `ready` deltaP `6.2881` edge `0.1539` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.837` n `64` status `ready` deltaP `14.939` edge `0.1469` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5201` n `64` status `ready` deltaP `9.0101` edge `0.0593` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3407` n `64` status `ready` deltaP `6.6149` edge `0.0508` maxDD `-2.0972`
- `market_context_high->crypto_alt_4h` score `0.2895` n `43` status `ready` deltaP `5.9274` edge `0.0933` maxDD `-5.323`
- `news_risk_high->fx_1h` score `0.1142` n `64` status `ready` deltaP `5.7354` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0762` n `64` status `ready` deltaP `3.0869` edge `0.0368` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0558` n `64` status `ready` deltaP `4.3694` edge `0.0097` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0314` n `64` status `ready` deltaP `11.471` edge `0.0219` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0844` n `64` status `ready` deltaP `3.7051` edge `0.0086` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.1817` n `55` status `ready` deltaP `4.9728` edge `0.0061` maxDD `-2.0038`
- `market_context_high->metal_1h` score `-0.4573` n `55` status `ready` deltaP `0.1824` edge `-0.0104` maxDD `-1.6224`
- `market_context_high->commodity_4h` score `-0.5035` n `43` status `ready` deltaP `6.5726` edge `0.0431` maxDD `-5.4508`
- `market_context_high->fx_4h` score `-0.7948` n `43` status `ready` deltaP `-0.5566` edge `-0.0041` maxDD `-1.007`
- `market_context_high->crypto_alt_1h` score `-0.8462` n `55` status `ready` deltaP `-6.9842` edge `0.0008` maxDD `-3.0178`
- `market_context_high->fx_1h` score `-0.9285` n `55` status `ready` deltaP `-3.4976` edge `-0.0038` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
