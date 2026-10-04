# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T15:52:36.273841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5032`

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

- `market_context_high->unknown_1h` score `96.1184` n `97` status `ready` deltaP `-0.6096` edge `8.0554` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `89.3199` n `93` status `ready` deltaP `3.5683` edge `7.4507` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.5939` n `65` status `ready` deltaP `37.5821` edge `0.6526` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `10.0244` n `46` status `ready` deltaP `26.0945` edge `0.7887` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `9.9007` n `46` status `ready` deltaP `32.5332` edge `0.6734` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.1105` n `65` status `ready` deltaP `23.5337` edge `0.529` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.4101` n `65` status `ready` deltaP `24.5122` edge `0.5885` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.1474` n `93` status `ready` deltaP `22.6938` edge `0.348` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.9029` n `65` status `ready` deltaP `26.7361` edge `0.147` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.826` n `65` status `ready` deltaP `25.9123` edge `0.2071` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1684` n `65` status `ready` deltaP `34.5052` edge `0.0602` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8717` n `65` status `ready` deltaP `12.4113` edge `0.1921` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6134` n `65` status `ready` deltaP `22.5845` edge `0.1088` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1585` n `65` status `ready` deltaP `26.5154` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1332` n `97` status `ready` deltaP `15.3297` edge `0.1206` maxDD `-2.2692`
- `market_context_high->crypto_alt_4h` score `1.6064` n `93` status `ready` deltaP `5.8025` edge `0.2741` maxDD `-7.6465`
- `market_context_high->equity_24h` score `1.5692` n `46` status `ready` deltaP `3.6005` edge `0.2059` maxDD `-6.264`
- `market_context_high->fx_4h` score `1.5348` n `93` status `ready` deltaP `26.5752` edge `0.0264` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.5199` n `65` status `ready` deltaP `5.0184` edge `0.1451` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3622` n `46` status `ready` deltaP `25.536` edge `0.1062` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
