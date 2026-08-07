# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T17:37:24.982169+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->metal_24h` score `2.8203` n `99` status `ready` deltaP `12.4825` edge `0.2094` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.7943` n `99` status `ready` deltaP `23.8127` edge `0.0513` maxDD `-3.3243`
- `market_context_high->commodity_4h` score `0.6182` n `109` status `ready` deltaP `11.7728` edge `0.0764` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.3297` n `121` status `ready` deltaP `8.8991` edge `0.0244` maxDD `-1.3171`
- `market_context_high->index_24h` score `0.3073` n `99` status `ready` deltaP `6.0024` edge `0.1369` maxDD `-5.7715`
- `market_context_high->fx_4h` score `0.1142` n `109` status `ready` deltaP `9.3113` edge `0.0061` maxDD `-1.6928`
- `market_context_high->equity_24h` score `-0.2236` n `99` status `ready` deltaP `-5.6925` edge `0.3996` maxDD `-24.0894`
- `market_context_high->fx_1h` score `-0.2589` n `121` status `ready` deltaP `5.1443` edge `-0.0051` maxDD `-1.0616`
- `market_context_high->index_4h` score `-0.7433` n `109` status `ready` deltaP `-2.4349` edge `-0.0126` maxDD `-1.6504`
- `market_context_high->index_1h` score `-0.7772` n `121` status `ready` deltaP `-1.8978` edge `-0.0104` maxDD `-1.3375`
- `market_context_high->crypto_alt_1h` score `-0.8678` n `121` status `ready` deltaP `-5.2098` edge `-0.0136` maxDD `-2.3669`
- `market_context_high->metal_4h` score `-0.9111` n `109` status `ready` deltaP `2.9397` edge `0.003` maxDD `-2.5483`
- `market_context_high->metal_1h` score `-1.0304` n `121` status `ready` deltaP `-4.2275` edge `-0.0081` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-1.1234` n `121` status `ready` deltaP `3.5941` edge `-0.0292` maxDD `-9.1031`
- `market_context_high->crypto_alt_4h` score `-1.2834` n `109` status `ready` deltaP `0.6223` edge `-0.0297` maxDD `-5.7857`
- `market_context_high->equity_4h` score `-2.5571` n `109` status `ready` deltaP `3.9956` edge `-0.1258` maxDD `-15.2933`
- `market_context_high->crypto_major_1h` score `-3.0069` n `121` status `ready` deltaP `-6.7254` edge `-0.0602` maxDD `-8.3095`
- `market_context_high->crypto_major_24h` score `-3.6654` n `99` status `ready` deltaP `-0.9056` edge `-0.1965` maxDD `-15.0579`
- `market_context_high->crypto_alt_24h` score `-4.1823` n `99` status `ready` deltaP `-14.1328` edge `-0.11` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.3934` n `109` status `ready` deltaP `-7.6485` edge `-0.1873` maxDD `-19.6643`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
