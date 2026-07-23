# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T15:37:26.473981+00:00`
- Price records: `672`
- Market context records: `7682`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->crypto_major_1h` score `0.2049` n `141` status `ready` deltaP `9.5745` edge `0.0291` maxDD `-3.4019`
- `market_context_high->index_1h` score `0.0918` n `141` status `ready` deltaP `6.8622` edge `0.0132` maxDD `-0.7743`
- `market_context_high->equity_1h` score `0.057` n `141` status `ready` deltaP `6.0699` edge `0.0673` maxDD `-5.3698`
- `market_context_high->crypto_major_4h` score `-0.0916` n `141` status `ready` deltaP `11.8545` edge `0.1062` maxDD `-8.4293`
- `market_context_high->crypto_alt_1h` score `-0.1614` n `141` status `ready` deltaP `2.6712` edge `0.0242` maxDD `-2.6829`
- `market_context_high->fx_24h` score `-0.1667` n `140` status `ready` deltaP `11.0802` edge `0.021` maxDD `-3.0343`
- `market_context_high->equity_24h` score `-0.2379` n `140` status `ready` deltaP `14.6341` edge `0.142` maxDD `-16.9384`
- `market_context_high->commodity_1h` score `-0.3867` n `141` status `ready` deltaP `1.7667` edge `0.0019` maxDD `-0.6722`
- `market_context_high->crypto_alt_4h` score `-0.4409` n `141` status `ready` deltaP `5.0672` edge `0.0797` maxDD `-7.018`
- `market_context_high->index_4h` score `-0.48` n `141` status `ready` deltaP `9.4216` edge `0.0353` maxDD `-2.4381`
- `market_context_high->commodity_4h` score `-0.489` n `141` status `ready` deltaP `1.516` edge `0.0085` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.5369` n `141` status `ready` deltaP `-0.5303` edge `-0.0014` maxDD `-0.5179`
- `market_context_high->equity_4h` score `-0.6251` n `141` status `ready` deltaP `1.1062` edge `0.2208` maxDD `-13.6655`
- `market_context_high->metal_1h` score `-0.6314` n `141` status `ready` deltaP `1.1105` edge `0.0162` maxDD `-1.0307`
- `market_context_high->commodity_24h` score `-1.4126` n `140` status `ready` deltaP `6.7247` edge `-0.0042` maxDD `-7.0012`
- `market_context_high->metal_4h` score `-1.4128` n `141` status `ready` deltaP `-0.9579` edge `0.0574` maxDD `-3.5711`
- `market_context_high->unknown_1h` score `-1.4516` n `141` status `ready` deltaP `-1.3632` edge `-0.0518` maxDD `-1.1399`
- `market_context_high->metal_24h` score `-1.5343` n `141` status `ready` deltaP `-1.1155` edge `0.0841` maxDD `-4.8699`
- `market_context_high->fx_4h` score `-2.5142` n `141` status `ready` deltaP `-6.1845` edge `-0.0038` maxDD `-1.8253`
- `market_context_high->index_24h` score `-3.2337` n `140` status `ready` deltaP `-20.5749` edge `-0.0275` maxDD `-5.3263`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
