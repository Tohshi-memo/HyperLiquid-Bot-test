# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T14:52:25.242239+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.6502` n `128` status `ready` deltaP `-23.596` edge `11.9194` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7516` n `32` status `ready` deltaP `-36.8772` edge `4.648` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7516` n `32` status `ready` deltaP `-36.8772` edge `4.648` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9484` n `36` status `ready` deltaP `26.4875` edge `0.9404` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7413` n `36` status `ready` deltaP `40.3963` edge `0.3758` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.4803` n `128` status `ready` deltaP `31.9716` edge `0.2493` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.0564` n `32` status `ready` deltaP `34.3154` edge `0.1926` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.0564` n `32` status `ready` deltaP `34.3154` edge `0.1926` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2222` n `32` status `ready` deltaP `28.2008` edge `0.4689` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2222` n `32` status `ready` deltaP `28.2008` edge `0.4689` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.6757` n `36` status `ready` deltaP `30.6759` edge `0.1018` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9002` n `32` status `ready` deltaP `20.8079` edge `0.1212` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9002` n `32` status `ready` deltaP `20.8079` edge `0.1212` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.9523` n `128` status `ready` deltaP `19.2454` edge `0.0815` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9388` n `36` status `ready` deltaP `22.3577` edge `0.0257` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7358` n `36` status `ready` deltaP `8.2835` edge `0.1213` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3581` n `32` status `ready` deltaP `14.5584` edge `0.0394` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3581` n `32` status `ready` deltaP `14.5584` edge `0.0394` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7703` n `32` status `ready` deltaP `15.0292` edge `0.1765` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7703` n `32` status `ready` deltaP `15.0292` edge `0.1765` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
