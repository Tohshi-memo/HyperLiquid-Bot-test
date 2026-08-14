# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T22:37:51.965704+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `136.3723` n `128` status `ready` deltaP `-30.9896` edge `11.8622` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9209` n `32` status `ready` deltaP `-44.2708` edge `4.5908` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9209` n `32` status `ready` deltaP `-44.2708` edge `4.5908` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.9214` n `36` status `ready` deltaP `15.625` edge `0.8439` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6813` n `36` status `ready` deltaP `40.3963` edge `0.3708` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.925` n `128` status `ready` deltaP `27.8645` edge `0.2304` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5011` n `32` status `ready` deltaP `30.2083` edge `0.1737` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5011` n `32` status `ready` deltaP `30.2083` edge `0.1737` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.2404` n `32` status `ready` deltaP `21.875` edge `0.3852` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.2404` n `32` status `ready` deltaP `21.875` edge `0.3852` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.6644` n `32` status `ready` deltaP `18.5213` edge `0.1168` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6644` n `32` status `ready` deltaP `18.5213` edge `0.1168` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5972` n `36` status `ready` deltaP `19.4444` edge `0.0868` maxDD `0.0`
- `news_risk_high->index_4h` score `1.8097` n `36` status `ready` deltaP `20.8333` edge `0.0251` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7274` n `36` status `ready` deltaP `8.4332` edge `0.1196` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.7166` n `128` status `ready` deltaP `16.9588` edge `0.0771` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.2335` n `32` status `ready` deltaP `13.2111` edge `0.038` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2335` n `32` status `ready` deltaP `13.2111` edge `0.038` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.0199` n `32` status `ready` deltaP `12.5` edge `0.0201` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.0199` n `32` status `ready` deltaP `12.5` edge `0.0201` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
