# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T14:07:23.376817+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9941`

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

- `risk_on_high->unknown_24h` score `116.6309` n `109` status `ready` deltaP `23.885` edge `9.571` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `116.6309` n `109` status `ready` deltaP `23.885` edge `9.571` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `9.0088` n `109` status `ready` deltaP `21.6329` edge `1.118` maxDD `-32.9189`
- `risk_on_and_context->crypto_major_24h` score `9.0088` n `109` status `ready` deltaP `21.6329` edge `1.118` maxDD `-32.9189`
- `market_context_high->equity_24h` score `2.3216` n `196` status `ready` deltaP `14.6755` edge `0.3465` maxDD `-11.7362`
- `risk_on_high->crypto_alt_24h` score `0.8366` n `109` status `ready` deltaP `9.9022` edge `0.4684` maxDD `-28.1759`
- `risk_on_and_context->crypto_alt_24h` score `0.8366` n `109` status `ready` deltaP `9.9022` edge `0.4684` maxDD `-28.1759`
- `risk_on_high->index_1h` score `-0.1135` n `137` status `ready` deltaP `4.9882` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1135` n `137` status `ready` deltaP `4.9882` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->equity_24h` score `-0.2075` n `109` status `ready` deltaP `5.4123` edge `0.1871` maxDD `-11.2382`
- `risk_on_and_context->equity_24h` score `-0.2075` n `109` status `ready` deltaP `5.4123` edge `0.1871` maxDD `-11.2382`
- `risk_on_high->metal_1h` score `-0.2193` n `137` status `ready` deltaP `6.7092` edge `-0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.2193` n `137` status `ready` deltaP `6.7092` edge `-0.0016` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.3339` n `137` status `ready` deltaP `2.1253` edge `0.0597` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3339` n `137` status `ready` deltaP `2.1253` edge `0.0597` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.4459` n `137` status `ready` deltaP `6.4492` edge `-0.0127` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4459` n `137` status `ready` deltaP `6.4492` edge `-0.0127` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.4752` n `137` status `ready` deltaP `1.508` edge `0.0007` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.4752` n `137` status `ready` deltaP `1.508` edge `0.0007` maxDD `-1.0281`
- `market_context_high->crypto_alt_24h` score `-0.5312` n `196` status `ready` deltaP `13.1413` edge `0.3798` maxDD `-30.9337`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
