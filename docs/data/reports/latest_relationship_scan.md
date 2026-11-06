# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T21:52:27.094701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4126`

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

- `news_risk_high->equity_4h` score `1.42` n `83` status `ready` deltaP `12.5129` edge `0.1892` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6459` n `83` status `ready` deltaP `12.3457` edge `0.0193` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.316` n `83` status `ready` deltaP `12.1871` edge `0.0046` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.3038` n `83` status `ready` deltaP `5.4289` edge `0.0577` maxDD `-1.396`
- `news_risk_high->fx_4h` score `0.0158` n `83` status `ready` deltaP `6.6761` edge `0.0021` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.1832` n `83` status `ready` deltaP `0.499` edge `0.14` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.2509` n `83` status `ready` deltaP `0.9307` edge `0.0006` maxDD `-0.1179`
- `news_risk_high->metal_1h` score `-0.3386` n `83` status `ready` deltaP `-0.4455` edge `-0.0047` maxDD `-0.5256`
- `news_risk_high->fx_24h` score `-0.3697` n `83` status `ready` deltaP `-2.5725` edge `0.0306` maxDD `-0.2073`
- `news_risk_high->crypto_alt_1h` score `-0.8099` n `83` status `ready` deltaP `1.6431` edge `0.008` maxDD `-5.8225`
- `news_risk_high->crypto_major_1h` score `-0.8265` n `83` status `ready` deltaP `-2.7271` edge `0.0061` maxDD `-4.1772`
- `news_risk_high->crypto_major_4h` score `-0.9581` n `83` status `ready` deltaP `-1.473` edge `0.0556` maxDD `-9.1553`
- `news_risk_high->metal_4h` score `-1.1348` n `83` status `ready` deltaP `-2.7807` edge `-0.0364` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-1.8246` n `83` status `ready` deltaP `25.1571` edge `0.757` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-2.3443` n `83` status `ready` deltaP `-5.1168` edge `-0.0028` maxDD `-14.0916`
- `news_risk_high->commodity_1h` score `-2.8435` n `83` status `ready` deltaP `-17.0136` edge `-0.0058` maxDD `-1.7518`
- `news_risk_high->metal_24h` score `-3.0222` n `83` status `ready` deltaP `3.5017` edge `-0.2212` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.0188` n `83` status `ready` deltaP `-25.8889` edge `-0.0016` maxDD `-4.1899`
- `news_risk_high->commodity_24h` score `-9.3171` n `83` status `ready` deltaP `-26.055` edge `-0.0285` maxDD `-28.6046`
- `news_risk_high->crypto_major_24h` score `-11.5529` n `83` status `ready` deltaP `-23.0273` edge `0.0411` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
