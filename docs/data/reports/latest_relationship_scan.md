# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T17:38:21.540538+00:00`
- Price records: `672`
- Market context records: `6838`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11802`

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

- `market_context_high->unknown_24h` score `0.9693` n `176` status `ready` deltaP `-1.5467` edge `0.5098` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0583` n `176` status `ready` deltaP `9.012` edge `0.1316` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2703` n `216` status `ready` deltaP `1.838` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_major_1h` score `-0.4986` n `216` status `ready` deltaP `4.455` edge `0.0189` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.5024` n `216` status `ready` deltaP `2.4534` edge `0.0182` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8825` n `216` status `ready` deltaP `-2.6281` edge `-0.0045` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.016` n `216` status `ready` deltaP `-6.4011` edge `-0.0108` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-1.0767` n `216` status `ready` deltaP `-2.4229` edge `-0.0051` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-1.0916` n `204` status `ready` deltaP `9.4094` edge `0.0037` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.6257` n `216` status `ready` deltaP `-3.2962` edge `-0.0234` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9707` n `216` status `ready` deltaP `-0.0804` edge `-0.0341` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.2313` n `204` status `ready` deltaP `0.6666` edge `-0.0352` maxDD `-11.0917`
- `market_context_high->commodity_4h` score `-2.3463` n `204` status `ready` deltaP `-4.6718` edge `-0.0154` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.7334` n `204` status `ready` deltaP `-3.5868` edge `-0.0282` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9073` n `204` status `ready` deltaP `0.3736` edge `-0.0425` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0952` n `204` status `ready` deltaP `0.3946` edge `-0.0411` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2158` n `204` status `ready` deltaP `-9.5887` edge `0.0325` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.46` n `176` status `ready` deltaP `-9.7853` edge `-0.0028` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.7407` n `204` status `ready` deltaP `-1.5782` edge `-0.2188` maxDD `-54.046`
- `market_context_high->metal_24h` score `-9.2719` n `176` status `ready` deltaP `-19.0183` edge `-0.2134` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
