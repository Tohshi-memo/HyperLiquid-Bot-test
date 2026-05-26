# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T23:52:17.822065+00:00`
- Price records: `672`
- Market context records: `1988`
- Flow alert records: `7615`
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

- `market_context_high->crypto_major_4h` score `7.6699` n `230` status `ready` deltaP `27.7929` edge `0.5376` maxDD `-3.0318`
- `market_context_high->crypto_alt_4h` score `7.6582` n `230` status `ready` deltaP `23.4676` edge `0.5962` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `3.3495` n `230` status `ready` deltaP `14.947` edge `0.3409` maxDD `-7.9138`
- `market_context_high->equity_4h` score `2.2643` n `230` status `ready` deltaP `14.0616` edge `0.2044` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.0258` n `195` status `ready` deltaP `16.4638` edge `0.5911` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.8869` n `195` status `ready` deltaP `16.8213` edge `0.2877` maxDD `-12.7414`
- `market_context_high->equity_24h` score `1.2804` n `195` status `ready` deltaP `15.4417` edge `0.4936` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.1334` n `230` status `ready` deltaP `10.2851` edge `0.1245` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.8632` n `230` status `ready` deltaP `8.4457` edge `0.127` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.6148` n `195` status `ready` deltaP `20.072` edge `0.776` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.3936` n `195` status `ready` deltaP `3.8005` edge `0.1303` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.3723` n `230` status `ready` deltaP `7.5398` edge `0.0697` maxDD `-3.4483`
- `market_context_high->fx_24h` score `0.2122` n `195` status `ready` deltaP `12.0231` edge `0.0233` maxDD `-1.1952`
- `market_context_high->equity_1h` score `-0.2123` n `230` status `ready` deltaP `3.8831` edge `0.0358` maxDD `-2.6836`
- `market_context_high->fx_1h` score `-0.6482` n `230` status `ready` deltaP `-2.9367` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7222` n `230` status `ready` deltaP `-0.7068` edge `0.0077` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.9397` n `230` status `ready` deltaP `1.8316` edge `0.0009` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.2141` n `230` status `ready` deltaP `-9.4234` edge `-0.0041` maxDD `-1.0983`
- `market_context_high->unknown_1h` score `-1.3763` n `230` status `ready` deltaP `1.1898` edge `-0.0276` maxDD `-3.6022`
- `market_context_high->commodity_1h` score `-1.9002` n `230` status `ready` deltaP `1.7534` edge `0.0005` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
