# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T02:37:27.547676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.6072` n `107` status `ready` deltaP `23.2691` edge `0.5406` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.6072` n `107` status `ready` deltaP `23.2691` edge `0.5406` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.015` n `154` status `ready` deltaP `19.3123` edge `0.442` maxDD `-2.5597`
- `market_context_high->unknown_1h` score `2.0173` n `154` status `ready` deltaP `4.6544` edge `0.2001` maxDD `-2.042`
- `risk_on_high->unknown_1h` score `1.999` n `107` status `ready` deltaP `4.5694` edge `0.1938` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.999` n `107` status `ready` deltaP `4.5694` edge `0.1938` maxDD `-1.9475`
- `risk_on_high->commodity_24h` score `1.6248` n `103` status `ready` deltaP `13.7102` edge `0.1428` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.6248` n `103` status `ready` deltaP `13.7102` edge `0.1428` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.093` n `61` status `ready` deltaP `1.6737` edge `0.1146` maxDD `-1.1072`
- `risk_on_high->crypto_alt_24h` score `1.0519` n `103` status `ready` deltaP `14.1485` edge `0.7309` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.0519` n `103` status `ready` deltaP `14.1485` edge `0.7309` maxDD `-42.8959`
- `market_context_high->commodity_24h` score `0.4316` n `150` status `ready` deltaP `11.7361` edge `0.0954` maxDD `-2.6803`
- `risk_on_high->fx_24h` score `0.1747` n `103` status `ready` deltaP `37.5995` edge `0.0236` maxDD `-4.1491`
- `risk_on_and_context->fx_24h` score `0.1747` n `103` status `ready` deltaP `37.5995` edge `0.0236` maxDD `-4.1491`
- `news_risk_high->commodity_4h` score `0.1499` n `61` status `ready` deltaP `5.8152` edge `0.0221` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1353` n `61` status `ready` deltaP `10.5008` edge `0.0006` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0795` n `154` status `ready` deltaP `8.4455` edge `0.0153` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `0.0185` n `107` status `ready` deltaP `5.9209` edge `0.0151` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0185` n `107` status `ready` deltaP `5.9209` edge `0.0151` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0462` n `107` status `ready` deltaP `5.8481` edge `-0.0004` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
