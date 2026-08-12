# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T20:07:40.317971+00:00`
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

- `news_risk_high->equity_4h` score `7.5241` n `36` status `ready` deltaP `39.4817` edge `0.3638` maxDD `0.0`
- `news_risk_high->index_4h` score `2.3723` n `36` status `ready` deltaP `26.3211` edge `0.0354` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.3228` n `32` status `ready` deltaP `16.3194` edge `0.3046` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.3228` n `32` status `ready` deltaP `16.3194` edge `0.3046` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.1116` n `32` status `ready` deltaP `14.1006` edge `0.1002` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1116` n `32` status `ready` deltaP `14.1006` edge `0.1002` maxDD `-0.1258`
- `news_risk_high->equity_1h` score `1.7729` n `36` status `ready` deltaP `9.032` edge `0.1194` maxDD `-0.5496`
- `risk_on_high->commodity_24h` score `1.7127` n `32` status `ready` deltaP `15.7986` edge `0.0374` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.7127` n `32` status `ready` deltaP `15.7986` edge `0.0374` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6343` n `32` status `ready` deltaP `18.2292` edge `0.0331` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6343` n `32` status `ready` deltaP `18.2292` edge `0.0331` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.0741` n `32` status `ready` deltaP `11.8638` edge `0.0337` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0741` n `32` status `ready` deltaP `11.8638` edge `0.0337` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8853` n `32` status `ready` deltaP `10.1372` edge `0.0203` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8853` n `32` status `ready` deltaP `10.1372` edge `0.0203` maxDD `-0.1285`
- `risk_on_high->index_24h` score `0.786` n `32` status `ready` deltaP `9.2014` edge `0.0346` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `0.786` n `32` status `ready` deltaP `9.2014` edge `0.0346` maxDD `-0.4355`
- `market_context_high->commodity_4h` score `0.7568` n `170` status `ready` deltaP `10.6815` edge `0.0557` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.6973` n `170` status `ready` deltaP `9.5844` edge `0.0264` maxDD `-0.5752`
- `risk_on_high->equity_24h` score `0.3623` n `32` status `ready` deltaP `2.0833` edge `0.2105` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
