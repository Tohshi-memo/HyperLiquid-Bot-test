# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T01:27:49.124683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9740`

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

- `market_context_high->unknown_4h` score `45.8898` n `46` status `ready` deltaP `7.0122` edge `3.7774` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6751` n `46` status `ready` deltaP `13.5341` edge `2.3983` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.4257` n `46` status `ready` deltaP `12.1453` edge `1.2979` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.0116` n `46` status `ready` deltaP `10.5903` edge `1.0137` maxDD `0.0`
- `market_context_high->index_24h` score `5.5251` n `46` status `ready` deltaP `19.6105` edge `0.3384` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9815` n `96` status `ready` deltaP `-9.2014` edge `1.1623` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.6299` n `96` status `ready` deltaP `35.4167` edge `0.2676` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9096` n `97` status `ready` deltaP `14.3701` edge `0.2044` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3386` n `97` status `ready` deltaP `9.4921` edge `0.2314` maxDD `-5.9838`
- `market_context_high->index_4h` score `1.9361` n `46` status `ready` deltaP `23.0116` edge `0.0213` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.7887` n `97` status `ready` deltaP `10.3216` edge `0.1198` maxDD `-1.1645`
- `news_risk_high->fx_4h` score `1.3815` n `97` status `ready` deltaP `20.5086` edge `0.042` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `1.3385` n `97` status `ready` deltaP `12.5672` edge `0.0671` maxDD `-1.8141`
- `news_risk_high->fx_24h` score `0.8264` n `96` status `ready` deltaP `23.2639` edge `0.1098` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.6409` n `97` status `ready` deltaP `15.2309` edge `0.0112` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6363` n `46` status `ready` deltaP `5.7147` edge `0.0392` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.61` n `46` status `ready` deltaP `9.9063` edge `0.0101` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.5347` n `46` status `ready` deltaP `18.6217` edge `-0.0562` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.3393` n `46` status `ready` deltaP `3.2609` edge `0.0372` maxDD `-0.4529`
- `news_risk_high->fx_1h` score `0.3311` n `97` status `ready` deltaP `9.0962` edge `0.0113` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
