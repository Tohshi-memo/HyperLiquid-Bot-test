# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T02:52:29.218107+00:00`
- Price records: `672`
- Market context records: `6348`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.173` n `32` status `ready` deltaP `42.5347` edge `0.9956` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.137` n `32` status `ready` deltaP `50.8681` edge `0.1723` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4502` n `32` status `ready` deltaP `17.5347` edge `0.5316` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1278` n `32` status `ready` deltaP `42.9116` edge `0.0625` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.6796` n `32` status `ready` deltaP `32.2917` edge `0.1119` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3883` n `32` status `ready` deltaP `28.7425` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5614` n `32` status `ready` deltaP `15.3256` edge `0.1447` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9525` n `32` status `ready` deltaP `11.9199` edge `0.0888` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.6453` n `196` status `ready` deltaP `13.6542` edge `0.0424` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.0646` n `207` status `ready` deltaP `-7.5154` edge `0.1563` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0189` n `196` status `ready` deltaP `6.4118` edge `0.0223` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.6365` n `207` status `ready` deltaP `3.378` edge `0.0022` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.6412` n `130` status `ready` deltaP `-5.1602` edge `0.1386` maxDD `-6.2457`
- `market_context_high->commodity_1h` score `-0.6464` n `207` status `ready` deltaP `-1.9902` edge `-0.0013` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.7122` n `130` status `ready` deltaP `13.6698` edge `0.0744` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.714` n `32` status `ready` deltaP `0.3472` edge `-0.0067` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7312` n `207` status `ready` deltaP `-0.8469` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7473` n `32` status `ready` deltaP `-3.1437` edge `-0.0251` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.7503` n `196` status `ready` deltaP `4.6043` edge `0.043` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.7935` n `32` status `ready` deltaP `5.4828` edge `-0.0682` maxDD `-0.7581`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
