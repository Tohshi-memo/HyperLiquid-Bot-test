# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T16:54:07.959291+00:00`
- Price records: `672`
- Market context records: `8532`
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

- `news_risk_high->unknown_24h` score `6279.9063` n `52` status `ready` deltaP `43.6966` edge `523.0763` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7824` n `64` status `ready` deltaP `21.2652` edge `0.3998` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0495` n `64` status `ready` deltaP `16.8064` edge `0.0778` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7877` n `64` status `ready` deltaP `16.2519` edge `0.0883` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9763` n `64` status `ready` deltaP `6.4405` edge `0.1598` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8142` n `64` status `ready` deltaP `14.6341` edge `0.146` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5147` n `48` status `ready` deltaP `8.3841` edge `0.1058` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.4866` n `64` status `ready` deltaP `8.561` edge `0.058` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3244` n `64` status `ready` deltaP `6.4652` edge `0.0497` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0885` n `64` status `ready` deltaP `5.2863` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0605` n `64` status `ready` deltaP `2.9345` edge `0.0358` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0379` n `64` status `ready` deltaP `4.07` edge `0.0094` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.035` n `64` status `ready` deltaP `11.471` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0844` n `64` status `ready` deltaP `3.7051` edge `0.0086` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.3734` n `60` status `ready` deltaP `0.5988` edge `-0.0016` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.4202` n `60` status `ready` deltaP `2.0958` edge `-0.0053` maxDD `-2.0038`
- `market_context_high->index_1h` score `-0.8921` n `60` status `ready` deltaP `-0.4092` edge `-0.0187` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9326` n `60` status `ready` deltaP `-2.5449` edge `-0.0113` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.9644` n `60` status `ready` deltaP `-4.2515` edge `0.0107` maxDD `-3.0178`
- `market_context_high->commodity_4h` score `-0.9822` n `48` status `ready` deltaP `2.0326` edge `0.012` maxDD `-5.4508`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
