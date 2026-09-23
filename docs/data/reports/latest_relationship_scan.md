# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T10:07:27.946056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_4h` score `46.8149` n `46` status `ready` deltaP `7.9268` edge `3.8484` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4718` n `46` status `ready` deltaP `13.7078` edge `2.3802` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6537` n `46` status `ready` deltaP `12.1453` edge `1.3169` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.2952` n `46` status `ready` deltaP `10.5903` edge `0.954` maxDD `0.0`
- `market_context_high->index_24h` score `5.6332` n `46` status `ready` deltaP `20.8258` edge `0.3393` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.7782` n `96` status `ready` deltaP `-9.0277` edge `1.1442` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.0797` n `96` status `ready` deltaP `33.1597` edge `0.2368` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9597` n `103` status `ready` deltaP `14.2316` edge `0.2095` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3043` n `103` status `ready` deltaP `9.0487` edge `0.2315` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.284` n `46` status `ready` deltaP `26.6702` edge `0.0259` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.8793` n `103` status `ready` deltaP `11.0618` edge `0.1319` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.6211` n `103` status `ready` deltaP `14.2056` edge `0.0839` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2799` n `103` status `ready` deltaP `19.7179` edge `0.0388` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1014` n `96` status `ready` deltaP `27.0833` edge `0.1196` maxDD `-1.7159`
- `market_context_high->equity_4h` score `0.9384` n `46` status `ready` deltaP `7.2243` edge `0.0607` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8976` n `46` status `ready` deltaP `7.8105` edge `0.047` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.7573` n `46` status `ready` deltaP `11.553` edge `0.0114` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5751` n `103` status `ready` deltaP `14.4541` edge `0.0109` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2495` n `103` status `ready` deltaP `8.2568` edge `0.0101` maxDD `-0.2147`
- `news_risk_high->metal_4h` score `0.1829` n `103` status `ready` deltaP `12.1359` edge `0.0383` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
