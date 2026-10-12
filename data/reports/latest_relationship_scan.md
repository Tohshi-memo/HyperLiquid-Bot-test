# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T06:37:27.700604+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9576`

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

- `market_context_high->unknown_4h` score `33.6145` n `119` status `ready` deltaP `-6.3781` edge `2.9113` maxDD `-2.0726`
- `market_context_high->crypto_major_24h` score `9.5166` n `54` status `ready` deltaP `20.544` edge `1.3467` maxDD `-13.7531`
- `risk_on_high->crypto_major_4h` score `6.0615` n `51` status `ready` deltaP `35.2492` edge `0.3554` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.0615` n `51` status `ready` deltaP `35.2492` edge `0.3554` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.3194` n `51` status `ready` deltaP `22.9436` edge `0.3351` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.3194` n `51` status `ready` deltaP `22.9436` edge `0.3351` maxDD `-1.9151`
- `market_context_high->crypto_alt_24h` score `5.3152` n `54` status `ready` deltaP `-1.1575` edge `1.0971` maxDD `-23.3024`
- `market_context_high->equity_24h` score `4.5397` n `54` status `ready` deltaP `20.081` edge `0.5459` maxDD `-4.1546`
- `market_context_high->index_24h` score `4.5173` n `54` status `ready` deltaP `39.0046` edge `0.1439` maxDD `-0.1993`
- `risk_on_high->crypto_alt_1h` score `1.7893` n `59` status `ready` deltaP `10.2152` edge `0.1407` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.7893` n `59` status `ready` deltaP `10.2152` edge `0.1407` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.4852` n `59` status `ready` deltaP `10.2684` edge `0.1206` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.4852` n `59` status `ready` deltaP `10.2684` edge `0.1206` maxDD `-3.2233`
- `risk_on_high->metal_4h` score `1.2585` n `51` status `ready` deltaP `15.4472` edge `0.0555` maxDD `-0.9555`
- `risk_on_and_context->metal_4h` score `1.2585` n `51` status `ready` deltaP `15.4472` edge `0.0555` maxDD `-0.9555`
- `market_context_high->crypto_alt_1h` score `1.1146` n `127` status `ready` deltaP `8.8005` edge `0.1293` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.9233` n `119` status `ready` deltaP `11.7198` edge `0.2508` maxDD `-11.1784`
- `market_context_high->crypto_major_1h` score `0.6656` n `127` status `ready` deltaP `5.157` edge `0.0974` maxDD `-3.4384`
- `market_context_high->crypto_alt_4h` score `0.3986` n `119` status `ready` deltaP `5.8567` edge `0.2679` maxDD `-13.8008`
- `market_context_high->metal_4h` score `0.1383` n `119` status `ready` deltaP `9.2847` edge `0.0219` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
