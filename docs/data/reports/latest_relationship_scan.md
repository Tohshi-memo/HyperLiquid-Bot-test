# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T21:52:22.858429+00:00`
- Price records: `672`
- Market context records: `1979`
- Flow alert records: `7589`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7584`

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

- `market_context_high->crypto_alt_4h` score `7.3892` n `234` status `ready` deltaP `22.5649` edge `0.5798` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8348` n `234` status `ready` deltaP `26.3511` edge `0.5185` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4817` n `234` status `ready` deltaP `13.5906` edge `0.3186` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1797` n `234` status `ready` deltaP `13.7534` edge `0.1994` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.6868` n `199` status `ready` deltaP `15.9255` edge `0.277` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.6501` n `199` status `ready` deltaP `16.7627` edge `0.5578` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.0646` n `199` status `ready` deltaP `14.6039` edge `0.4812` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.9968` n `234` status `ready` deltaP `9.252` edge `0.12` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.7572` n `234` status `ready` deltaP `7.9457` edge `0.1215` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.4597` n `199` status `ready` deltaP `4.1922` edge `0.1332` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `0.1434` n `199` status `ready` deltaP `19.1454` edge `0.7429` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.0541` n `234` status `ready` deltaP `6.9158` edge `0.0673` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1749` n `234` status `ready` deltaP `4.3503` edge `0.0358` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1832` n `199` status `ready` deltaP `10.446` edge `0.02` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.66` n `234` status `ready` deltaP `-3.1629` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6664` n `234` status `ready` deltaP `-0.1138` edge `0.0084` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.161` n `234` status `ready` deltaP `-8.4493` edge `-0.0037` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.3479` n `234` status `ready` deltaP `2.7983` edge `0.0026` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4556` n `234` status `ready` deltaP `1.1081` edge `-0.0335` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.8853` n `234` status `ready` deltaP `2.0088` edge `0.0007` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
