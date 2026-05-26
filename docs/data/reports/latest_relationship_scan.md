# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T21:07:18.892901+00:00`
- Price records: `672`
- Market context records: `1975`
- Flow alert records: `7580`
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

- `market_context_high->crypto_alt_4h` score `7.417` n `234` status `ready` deltaP `22.7173` edge `0.5811` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8106` n `234` status `ready` deltaP `26.1987` edge `0.5175` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4685` n `234` status `ready` deltaP `13.5906` edge `0.3175` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2342` n `234` status `ready` deltaP `14.2107` edge `0.2009` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.5997` n `199` status `ready` deltaP `16.7627` edge `0.5536` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.4981` n `199` status `ready` deltaP `15.4118` edge `0.2647` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.9824` n `234` status `ready` deltaP `9.1023` edge `0.1198` maxDD `-3.2225`
- `market_context_high->equity_24h` score `0.9227` n `199` status `ready` deltaP `14.0902` edge `0.4728` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7632` n `234` status `ready` deltaP `7.9457` edge `0.122` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.4249` n `199` status `ready` deltaP `4.1922` edge `0.1303` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1099` n `234` status `ready` deltaP `7.3731` edge `0.0689` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `-0.0909` n `199` status `ready` deltaP `18.6317` edge `0.7268` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1174` n `234` status `ready` deltaP `4.7994` edge `0.0376` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1904` n `199` status `ready` deltaP `10.446` edge `0.0194` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6328` n `234` status `ready` deltaP `0.1856` edge `0.0092` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6849` n `234` status `ready` deltaP `-3.612` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1365` n `234` status `ready` deltaP `-7.992` edge `-0.0036` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.3371` n `234` status `ready` deltaP `2.7983` edge `0.0035` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4556` n `234` status `ready` deltaP `1.1081` edge `-0.0335` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.8627` n `234` status `ready` deltaP `2.3082` edge `0.0016` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
