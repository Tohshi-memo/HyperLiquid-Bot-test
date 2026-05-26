# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T15:37:17.480096+00:00`
- Price records: `672`
- Market context records: `1951`
- Flow alert records: `7512`
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

- `market_context_high->crypto_alt_4h` score `7.0354` n `232` status `ready` deltaP `21.7581` edge `0.5557` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4799` n `232` status `ready` deltaP `25.4389` edge `0.495` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.3878` n `232` status `ready` deltaP `13.511` edge `0.3113` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0244` n `232` status `ready` deltaP `14.0778` edge `0.1843` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.9564` n `199` status `ready` deltaP `15.9066` edge `0.5057` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.8205` n `234` status `ready` deltaP `8.3538` edge `0.1113` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6564` n `234` status `ready` deltaP `7.6463` edge `0.1151` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2642` n `199` status `ready` deltaP `11.9871` edge `0.1847` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1297` n `199` status `ready` deltaP `4.1922` edge `0.1057` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1165` n `232` status `ready` deltaP `8.2655` edge `0.0635` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2086` n `234` status `ready` deltaP `4.6497` edge `0.031` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2627` n `199` status `ready` deltaP `9.9323` edge `0.0168` maxDD `-1.3925`
- `market_context_high->equity_24h` score `-0.3459` n `199` status `ready` deltaP `10.3231` edge `0.3922` maxDD `-33.1875`
- `market_context_high->index_1h` score `-0.6113` n `234` status `ready` deltaP `0.6347` edge `0.008` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6343` n `234` status `ready` deltaP `-2.7138` edge `0.0` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0614` n `232` status `ready` deltaP `-6.6536` edge `-0.0029` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2424` n `234` status `ready` deltaP `3.3971` edge `0.0074` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.5695` n `234` status `ready` deltaP `0.2099` edge `-0.037` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.7674` n `199` status `ready` deltaP `14.8646` edge `0.6122` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.8373` n `232` status `ready` deltaP `6.7921` edge `0.0708` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
