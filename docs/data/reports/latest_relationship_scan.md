# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T19:22:31.113416+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `news_risk_high->equity_4h` score `7.5651` n `36` status `ready` deltaP `39.6341` edge `0.3662` maxDD `0.0`
- `news_risk_high->index_4h` score `2.4173` n `36` status `ready` deltaP `26.7784` edge `0.0361` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.3791` n `32` status `ready` deltaP `16.6667` edge `0.3095` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.3791` n `32` status `ready` deltaP `16.6667` edge `0.3095` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.12` n `32` status `ready` deltaP `14.1006` edge `0.1009` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.12` n `32` status `ready` deltaP `14.1006` edge `0.1009` maxDD `-0.1258`
- `news_risk_high->equity_1h` score `1.7645` n `36` status `ready` deltaP `8.8823` edge `0.1197` maxDD `-0.5496`
- `risk_on_high->commodity_24h` score `1.6813` n `32` status `ready` deltaP `15.4514` edge `0.0371` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.6813` n `32` status `ready` deltaP `15.4514` edge `0.0371` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6355` n `32` status `ready` deltaP `18.2292` edge `0.0332` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6355` n `32` status `ready` deltaP `18.2292` edge `0.0332` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.0825` n `32` status `ready` deltaP `11.8638` edge `0.0344` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0825` n `32` status `ready` deltaP `11.8638` edge `0.0344` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8975` n `32` status `ready` deltaP `10.2896` edge `0.0203` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8975` n `32` status `ready` deltaP `10.2896` edge `0.0203` maxDD `-0.1285`
- `risk_on_high->index_24h` score `0.8817` n `32` status `ready` deltaP `9.7222` edge `0.0391` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `0.8817` n `32` status `ready` deltaP `9.7222` edge `0.0391` maxDD `-0.4355`
- `market_context_high->commodity_4h` score `0.7026` n `171` status `ready` deltaP `10.2446` edge `0.0541` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.6518` n `171` status `ready` deltaP `9.1957` edge `0.0252` maxDD `-0.5752`
- `risk_on_high->equity_24h` score `0.6094` n `32` status `ready` deltaP `2.6042` edge `0.2387` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
