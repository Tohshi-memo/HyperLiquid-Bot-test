# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T17:37:23.279973+00:00`
- Price records: `672`
- Market context records: `1960`
- Flow alert records: `7536`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7565`

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

- `market_context_high->crypto_alt_4h` score `6.956` n `234` status `ready` deltaP `21.6502` edge `0.5498` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4243` n `234` status `ready` deltaP `25.284` edge `0.4914` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4529` n `234` status `ready` deltaP `13.5906` edge `0.3162` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2378` n `234` status `ready` deltaP `14.2107` edge `0.2012` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.2291` n `199` status `ready` deltaP `16.4203` edge `0.525` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.8937` n `234` status `ready` deltaP `8.8029` edge `0.1144` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6624` n `234` status `ready` deltaP `7.6463` edge `0.1156` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.6536` n `199` status `ready` deltaP `13.0145` edge `0.2103` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.2664` n `234` status `ready` deltaP `8.7451` edge `0.0728` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.2593` n `199` status `ready` deltaP `4.1922` edge `0.1165` maxDD `-4.1604`
- `market_context_high->equity_24h` score `0.1705` n `199` status `ready` deltaP `11.6929` edge `0.4261` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.1918` n `234` status `ready` deltaP `4.7994` edge `0.0314` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2555` n `199` status `ready` deltaP `9.9323` edge `0.0174` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6281` n `234` status `ready` deltaP `0.6347` edge `0.0066` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.667` n `234` status `ready` deltaP `-3.3126` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1024` n `234` status `ready` deltaP `-7.3822` edge `-0.0033` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2388` n `234` status `ready` deltaP `3.5468` edge `0.0067` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-1.2486` n `199` status `ready` deltaP `16.2345` edge `0.6463` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.6342` n `234` status `ready` deltaP `0.0602` edge `-0.0414` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8312` n `234` status `ready` deltaP `6.9276` edge `0.0704` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
