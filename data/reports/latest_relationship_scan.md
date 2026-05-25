# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T01:07:18.821362+00:00`
- Price records: `672`
- Market context records: `1795`
- Flow alert records: `7062`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8892`

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

- `market_context_high->metal_24h` score `7.2484` n `190` status `ready` deltaP `28.6549` edge `0.6556` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.4232` n `30` status `ready` deltaP `29.1057` edge `0.4067` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.7856` n `195` status `ready` deltaP `21.6979` edge `0.5141` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.5129` n `195` status `ready` deltaP `23.0152` edge `0.451` maxDD `-9.9352`
- `market_context_high->unknown_4h` score `3.8501` n `195` status `ready` deltaP `15.8216` edge `0.431` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2662` n `30` status `ready` deltaP `24.8703` edge `0.1381` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9519` n `195` status `ready` deltaP `16.4462` edge `0.2458` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.6787` n `190` status `ready` deltaP `13.6751` edge `0.2549` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.4568` n `190` status `ready` deltaP `15.276` edge `0.5094` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8992` n `195` status `ready` deltaP `12.6203` edge `0.0997` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8569` n `30` status `ready` deltaP `21.0265` edge `-0.0031` maxDD `-0.1774`
- `market_context_high->unknown_24h` score `0.8347` n `190` status `ready` deltaP `12.1948` edge `0.5203` maxDD `-35.8966`
- `news_risk_high->unknown_4h` score `0.4568` n `30` status `ready` deltaP `10.437` edge `0.0613` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.356` n `197` status `ready` deltaP `7.1127` edge `0.0934` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.2051` n `197` status `ready` deltaP `4.8155` edge `0.0836` maxDD `-3.2225`
- `market_context_high->equity_1h` score `-0.058` n `197` status `ready` deltaP `4.5024` edge `0.046` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3403` n `197` status `ready` deltaP `2.687` edge `0.0169` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3566` n `195` status `ready` deltaP `12.3562` edge `0.1411` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.3948` n `190` status `ready` deltaP `8.8962` edge `0.0127` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4123` n `30` status `ready` deltaP `17.006` edge `-0.119` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
