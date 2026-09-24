# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T07:37:31.923854+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9897`

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

- `market_context_high->unknown_1h` score `66.1482` n `47` status `ready` deltaP `10.5651` edge `5.449` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `40.0826` n `46` status `ready` deltaP `27.423` edge `3.173` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `25.1245` n `46` status `ready` deltaP `22.3958` edge `1.9444` maxDD `0.0`
- `market_context_high->equity_24h` score `23.2044` n `46` status `ready` deltaP `24.8189` edge `1.7783` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.702` n `46` status `ready` deltaP `33.8466` edge `0.4249` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `6.3414` n `103` status `ready` deltaP `-0.268` edge `1.4345` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.8024` n `103` status `ready` deltaP `14.3841` edge `0.4041` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.723` n `103` status `ready` deltaP `18.3475` edge `0.329` maxDD `-2.619`
- `market_context_high->metal_24h` score `2.9052` n `46` status `ready` deltaP `27.8231` edge `0.08` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `2.8624` n `103` status `ready` deltaP `-2.8469` edge `0.9588` maxDD `-49.7699`
- `market_context_high->index_4h` score `2.7677` n `47` status `ready` deltaP `32.1971` edge `0.0314` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.2757` n `112` status `ready` deltaP `12.4466` edge `0.1557` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.0408` n `47` status `ready` deltaP `15.0103` edge `0.1118` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `1.8893` n `103` status `ready` deltaP `20.449` edge `0.139` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `1.8617` n `112` status `ready` deltaP `14.5424` edge `0.1017` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.616` n `103` status `ready` deltaP `23.5289` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.248` n `103` status `ready` deltaP `29.8375` edge `0.1242` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8744` n `47` status `ready` deltaP `13.7119` edge `0.0093` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.7689` n `47` status `ready` deltaP `10.1191` edge `0.0369` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.5833` n `112` status `ready` deltaP `14.4514` edge `0.0116` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
