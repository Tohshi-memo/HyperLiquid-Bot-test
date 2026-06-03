# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T11:07:28.563664+00:00`
- Price records: `672`
- Market context records: `2758`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `5.9431` n `127` status `ready` deltaP `12.8664` edge `0.4423` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `4.2339` n `127` status `ready` deltaP `7.8398` edge `0.8399` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9835` n `143` status `ready` deltaP `6.5539` edge `0.1436` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1101` n `143` status `ready` deltaP `10.7038` edge `0.0269` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.098` n `143` status `ready` deltaP `3.6473` edge `0.0406` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1441` n `143` status `ready` deltaP `3.35` edge `0.0086` maxDD `-1.2855`
- `market_context_high->commodity_24h` score `-0.2835` n `127` status `ready` deltaP `7.4611` edge `0.2233` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5853` n `143` status `ready` deltaP `-1.096` edge `0.0029` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6734` n `143` status `ready` deltaP `5.8457` edge `0.0507` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6776` n `143` status `ready` deltaP `-0.5464` edge `-0.0079` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.77` n `143` status `ready` deltaP `-0.9506` edge `-0.0078` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9573` n `143` status `ready` deltaP `3.6473` edge `0.0399` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1476` n `143` status `ready` deltaP `-3.6367` edge `0.0119` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-1.1966` n `143` status `ready` deltaP `15.1437` edge `0.2334` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2283` n `143` status `ready` deltaP `-4.7075` edge `0.0069` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2354` n `127` status `ready` deltaP `0.3363` edge `-0.018` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.7142` n `143` status `ready` deltaP `-0.7728` edge `-0.0226` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0203` n `143` status `ready` deltaP `-0.9444` edge `-0.0241` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.43` n `143` status `ready` deltaP `-2.3389` edge `-0.0409` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.5858` n `143` status `ready` deltaP `5.3802` edge `0.1232` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
