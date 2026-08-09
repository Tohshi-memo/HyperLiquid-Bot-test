# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T17:22:26.881376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10842`

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

- `market_context_high->equity_24h` score `2.7571` n `108` status `ready` deltaP `3.4722` edge `0.5126` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.0042` n `108` status `ready` deltaP `8.5069` edge `0.1679` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3198` n `143` status `ready` deltaP `16.2716` edge `0.0688` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8924` n `143` status `ready` deltaP `11.8892` edge `0.0294` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6523` n `108` status `ready` deltaP `20.8334` edge `0.0314` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.2721` n `108` status `ready` deltaP `6.0185` edge `0.1479` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4187` n `143` status `ready` deltaP `2.7983` edge `-0.004` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4408` n `143` status `ready` deltaP `-1.8424` edge `-0.0053` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.6234` n `143` status `ready` deltaP `4.1511` edge `-0.0043` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7064` n `143` status `ready` deltaP `-5.1871` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.9622` n `143` status `ready` deltaP `-1.5254` edge `-0.0095` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.978` n `143` status `ready` deltaP `-0.7862` edge `0.0066` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0279` n `143` status `ready` deltaP `-1.9657` edge `-0.0178` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0655` n `143` status `ready` deltaP `-11.3312` edge `-0.0324` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.625` n `143` status `ready` deltaP `-2.0286` edge `-0.0715` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.3568` n `143` status `ready` deltaP `-12.4838` edge `-0.0643` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.9957` n `143` status `ready` deltaP `-8.7338` edge `-0.1091` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.2394` n `108` status `ready` deltaP `1.4467` edge `-0.1135` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.3138` n `108` status `ready` deltaP `-17.7662` edge `-0.2634` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8304` n `143` status `ready` deltaP `-6.2435` edge `-0.5662` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
