# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T18:07:21.038963+00:00`
- Price records: `672`
- Market context records: `1654`
- Flow alert records: `6671`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `9.6388` n `169` status `ready` deltaP `28.4147` edge `0.8564` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.2393` n `189` status `ready` deltaP `22.0193` edge `0.4729` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7629` n `169` status `ready` deltaP `20.4111` edge `0.3153` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.4599` n `189` status `ready` deltaP `18.0112` edge `0.3558` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.8092` n `189` status `ready` deltaP `12.2273` edge `0.1787` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.6785` n `169` status `ready` deltaP `19.4283` edge `0.5002` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.6708` n `169` status `ready` deltaP `25.2277` edge `0.7463` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.5044` n `169` status `ready` deltaP `25.882` edge `1.0504` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.4154` n `199` status `ready` deltaP `5.9068` edge `0.0976` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.2974` n `199` status `ready` deltaP `1.309` edge `0.034` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.4053` n `189` status `ready` deltaP `0.8915` edge `0.051` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.4882` n `169` status `ready` deltaP `6.214` edge `0.0228` maxDD `-1.3925`
- `market_context_high->crypto_major_1h` score `-0.494` n `199` status `ready` deltaP `1.9724` edge `0.0509` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.5135` n `199` status `ready` deltaP `-1.2999` edge `0.006` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5188` n `199` status `ready` deltaP `-0.0271` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.8158` n `199` status `ready` deltaP `3.6297` edge `0.0048` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8558` n `199` status `ready` deltaP `1.4165` edge `-0.006` maxDD `-6.7191`
- `market_context_high->metal_4h` score `-1.3651` n `189` status `ready` deltaP `8.299` edge `0.1001` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.9933` n `189` status `ready` deltaP `-8.9875` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.6038` n `189` status `ready` deltaP `10.9807` edge `-0.1464` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
