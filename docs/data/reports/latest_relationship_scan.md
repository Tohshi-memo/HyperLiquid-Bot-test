# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T21:07:34.690577+00:00`
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

- `news_risk_high->equity_4h` score `7.5425` n `36` status `ready` deltaP `39.7866` edge `0.3633` maxDD `0.0`
- `news_risk_high->index_4h` score `2.3285` n `36` status `ready` deltaP `25.8638` edge `0.0348` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.2665` n `32` status `ready` deltaP `15.9722` edge `0.2997` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.2665` n `32` status `ready` deltaP `15.9722` edge `0.2997` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.17` n `32` status `ready` deltaP `14.7104` edge `0.101` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.17` n `32` status `ready` deltaP `14.7104` edge `0.101` maxDD `-0.1258`
- `news_risk_high->equity_1h` score `1.8077` n `36` status `ready` deltaP `9.3314` edge `0.1203` maxDD `-0.5496`
- `risk_on_high->commodity_24h` score `1.7573` n `32` status `ready` deltaP `16.1458` edge `0.0388` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.7573` n `32` status `ready` deltaP `16.1458` edge `0.0388` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6355` n `32` status `ready` deltaP `18.2292` edge `0.0332` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6355` n `32` status `ready` deltaP `18.2292` edge `0.0332` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.1173` n `32` status `ready` deltaP `12.3129` edge `0.0343` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1173` n `32` status `ready` deltaP `12.3129` edge `0.0343` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8475` n `32` status `ready` deltaP `9.6799` edge `0.0202` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8475` n `32` status `ready` deltaP `9.6799` edge `0.0202` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.8092` n `169` status `ready` deltaP `11.1416` edge `0.057` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.7173` n `169` status `ready` deltaP `9.8351` edge `0.0264` maxDD `-0.5752`
- `risk_on_high->index_24h` score `0.68` n `32` status `ready` deltaP `8.5069` edge `0.0304` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `0.68` n `32` status `ready` deltaP `8.5069` edge `0.0304` maxDD `-0.4355`
- `risk_on_high->index_1h` score `0.3062` n `32` status `ready` deltaP `10.1048` edge `0.0094` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
