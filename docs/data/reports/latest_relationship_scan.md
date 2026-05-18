# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T12:37:21.105673+00:00`
- Price records: `672`
- Market context records: `1118`
- Flow alert records: `5122`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8704`

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

- `market_context_high->crypto_major_24h` score `18.4484` n `150` status `ready` deltaP `39.8125` edge `1.3183` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `8.0943` n `150` status `ready` deltaP `16.1736` edge `0.6901` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.6321` n `150` status `ready` deltaP `16.5208` edge `0.4922` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5667` n `150` status `ready` deltaP `-1.8889` edge `0.6432` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.2715` n `150` status `ready` deltaP `15.4791` edge `0.3669` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5531` n `168` status `ready` deltaP `8.8125` edge `0.137` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.828` n `168` status `ready` deltaP `7.68` edge `0.0861` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.469` n `168` status `ready` deltaP `7.4957` edge `0.0208` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2057` n `168` status `ready` deltaP `2.2811` edge `0.0397` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1484` n `168` status `ready` deltaP `8.4652` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.0125` n `168` status `ready` deltaP `7.847` edge `0.1382` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0434` n `168` status `ready` deltaP `6.6831` edge `0.0284` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2436` n `168` status `ready` deltaP `6.8007` edge `-0.0046` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3857` n `168` status `ready` deltaP `2.3453` edge `0.0365` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7057` n `168` status `ready` deltaP `1.2412` edge `0.0009` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7317` n `168` status `ready` deltaP `-1.9247` edge `-0.0002` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0702` n `168` status `ready` deltaP `5.2338` edge `0.1244` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.4602` n `168` status `ready` deltaP `5.9378` edge `-0.0492` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1551` n `168` status `ready` deltaP `-11.1208` edge `-0.0136` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.354` n `168` status `ready` deltaP `9.0085` edge `-0.2179` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
