# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T07:22:19.366716+00:00`
- Price records: `672`
- Market context records: `2223`
- Flow alert records: `8291`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `26.7991` n `33` status `ready` deltaP `57.8283` edge `1.9066` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.0741` n `33` status `ready` deltaP `48.185` edge `0.9789` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.6103` n `33` status `ready` deltaP `39.1572` edge `0.9046` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.9573` n `132` status `ready` deltaP `37.6063` edge `0.9227` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7088` n `132` status `ready` deltaP `41.8237` edge `0.7499` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `10.2277` n `33` status `ready` deltaP `38.7311` edge `0.6167` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `8.0619` n `33` status `ready` deltaP `20.6755` edge `0.9538` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.4706` n `132` status `ready` deltaP `21.2214` edge `0.3823` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.9346` n `43` status `ready` deltaP `32.9197` edge `0.3521` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3484` n `132` status `ready` deltaP `23.2631` edge `0.2334` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2296` n `136` status `ready` deltaP `17.7968` edge `0.1982` maxDD `-1.817`
- `market_context_high->index_4h` score `3.2186` n `132` status `ready` deltaP `26.6214` edge `0.1591` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.0789` n `136` status `ready` deltaP `17.0615` edge `0.2292` maxDD `-4.9097`
- `news_risk_high->fx_24h` score `2.9784` n `33` status `ready` deltaP `31.0606` edge `0.0596` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `2.5182` n `33` status `ready` deltaP `-1.0733` edge `0.2987` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.2048` n `43` status `ready` deltaP `27.8892` edge `0.0162` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `1.9207` n `132` status `ready` deltaP `24.3372` edge `0.4793` maxDD `-32.8525`
- `market_context_high->index_24h` score `1.7898` n `132` status `ready` deltaP `9.3434` edge `0.2097` maxDD `-4.1604`
- `news_risk_high->index_24h` score `1.7179` n `33` status `ready` deltaP `11.6162` edge `0.1076` maxDD `-1.3507`
- `news_risk_high->unknown_1h` score `1.4084` n `43` status `ready` deltaP `21.0451` edge `0.024` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
