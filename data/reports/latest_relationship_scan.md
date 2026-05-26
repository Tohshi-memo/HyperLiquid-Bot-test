# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T23:22:15.124454+00:00`
- Price records: `672`
- Market context records: `1986`
- Flow alert records: `7608`
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

- `market_context_high->crypto_alt_4h` score `7.5171` n `232` status `ready` deltaP `22.9342` edge `0.588` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2624` n `232` status `ready` deltaP `27.0658` edge `0.5288` maxDD `-3.9895`
- `market_context_high->unknown_4h` score `2.9093` n `232` status `ready` deltaP `14.3398` edge `0.33` maxDD `-8.9859`
- `market_context_high->equity_4h` score `2.2207` n `232` status `ready` deltaP `13.9666` edge `0.2014` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.9278` n `197` status `ready` deltaP `16.7182` edge `0.2918` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.8855` n `197` status `ready` deltaP `16.6148` edge `0.5784` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.2861` n `197` status `ready` deltaP `15.4527` edge `0.494` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.0845` n `232` status `ready` deltaP `10.0635` edge `0.1219` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.8074` n `232` status `ready` deltaP `8.2129` edge `0.1239` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.5525` n `197` status `ready` deltaP `19.9534` edge `0.7716` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.4562` n `197` status `ready` deltaP `3.9984` edge `0.1342` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1997` n `232` status `ready` deltaP `7.2224` edge `0.0681` maxDD `-3.6352`
- `market_context_high->fx_24h` score `0.0313` n `197` status `ready` deltaP `11.2266` edge `0.0219` maxDD `-1.1973`
- `market_context_high->equity_1h` score `-0.1994` n `232` status `ready` deltaP `4.0445` edge `0.0358` maxDD `-2.6836`
- `market_context_high->fx_1h` score `-0.6621` n `232` status `ready` deltaP `-3.2031` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7144` n `232` status `ready` deltaP `-0.6246` edge `0.0078` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.2052` n `232` status `ready` deltaP `-9.241` edge `-0.0041` maxDD `-1.1041`
- `market_context_high->unknown_1h` score `-1.4027` n `232` status `ready` deltaP `1.2802` edge `-0.0304` maxDD `-3.6022`
- `market_context_high->metal_1h` score `-1.4265` n `232` status `ready` deltaP `1.9513` edge `0.0017` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.8908` n `232` status `ready` deltaP `1.8738` edge `0.0009` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
