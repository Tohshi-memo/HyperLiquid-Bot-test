# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T15:37:31.691482+00:00`
- Price records: `672`
- Market context records: `7042`
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

- `market_context_high->fx_4h` score `0.0219` n `204` status `ready` deltaP `13.7553` edge `0.0103` maxDD `-0.9353`
- `market_context_high->fx_1h` score `-0.2184` n `204` status `ready` deltaP `2.3277` edge `0.0016` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.2767` n `204` status `ready` deltaP `2.2749` edge `0.0358` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5565` n `204` status `ready` deltaP `4.1535` edge `0.0362` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.7325` n `204` status `ready` deltaP `-0.1938` edge `-0.0015` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.746` n `204` status `ready` deltaP `-2.9265` edge `-0.0145` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-0.7592` n `204` status `ready` deltaP `-2.9177` edge `-0.0011` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-1.0374` n `204` status `ready` deltaP `-2.6976` edge `0.0098` maxDD `-2.5944`
- `market_context_high->unknown_4h` score `-1.6862` n `204` status `ready` deltaP `-6.3666` edge `0.0937` maxDD `-7.0087`
- `market_context_high->equity_1h` score `-1.77` n `204` status `ready` deltaP `4.4499` edge `-0.0143` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.0387` n `204` status `ready` deltaP `4.4745` edge `-0.0213` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-2.0657` n `204` status `ready` deltaP `3.9574` edge `0.0071` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.0894` n `204` status `ready` deltaP `-3.8528` edge `-0.0324` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.2405` n `200` status `ready` deltaP `-0.2292` edge `-0.0543` maxDD `-4.4704`
- `market_context_high->unknown_24h` score `-2.3857` n `200` status `ready` deltaP `-10.5556` edge `0.263` maxDD `-22.2126`
- `market_context_high->crypto_alt_4h` score `-2.5279` n `204` status `ready` deltaP `3.0817` edge `0.0339` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7822` n `204` status `ready` deltaP `4.3132` edge `0.043` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.6563` n `200` status `ready` deltaP `-1.6319` edge `-0.0111` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.3593` n `204` status `ready` deltaP `4.7465` edge `-0.0881` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.6891` n `200` status `ready` deltaP `-15.4444` edge `-0.0731` maxDD `-43.5089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
