# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T21:52:26.132188+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1381.0113` n `40` status `ready` deltaP `-22.5694` edge `115.2711` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `48.3584` n `96` status `ready` deltaP `-2.9217` edge `4.1074` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7984` n `40` status `ready` deltaP `27.6736` edge `0.5916` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4108` n `40` status `ready` deltaP `52.4306` edge `0.1847` maxDD `0.0`
- `market_context_high->unknown_1h` score `4.4649` n `108` status `ready` deltaP `-2.9108` edge `0.4251` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.0538` n `40` status `ready` deltaP `34.6875` edge `0.0362` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.3948` n `40` status `ready` deltaP `-21.1111` edge `0.5718` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.6879` n `96` status `ready` deltaP `11.7887` edge `0.0071` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.6199` n `96` status `ready` deltaP `13.0335` edge `0.0181` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3234` n `108` status `ready` deltaP `7.2466` edge `0.007` maxDD `-0.6025`
- `market_context_high->metal_4h` score `0.1464` n `96` status `ready` deltaP `9.4766` edge `0.0213` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `0.077` n `108` status `ready` deltaP `4.918` edge `0.0805` maxDD `-4.9401`
- `market_context_high->fx_1h` score `-0.0707` n `108` status `ready` deltaP `2.1679` edge `0.0007` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.1035` n `108` status `ready` deltaP `7.0138` edge `0.0035` maxDD `-0.7107`
- `market_context_high->crypto_major_4h` score `-0.1127` n `96` status `ready` deltaP `0.4065` edge `0.1934` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-0.3238` n `96` status `ready` deltaP `-2.185` edge `0.2289` maxDD `-13.8008`
- `market_context_high->crypto_major_1h` score `-0.3983` n `108` status `ready` deltaP `-1.0756` edge `0.045` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.5532` n `96` status `ready` deltaP `-1.0924` edge `0.0064` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7967` n `108` status `ready` deltaP `-5.3504` edge `-0.0014` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.988` n `108` status `ready` deltaP `-6.2874` edge `0.0022` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
