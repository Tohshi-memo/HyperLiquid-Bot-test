# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T19:07:26.102969+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11330`

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

- `news_risk_high->unknown_24h` score `30.2596` n `60` status `ready` deltaP `3.6458` edge `2.5947` maxDD `-4.1232`
- `risk_on_high->crypto_alt_4h` score `12.4629` n `33` status `ready` deltaP `47.1221` edge `0.7303` maxDD `-0.1367`
- `risk_on_and_context->crypto_alt_4h` score `12.4629` n `33` status `ready` deltaP `47.1221` edge `0.7303` maxDD `-0.1367`
- `market_context_high->unknown_24h` score `11.2651` n `104` status `ready` deltaP `20.9535` edge `0.8723` maxDD `-3.1917`
- `news_risk_high->crypto_alt_24h` score `10.7935` n `60` status `ready` deltaP `29.6181` edge `1.5239` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `8.1566` n `33` status `ready` deltaP `38.9274` edge `0.4478` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `8.1566` n `33` status `ready` deltaP `38.9274` edge `0.4478` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `5.7839` n `69` status `ready` deltaP `7.9047` edge `0.4883` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6958` n `104` status `ready` deltaP `34.415` edge `0.2638` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `2.9827` n `33` status `ready` deltaP `32.6774` edge `0.0393` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `2.9827` n `33` status `ready` deltaP `32.6774` edge `0.0393` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.5689` n `69` status `ready` deltaP `1.241` edge `0.2415` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.3261` n `133` status `ready` deltaP `18.8451` edge `0.1114` maxDD `-0.7887`
- `risk_on_high->unknown_4h` score `1.6363` n `33` status `ready` deltaP `30.8296` edge `-0.0554` maxDD `-0.4351`
- `risk_on_and_context->unknown_4h` score `1.6363` n `33` status `ready` deltaP `30.8296` edge `-0.0554` maxDD `-0.4351`
- `news_risk_high->fx_4h` score `1.5178` n `69` status `ready` deltaP `34.2789` edge `0.021` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.4101` n `43` status `ready` deltaP `19.3984` edge `0.0096` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.4101` n `43` status `ready` deltaP `19.3984` edge `0.0096` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.8641` n `133` status `ready` deltaP `21.7025` edge `0.2724` maxDD `-20.9394`
- `risk_on_high->equity_4h` score `0.8352` n `33` status `ready` deltaP `6.1854` edge `0.0533` maxDD `-0.3281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
