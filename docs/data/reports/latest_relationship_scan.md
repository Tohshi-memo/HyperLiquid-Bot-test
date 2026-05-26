# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T22:52:17.891763+00:00`
- Price records: `672`
- Market context records: `1984`
- Flow alert records: `7602`
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

- `market_context_high->crypto_alt_4h` score `7.3988` n `234` status `ready` deltaP `22.5649` edge `0.5806` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8624` n `234` status `ready` deltaP `26.3511` edge `0.5208` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.5023` n `234` status `ready` deltaP `13.743` edge `0.3193` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1531` n `234` status `ready` deltaP `13.601` edge `0.1982` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.9432` n `199` status `ready` deltaP `16.6104` edge `0.2938` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.7449` n `199` status `ready` deltaP `16.7627` edge `0.5657` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.267` n `199` status `ready` deltaP `15.2888` edge `0.4935` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.0579` n `234` status `ready` deltaP `9.8508` edge `0.1211` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.8339` n `234` status `ready` deltaP `8.5445` edge `0.1239` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.5149` n `199` status `ready` deltaP `4.1922` edge `0.1378` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `0.4862` n `199` status `ready` deltaP `19.8304` edge `0.7669` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.0481` n `234` status `ready` deltaP `6.9158` edge `0.0668` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.1796` n `199` status `ready` deltaP `10.446` edge `0.0203` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1893` n `234` status `ready` deltaP `4.2006` edge `0.0356` maxDD `-2.6836`
- `market_context_high->index_1h` score `-0.6808` n `234` status `ready` deltaP `-0.2635` edge `0.0082` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6849` n `234` status `ready` deltaP `-3.612` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1951` n `234` status `ready` deltaP `-9.059` edge `-0.004` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.3898` n `234` status `ready` deltaP `2.3492` edge `0.0021` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4796` n `234` status `ready` deltaP `0.8087` edge `-0.0335` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.89` n `234` status `ready` deltaP `1.8591` edge `0.0011` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
