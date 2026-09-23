# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T14:52:31.304879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9888`

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

- `market_context_high->unknown_1h` score `80.2724` n `47` status `ready` deltaP `9.2178` edge `6.635` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `30.4988` n `46` status `ready` deltaP `15.7911` edge `2.4519` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.3238` n `46` status `ready` deltaP `13.1869` edge `1.3658` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.7831` n `46` status `ready` deltaP `10.7639` edge `0.9935` maxDD `0.0`
- `market_context_high->unknown_4h` score `11.2144` n `46` status `ready` deltaP `7.7744` edge `0.8827` maxDD `0.0`
- `market_context_high->index_24h` score `5.8499` n `46` status `ready` deltaP `22.2147` edge `0.3481` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.8053` n `96` status `ready` deltaP `-6.9444` edge `1.2159` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `3.3683` n `103` status `ready` deltaP `14.6889` edge `0.2405` maxDD `-2.619`
- `news_risk_high->commodity_24h` score `3.313` n `96` status `ready` deltaP `29.8611` edge `0.1949` maxDD `-2.431`
- `news_risk_high->crypto_alt_4h` score `2.6001` n `103` status `ready` deltaP `9.506` edge `0.2531` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.5248` n `46` status `ready` deltaP `29.1092` edge `0.0297` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `2.1312` n `103` status `ready` deltaP `11.9601` edge `0.1469` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.8106` n `103` status `ready` deltaP `14.8044` edge `0.0957` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.4011` n `46` status `ready` deltaP `9.6633` edge `0.083` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.1861` n `103` status `ready` deltaP `18.6509` edge `0.0381` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1665` n `96` status `ready` deltaP `28.125` edge `0.121` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7103` n `47` status `ready` deltaP `11.7658` edge `0.0086` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6817` n `103` status `ready` deltaP `15.502` edge `0.0128` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.4607` n `47` status `ready` deltaP `7.5742` edge `0.0283` maxDD `-1.5655`
- `market_context_high->metal_24h` score `0.3427` n `46` status `ready` deltaP `16.1912` edge `-0.056` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
