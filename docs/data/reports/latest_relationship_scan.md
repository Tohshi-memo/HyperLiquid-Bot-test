# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T20:22:20.915740+00:00`
- Price records: `672`
- Market context records: `1972`
- Flow alert records: `7570`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7583`

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

- `market_context_high->crypto_alt_4h` score `7.387` n `234` status `ready` deltaP `22.7173` edge `0.5786` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7734` n `234` status `ready` deltaP `26.1987` edge `0.5144` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4625` n `234` status `ready` deltaP `13.5906` edge `0.317` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2752` n `234` status `ready` deltaP `14.3632` edge `0.2033` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.5493` n `199` status `ready` deltaP `16.7627` edge `0.5494` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.3166` n `199` status `ready` deltaP `14.8981` edge `0.253` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.9716` n `234` status `ready` deltaP `9.1023` edge `0.1189` maxDD `-3.2225`
- `market_context_high->equity_24h` score `0.7868` n `199` status `ready` deltaP `13.5765` edge `0.4649` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7824` n `234` status `ready` deltaP `8.0954` edge `0.1226` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.4105` n `199` status `ready` deltaP `4.1922` edge `0.1291` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1764` n `234` status `ready` deltaP `7.8304` edge `0.0714` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0539` n `234` status `ready` deltaP `5.2485` edge `0.0399` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1952` n `199` status `ready` deltaP `10.446` edge `0.019` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.336` n `199` status `ready` deltaP `18.118` edge `0.7098` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.5957` n `234` status `ready` deltaP `0.485` edge `0.0103` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6841` n `234` status `ready` deltaP `-3.612` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1198` n `234` status `ready` deltaP `-7.6871` edge `-0.0035` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.288` n `234` status `ready` deltaP `3.2474` edge `0.0046` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4616` n `234` status `ready` deltaP `0.9584` edge `-0.033` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.8682` n `234` status `ready` deltaP `2.3082` edge `0.0009` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
