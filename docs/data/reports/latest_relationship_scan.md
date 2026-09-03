# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T17:22:31.695420+00:00`
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

- `risk_on_high->unknown_4h` score `31.2678` n `133` status `ready` deltaP `12.657` edge `2.5831` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `31.2678` n `133` status `ready` deltaP `12.657` edge `2.5831` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `24.5028` n `167` status `ready` deltaP `14.2553` edge `2.0164` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.4981` n `133` status `ready` deltaP `1.0422` edge `1.4256` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.4981` n `133` status `ready` deltaP `1.0422` edge `1.4256` maxDD `-1.95`
- `market_context_high->unknown_1h` score `12.0183` n `167` status `ready` deltaP `1.497` edge `1.0546` maxDD `-2.0446`
- `market_context_high->equity_24h` score `2.5724` n `127` status `ready` deltaP `19.7752` edge `0.5171` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.3537` n `67` status `ready` deltaP `19.3511` edge `0.4662` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `2.0895` n `107` status `ready` deltaP `15.0214` edge `0.4885` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `2.0895` n `107` status `ready` deltaP `15.0214` edge `0.4885` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `1.7919` n `67` status `ready` deltaP `15.8479` edge `0.5624` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.1568` n `67` status `ready` deltaP `7.4471` edge `0.3454` maxDD `-15.4056`
- `news_risk_high->commodity_4h` score `0.397` n `67` status `ready` deltaP `7.4718` edge `0.037` maxDD `-0.8733`
- `risk_on_high->crypto_alt_24h` score `0.1009` n `107` status `ready` deltaP `15.1804` edge `0.6021` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.1009` n `107` status `ready` deltaP `15.1804` edge `0.6021` maxDD `-42.8959`
- `news_risk_high->fx_4h` score `0.0909` n `67` status `ready` deltaP `10.2612` edge `0.0048` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0595` n `133` status `ready` deltaP `11.6643` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0595` n `133` status `ready` deltaP `11.6643` edge `0.0011` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0578` n `67` status `ready` deltaP `4.6251` edge `-0.0029` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.096` n `133` status `ready` deltaP `5.0403` edge `-0.0014` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
