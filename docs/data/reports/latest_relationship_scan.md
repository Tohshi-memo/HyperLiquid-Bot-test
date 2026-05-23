# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T19:07:15.708699+00:00`
- Price records: `672`
- Market context records: `1659`
- Flow alert records: `6684`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `9.9383` n `169` status `ready` deltaP `28.9337` edge `0.8779` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.4157` n `192` status `ready` deltaP `22.4244` edge `0.4849` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7959` n `169` status `ready` deltaP `20.5841` edge `0.3169` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.5665` n `192` status `ready` deltaP `18.4741` edge `0.3616` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.9074` n `192` status `ready` deltaP `12.6902` edge `0.1838` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7693` n `169` status `ready` deltaP `19.9473` edge `0.5043` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.9043` n `169` status `ready` deltaP `25.7468` edge `0.7623` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.7056` n `169` status `ready` deltaP `26.401` edge `1.0637` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.6143` n `203` status `ready` deltaP `6.6989` edge `0.1089` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.2091` n `203` status `ready` deltaP `2.1209` edge `0.0399` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3726` n `192` status `ready` deltaP `1.3841` edge `0.0519` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.385` n `203` status `ready` deltaP `2.7337` edge `0.0598` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4503` n `169` status `ready` deltaP `6.387` edge `0.0248` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.4575` n `203` status `ready` deltaP `-0.7477` edge `0.0095` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7614` n `203` status `ready` deltaP `4.5109` edge `0.0059` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.8032` n `203` status `ready` deltaP `-0.0914` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-1.1788` n `203` status `ready` deltaP `0.3768` edge `-0.0145` maxDD `-8.7978`
- `market_context_high->metal_4h` score `-1.2825` n `192` status `ready` deltaP `9.0017` edge `0.1023` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.9252` n `192` status `ready` deltaP `-8.1359` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.0527` n `192` status `ready` deltaP `11.3989` edge `-0.1866` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
