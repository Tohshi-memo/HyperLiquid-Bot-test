# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T17:37:28.029477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11679`

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

- `risk_on_high->unknown_4h` score `30.7626` n `133` status `ready` deltaP `12.657` edge `2.541` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `30.7626` n `133` status `ready` deltaP `12.657` edge `2.541` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `23.9976` n `167` status `ready` deltaP `14.2553` edge `1.9743` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.4645` n `133` status `ready` deltaP `1.0422` edge `1.4228` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.4645` n `133` status `ready` deltaP `1.0422` edge `1.4228` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.9847` n `167` status `ready` deltaP `1.497` edge `1.0518` maxDD `-2.0446`
- `market_context_high->equity_24h` score `2.4697` n `127` status `ready` deltaP `19.6016` edge `0.5097` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.2347` n `67` status `ready` deltaP `19.1775` edge `0.4521` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `1.9868` n `107` status `ready` deltaP `14.8478` edge `0.4811` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.9868` n `107` status `ready` deltaP `14.8478` edge `0.4811` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `1.6588` n `67` status `ready` deltaP `15.6743` edge `0.5465` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.0901` n `67` status `ready` deltaP `7.2735` edge `0.338` maxDD `-15.4056`
- `news_risk_high->commodity_4h` score `0.408` n `67` status `ready` deltaP `7.6242` edge `0.0374` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0897` n `67` status `ready` deltaP `10.2612` edge `0.0047` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0509` n `133` status `ready` deltaP `11.5146` edge `0.001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0509` n `133` status `ready` deltaP `11.5146` edge `0.001` maxDD `-1.699`
- `risk_on_high->crypto_alt_24h` score `-0.0181` n `107` status `ready` deltaP `15.0068` edge `0.588` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `-0.0181` n `107` status `ready` deltaP `15.0068` edge `0.588` maxDD `-42.8959`
- `news_risk_high->index_1h` score `-0.0664` n `67` status `ready` deltaP `4.4754` edge `-0.003` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1045` n `133` status `ready` deltaP `4.8906` edge `-0.0015` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
