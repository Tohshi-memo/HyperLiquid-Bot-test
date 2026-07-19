# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T08:37:25.316418+00:00`
- Price records: `672`
- Market context records: `7232`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13702`

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

- `risk_on_high->crypto_major_4h` score `5.8145` n `34` status `ready` deltaP `26.3182` edge `0.3474` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.8145` n `34` status `ready` deltaP `26.3182` edge `0.3474` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.2711` n `34` status `ready` deltaP `17.1001` edge `0.2812` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.2711` n `34` status `ready` deltaP `17.1001` edge `0.2812` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1072` n `34` status `ready` deltaP `22.5784` edge `0.0401` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1072` n `34` status `ready` deltaP `22.5784` edge `0.0401` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0322` n `34` status `ready` deltaP `4.9856` edge `0.1371` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0322` n `34` status `ready` deltaP `4.9856` edge `0.1371` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.284` n `34` status `ready` deltaP `7.7756` edge `0.0136` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.284` n `34` status `ready` deltaP `7.7756` edge `0.0136` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.1921` n `34` status `ready` deltaP `2.448` edge `0.0297` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.1921` n `34` status `ready` deltaP `2.448` edge `0.0297` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.0805` n `34` status `ready` deltaP `3.9814` edge `0.023` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.0805` n `34` status `ready` deltaP `3.9814` edge `0.023` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2795` n `172` status `ready` deltaP `1.8765` edge `0.0006` maxDD `-0.5817`
- `risk_on_high->commodity_4h` score `-0.5397` n `34` status `ready` deltaP `1.0491` edge `-0.0092` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.5397` n `34` status `ready` deltaP `1.0491` edge `-0.0092` maxDD `-0.7546`
- `market_context_high->commodity_1h` score `-0.6035` n `172` status `ready` deltaP `-0.4038` edge `-0.0126` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7512` n `172` status `ready` deltaP `-0.9783` edge `0.0141` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7574` n `172` status `ready` deltaP `3.0219` edge `0.0238` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
