# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T15:22:38.675984+00:00`
- Price records: `672`
- Market context records: `1950`
- Flow alert records: `7509`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.0278` n `232` status `ready` deltaP `21.6932` edge `0.5555` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4712` n `232` status `ready` deltaP `25.3756` edge `0.4947` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4065` n `232` status `ready` deltaP `13.5948` edge `0.3123` maxDD `-9.8581`
- `market_context_high->equity_4h` score `1.9961` n `232` status `ready` deltaP `14.0233` edge `0.1823` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.8983` n `199` status `ready` deltaP `15.7353` edge `0.502` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.7894` n `234` status `ready` deltaP `8.2041` edge `0.1097` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6241` n `234` status `ready` deltaP `7.4966` edge `0.1134` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2438` n `199` status `ready` deltaP `11.9871` edge `0.183` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1261` n `199` status `ready` deltaP `4.1922` edge `0.1054` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1059` n `232` status `ready` deltaP `8.2086` edge `0.063` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.205` n `234` status `ready` deltaP `4.6497` edge `0.0313` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2639` n `199` status `ready` deltaP `9.9323` edge `0.0167` maxDD `-1.3925`
- `market_context_high->equity_24h` score `-0.41` n `199` status `ready` deltaP `10.1518` edge `0.388` maxDD `-33.1875`
- `market_context_high->index_1h` score `-0.6053` n `234` status `ready` deltaP `0.6347` edge `0.0085` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6335` n `234` status `ready` deltaP `-2.7138` edge `0.0001` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0564` n `232` status `ready` deltaP `-6.5724` edge `-0.0028` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.24` n `234` status `ready` deltaP `3.3971` edge `0.0076` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.5407` n `234` status `ready` deltaP `0.3596` edge `-0.0356` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8229` n `232` status `ready` deltaP `6.8666` edge `0.0715` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-1.8243` n `199` status `ready` deltaP `14.6934` edge `0.6086` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
