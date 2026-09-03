# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T17:07:27.844061+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11625`

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

- `risk_on_high->unknown_4h` score `31.4418` n `133` status `ready` deltaP `12.657` edge `2.5976` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `31.4418` n `133` status `ready` deltaP `12.657` edge `2.5976` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `24.6768` n `167` status `ready` deltaP `14.2553` edge `2.0309` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.5389` n `133` status `ready` deltaP `1.0422` edge `1.429` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.5389` n `133` status `ready` deltaP `1.0422` edge `1.429` maxDD `-1.95`
- `market_context_high->unknown_1h` score `12.0591` n `167` status `ready` deltaP `1.497` edge `1.058` maxDD `-2.0446`
- `market_context_high->equity_24h` score `2.6727` n `127` status `ready` deltaP `19.9488` edge `0.5243` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.4743` n `67` status `ready` deltaP `19.5248` edge `0.4805` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `2.1898` n `107` status `ready` deltaP `15.195` edge `0.4957` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `2.1898` n `107` status `ready` deltaP `15.195` edge `0.4957` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `1.9218` n `67` status `ready` deltaP `16.0215` edge `0.5779` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.222` n `67` status `ready` deltaP `7.6207` edge `0.3526` maxDD `-15.4056`
- `news_risk_high->commodity_4h` score `0.3883` n `67` status `ready` deltaP `7.3193` edge `0.0369` maxDD `-0.8733`
- `risk_on_high->crypto_alt_24h` score `0.2215` n `107` status `ready` deltaP `15.3541` edge `0.6164` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.2215` n `107` status `ready` deltaP `15.3541` edge `0.6164` maxDD `-42.8959`
- `news_risk_high->fx_4h` score `0.0909` n `67` status `ready` deltaP `10.2612` edge `0.0048` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0595` n `133` status `ready` deltaP `11.6643` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0595` n `133` status `ready` deltaP `11.6643` edge `0.0011` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.057` n `67` status `ready` deltaP `4.6251` edge `-0.0028` maxDD `-0.8275`
- `market_context_high->crypto_alt_24h` score `-0.0575` n `127` status `ready` deltaP `17.0098` edge `0.6291` maxDD `-46.3234`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
