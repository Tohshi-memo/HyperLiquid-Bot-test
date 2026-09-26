# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T04:37:27.847313+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11758`

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

- `news_risk_high->unknown_24h` score `3162.1461` n `94` status `ready` deltaP `-0.7166` edge `263.5214` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.543` n `47` status `ready` deltaP `8.0201` edge `5.8322` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.9383` n `47` status `ready` deltaP `25.7351` edge `3.9459` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.3609` n `47` status `ready` deltaP `23.3931` edge `2.4121` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2879` n `47` status `ready` deltaP `33.3739` edge `1.9204` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.3956` n `47` status `ready` deltaP `32.6795` edge `0.4114` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.5595` n `47` status `ready` deltaP `30.0237` edge `0.1203` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7179` n `47` status `ready` deltaP `17.1445` edge `0.154` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5286` n `47` status `ready` deltaP `29.1483` edge `0.0318` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.109` n `47` status `ready` deltaP `10.6026` edge `0.0885` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0901` n `47` status `ready` deltaP `12.5143` edge `0.0477` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `1.0763` n `94` status `ready` deltaP `26.8322` edge `0.1252` maxDD `-6.9545`
- `market_context_high->index_1h` score `0.7702` n `47` status `ready` deltaP `12.3646` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4973` n `47` status `ready` deltaP `10.4089` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.4052` n `94` status `ready` deltaP `13.5306` edge `0.0437` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3326` n `47` status `ready` deltaP `5.2013` edge `0.0748` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.303` n `47` status `ready` deltaP `4.0801` edge `0.0885` maxDD `-5.2359`
- `news_risk_high->index_1h` score `0.2311` n `123` status `ready` deltaP `6.5698` edge `0.0047` maxDD `-0.3395`
- `news_risk_high->crypto_alt_1h` score `0.0237` n `123` status `ready` deltaP `6.1645` edge `0.053` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0225` n `47` status `ready` deltaP `9.1691` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
