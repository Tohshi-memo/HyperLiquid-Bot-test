# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T11:37:14.897173+00:00`
- Price records: `672`
- Market context records: `1732`
- Flow alert records: `6890`
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

- `market_context_high->metal_24h` score `6.8755` n `150` status `ready` deltaP `25.5986` edge `0.6449` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8135` n `196` status `ready` deltaP `20.6664` edge `0.5233` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `5.2211` n `150` status `ready` deltaP `16.4752` edge `0.8573` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.281` n `196` status `ready` deltaP `22.2623` edge `0.4489` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.2424` n `150` status `ready` deltaP `18.2353` edge `0.3548` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0857` n `196` status `ready` deltaP `13.7941` edge `0.3923` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9789` n `196` status `ready` deltaP `15.9594` edge `0.2513` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.3132` n `150` status `ready` deltaP `16.6067` edge `0.5719` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7321` n `196` status `ready` deltaP `7.4209` edge `0.1139` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5979` n `196` status `ready` deltaP `9.2739` edge `0.0969` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.2517` n `150` status `ready` deltaP `22.1084` edge `1.0545` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1705` n `196` status `ready` deltaP `4.598` edge `0.0909` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0466` n `196` status `ready` deltaP `4.9707` edge `0.0516` maxDD `-2.8014`
- `market_context_high->crypto_major_24h` score `-0.111` n `150` status `ready` deltaP `20.7797` edge `0.7108` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.3425` n `196` status `ready` deltaP `2.4197` edge `0.0185` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3661` n `196` status `ready` deltaP `11.3769` edge `0.1464` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5611` n `196` status `ready` deltaP `5.3465` edge `0.026` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.649` n `196` status `ready` deltaP `-2.8168` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7328` n `150` status `ready` deltaP `5.601` edge `0.0065` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.4964` n `196` status `ready` deltaP `1.5367` edge `0.012` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
