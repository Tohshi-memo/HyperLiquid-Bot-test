# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T17:52:19.506724+00:00`
- Price records: `672`
- Market context records: `1961`
- Flow alert records: `7539`
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

- `market_context_high->crypto_alt_4h` score `7.0114` n `234` status `ready` deltaP `21.8027` edge `0.5534` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4713` n `234` status `ready` deltaP `25.4365` edge `0.4943` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4469` n `234` status `ready` deltaP `13.5906` edge `0.3157` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2558` n `234` status `ready` deltaP `14.2107` edge `0.2027` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.2483` n `199` status `ready` deltaP `16.4203` edge `0.5266` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.9176` n `234` status `ready` deltaP `8.9526` edge `0.1154` maxDD `-3.2225`
- `market_context_high->metal_24h` score `0.7249` n `199` status `ready` deltaP `13.1858` edge `0.2151` maxDD `-12.7414`
- `market_context_high->crypto_alt_1h` score `0.6936` n `234` status `ready` deltaP `7.796` edge `0.1172` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.2833` n `199` status `ready` deltaP `4.1922` edge `0.1185` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.2772` n `234` status `ready` deltaP `8.7451` edge `0.0737` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.2454` n `199` status `ready` deltaP `11.8642` edge `0.4312` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.187` n `234` status `ready` deltaP `4.7994` edge `0.0318` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2543` n `199` status `ready` deltaP `9.9323` edge `0.0175` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6245` n `234` status `ready` deltaP `0.6347` edge `0.0069` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6755` n `234` status `ready` deltaP `-3.4623` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1103` n `234` status `ready` deltaP `-7.5347` edge `-0.0033` maxDD `-1.1056`
- `market_context_high->crypto_major_24h` score `-1.1569` n `199` status `ready` deltaP `16.4057` edge `0.6528` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-1.2245` n `234` status `ready` deltaP `3.6965` edge `0.0069` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.6342` n `234` status `ready` deltaP `0.0602` edge `-0.0414` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8288` n `234` status `ready` deltaP `6.9276` edge `0.0706` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
