# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T19:52:41.473797+00:00`
- Price records: `672`
- Market context records: `3311`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.8855` n `32` status `ready` deltaP `30.1829` edge `1.2348` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8855` n `32` status `ready` deltaP `30.1829` edge `1.2348` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.9353` n `127` status `ready` deltaP `20.929` edge `2.7594` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.4853` n `127` status `ready` deltaP `32.5842` edge `0.912` maxDD `-16.1026`
- `market_context_high->equity_24h` score `8.6746` n `127` status `ready` deltaP `24.4873` edge `1.7905` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3575` n `32` status `ready` deltaP `9.8323` edge `0.732` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3575` n `32` status `ready` deltaP `9.8323` edge `0.732` maxDD `-11.7537`
- `market_context_high->commodity_24h` score `6.1877` n `127` status `ready` deltaP `30.6622` edge `0.5547` maxDD `-13.1447`
- `risk_on_high->equity_4h` score `3.5796` n `32` status `ready` deltaP `13.7957` edge `0.4804` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5796` n `32` status `ready` deltaP `13.7957` edge `0.4804` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.8018` n `127` status `ready` deltaP `21.9338` edge `2.2829` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.0759` n `32` status `ready` deltaP `7.1669` edge `0.3253` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0759` n `32` status `ready` deltaP `7.1669` edge `0.3253` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.0499` n `184` status `ready` deltaP `19.0416` edge `0.1397` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.09` n `32` status `ready` deltaP `0.8384` edge `0.1929` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.09` n `32` status `ready` deltaP `0.8384` edge `0.1929` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2868` n `32` status `ready` deltaP `6.3997` edge `0.0626` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2868` n `32` status `ready` deltaP `6.3997` edge `0.0626` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.247` n `32` status `ready` deltaP `0.5988` edge `0.1714` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.247` n `32` status `ready` deltaP `0.5988` edge `0.1714` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
