# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T13:22:36.156935+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->crypto_alt_24h` score `18.2788` n `60` status `ready` deltaP `42.5` edge `1.3869` maxDD `-9.4264`
- `risk_on_and_context->crypto_alt_24h` score `18.2788` n `60` status `ready` deltaP `42.5` edge `1.3869` maxDD `-9.4264`
- `risk_on_high->unknown_4h` score `8.1312` n `107` status `ready` deltaP `25.4032` edge `0.5699` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.1312` n `107` status `ready` deltaP `25.4032` edge `0.5699` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5852` n `159` status `ready` deltaP `22.0998` edge `0.4708` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `5.6138` n `60` status `ready` deltaP `66.6667` edge `0.0511` maxDD `-0.5514`
- `risk_on_and_context->fx_24h` score `5.6138` n `60` status `ready` deltaP `66.6667` edge `0.0511` maxDD `-0.5514`
- `risk_on_high->crypto_major_24h` score `5.0315` n `60` status `ready` deltaP `27.0833` edge `0.7277` maxDD `-17.0558`
- `risk_on_and_context->crypto_major_24h` score `5.0315` n `60` status `ready` deltaP `27.0833` edge `0.7277` maxDD `-17.0558`
- `market_context_high->metal_24h` score `4.2048` n `102` status `ready` deltaP `32.4346` edge `0.2251` maxDD `-2.2747`
- `market_context_high->crypto_major_24h` score `4.0185` n `102` status `ready` deltaP `20.7108` edge `0.4784` maxDD `-18.1945`
- `market_context_high->crypto_alt_24h` score `3.9844` n `102` status `ready` deltaP `20.8334` edge `0.7909` maxDD `-27.517`
- `risk_on_high->unknown_1h` score `2.3986` n `107` status `ready` deltaP `6.5155` edge `0.2141` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.3986` n `107` status `ready` deltaP `6.5155` edge `0.2141` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.176` n `159` status `ready` deltaP `5.8572` edge `0.2053` maxDD `-2.041`
- `risk_on_high->metal_24h` score `1.9869` n `60` status `ready` deltaP `33.6111` edge `0.1162` maxDD `-2.1767`
- `risk_on_and_context->metal_24h` score `1.9869` n `60` status `ready` deltaP `33.6111` edge `0.1162` maxDD `-2.1767`
- `news_risk_high->unknown_1h` score `1.4951` n `61` status `ready` deltaP `3.6198` edge `0.1351` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.0715` n `102` status `ready` deltaP `37.7451` edge `0.0316` maxDD `-1.6688`
- `news_risk_high->commodity_24h` score `0.6651` n `44` status `ready` deltaP `7.9072` edge `0.0641` maxDD `-1.1904`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
