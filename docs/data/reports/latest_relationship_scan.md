# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T10:37:17.285453+00:00`
- Price records: `672`
- Market context records: `1727`
- Flow alert records: `6878`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8838`

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

- `market_context_high->metal_24h` score `6.7798` n `146` status `ready` deltaP `25.7975` edge `0.6356` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8773` n `196` status `ready` deltaP `20.8188` edge `0.5276` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `5.6451` n `146` status `ready` deltaP `16.7654` edge `0.8907` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.4018` n `196` status `ready` deltaP `22.8721` edge `0.4549` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.0845` n `146` status `ready` deltaP `17.6874` edge `0.3453` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0773` n `196` status `ready` deltaP `13.7941` edge `0.3916` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.0177` n `196` status `ready` deltaP `16.2643` edge `0.2525` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9823` n `146` status `ready` deltaP `16.5047` edge `0.545` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.774` n `196` status `ready` deltaP `7.7203` edge `0.1154` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5553` n `196` status `ready` deltaP `8.8166` edge `0.0964` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.222` n `196` status `ready` deltaP `5.0471` edge `0.0922` maxDD `-3.9211`
- `market_context_high->crypto_alt_24h` score `0.1173` n `146` status `ready` deltaP `22.4534` edge `1.041` maxDD `-88.8062`
- `market_context_high->equity_1h` score `0.0239` n `196` status `ready` deltaP `4.6713` edge `0.0517` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.3392` n `196` status `ready` deltaP `11.8343` edge `0.1468` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.382` n `196` status `ready` deltaP `1.9706` edge `0.0182` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5619` n `196` status `ready` deltaP `5.3465` edge `0.0259` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6482` n `196` status `ready` deltaP `-2.8168` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.7134` n `146` status `ready` deltaP `20.9603` edge `0.6594` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.764` n `146` status `ready` deltaP `5.1809` edge `0.0067` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.4173` n `196` status `ready` deltaP `2.1355` edge `0.0146` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
