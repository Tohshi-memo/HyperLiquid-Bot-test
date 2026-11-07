# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T15:22:28.757598+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4147`

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

- `market_context_high->unknown_4h` score `143.5986` n `37` status `ready` deltaP `-8.9692` edge `12.0711` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4008` n `37` status `ready` deltaP `36.9726` edge `0.0459` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.137` n `37` status `ready` deltaP `9.1601` edge `0.2463` maxDD `-2.3425`
- `market_context_high->index_4h` score `2.0268` n `37` status `ready` deltaP `26.5079` edge `0.0392` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.4332` n `53` status `ready` deltaP `7.3703` edge `0.0924` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8063` n `53` status `ready` deltaP `6.1465` edge `0.1363` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.6872` n `37` status `ready` deltaP `9.152` edge `0.0548` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.532` n `37` status `ready` deltaP `8.4197` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4194` n `37` status `ready` deltaP `10.9484` edge `0.0623` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.3904` n `53` status `ready` deltaP `11.4645` edge `0.0214` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2853` n `37` status `ready` deltaP `1.8005` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.1834` n `53` status `ready` deltaP `6.7086` edge `0.1456` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.135` n `37` status `ready` deltaP `9.3179` edge `0.0098` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0518` n `53` status `ready` deltaP `6.5289` edge `0.007` maxDD `-0.1772`
- `news_risk_high->index_1h` score `0.0374` n `53` status `ready` deltaP `7.0529` edge `0.0031` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `0.0082` n `37` status `ready` deltaP `3.4443` edge `0.0235` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0754` n `37` status `ready` deltaP `1.052` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2265` n `53` status `ready` deltaP `0.9745` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.2528` n `53` status `ready` deltaP `-3.1296` edge `0.0434` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.8853` n `37` status `ready` deltaP `19.813` edge `0.0824` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
