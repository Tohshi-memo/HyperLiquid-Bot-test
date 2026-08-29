# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T23:37:27.275777+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `risk_on_high->crypto_alt_4h` score `7.3624` n `49` status `ready` deltaP `25.3578` edge `0.4755` maxDD `-0.4812`
- `risk_on_and_context->crypto_alt_4h` score `7.3624` n `49` status `ready` deltaP `25.3578` edge `0.4755` maxDD `-0.4812`
- `risk_on_high->crypto_major_4h` score `6.3463` n `49` status `ready` deltaP `34.5539` edge `0.3261` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.3463` n `49` status `ready` deltaP `34.5539` edge `0.3261` maxDD `-1.208`
- `news_risk_high->crypto_alt_24h` score `5.5574` n `43` status `ready` deltaP `20.3933` edge `0.9141` maxDD `-22.3391`
- `news_risk_high->unknown_4h` score `5.1801` n `51` status `ready` deltaP `-1.5633` edge `0.5011` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6814` n `104` status `ready` deltaP `34.415` edge `0.2626` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.2967` n `51` status `ready` deltaP `-5.8764` edge `0.3496` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.1224` n `49` status `ready` deltaP `35.1886` edge `0.0342` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.1224` n `49` status `ready` deltaP `35.1886` edge `0.0342` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.3647` n `49` status `ready` deltaP `19.0487` edge `0.095` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.3647` n `49` status `ready` deltaP `19.0487` edge `0.095` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.8884` n `151` status `ready` deltaP `18.4471` edge `0.0814` maxDD `-1.0945`
- `risk_on_high->index_4h` score `1.4555` n `49` status `ready` deltaP `21.2419` edge `0.0106` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.4555` n `49` status `ready` deltaP `21.2419` edge `0.0106` maxDD `-0.1405`
- `market_context_high->unknown_1h` score `1.4145` n `163` status `ready` deltaP `8.5468` edge `0.109` maxDD `-1.5148`
- `risk_on_high->metal_1h` score `1.2089` n `61` status `ready` deltaP `17.1984` edge `0.0075` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.2089` n `61` status `ready` deltaP `17.1984` edge `0.0075` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `1.0978` n `51` status `ready` deltaP `27.3583` edge `0.0133` maxDD `-0.3953`
- `risk_on_high->unknown_1h` score `0.7221` n `61` status `ready` deltaP `1.5167` edge `0.094` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
