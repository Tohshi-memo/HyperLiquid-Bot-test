# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T13:37:33.739090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9786`

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

- `market_context_high->unknown_4h` score `48.5309` n `46` status `ready` deltaP `7.9268` edge `3.9914` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.9794` n `46` status `ready` deltaP `14.923` edge `2.4144` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.9796` n `46` status `ready` deltaP `12.3189` edge `1.3429` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.3672` n `46` status `ready` deltaP `10.5903` edge `0.96` maxDD `0.0`
- `market_context_high->index_24h` score `5.7276` n `46` status `ready` deltaP `21.3466` edge `0.3437` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.2858` n `96` status `ready` deltaP `-7.8125` edge `1.1784` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.4725` n `96` status `ready` deltaP `30.7292` edge `0.2024` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `3.1313` n `103` status `ready` deltaP `14.2316` edge `0.2238` maxDD `-2.619`
- `market_context_high->index_4h` score `2.4848` n `46` status `ready` deltaP `28.8043` edge `0.0284` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.3043` n `103` status `ready` deltaP `9.0487` edge `0.2315` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9716` n `103` status `ready` deltaP `11.6607` edge `0.1356` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.6739` n `103` status `ready` deltaP `14.505` edge `0.0863` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.2987` n `46` status `ready` deltaP `9.3585` edge `0.0765` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2409` n `103` status `ready` deltaP `19.2606` edge `0.0386` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1575` n `96` status `ready` deltaP `27.9514` edge `0.121` maxDD `-1.7159`
- `market_context_high->equity_1h` score `1.0067` n `46` status `ready` deltaP `8.4093` edge `0.0521` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.8495` n `46` status `ready` deltaP `12.6009` edge `0.0121` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6182` n `103` status `ready` deltaP `14.9032` edge `0.0115` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.2442` n `103` status `ready` deltaP `12.7457` edge `0.0421` maxDD `-1.9941`
- `news_risk_high->fx_1h` score `0.2256` n `103` status `ready` deltaP `7.9574` edge `0.0101` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
