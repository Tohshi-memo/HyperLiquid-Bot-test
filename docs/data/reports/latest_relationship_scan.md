# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T22:37:24.935241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9868`

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

- `market_context_high->unknown_4h` score `25.2767` n `58` status `ready` deltaP `1.9922` edge `2.1081` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `12.5667` n `101` status `ready` deltaP `1.3734` edge `1.7239` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `7.7379` n `101` status `ready` deltaP `1.7584` edge `1.1212` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.3528` n `101` status `ready` deltaP `16.1751` edge `0.2925` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.45` n `101` status `ready` deltaP `15.0338` edge `0.1505` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.3842` n `101` status `ready` deltaP `17.3946` edge `0.2085` maxDD `-8.0625`
- `news_risk_high->commodity_24h` score `2.3427` n `101` status `ready` deltaP `29.794` edge `0.2323` maxDD `-3.4467`
- `market_context_high->crypto_major_24h` score `1.9306` n `48` status `ready` deltaP `1.9097` edge `0.9006` maxDD `-48.5989`
- `news_risk_high->crypto_major_1h` score `1.6527` n `101` status `ready` deltaP `16.2314` edge `0.0818` maxDD `-2.8494`
- `market_context_high->index_24h` score `1.42` n `48` status `ready` deltaP `-0.8681` edge `0.203` maxDD `-1.644`
- `market_context_high->equity_24h` score `1.3944` n `48` status `ready` deltaP `-4.8611` edge `0.4909` maxDD `-17.7117`
- `market_context_high->equity_1h` score `0.6174` n `58` status `ready` deltaP `4.362` edge `0.0477` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.4987` n `101` status `ready` deltaP `13.4004` edge `0.0124` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4944` n `58` status `ready` deltaP `8.1819` edge `0.0122` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4444` n `58` status `ready` deltaP `9.9732` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.4108` n `101` status `ready` deltaP `10.7748` edge `0.026` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2207` n `58` status `ready` deltaP `4.9505` edge `0.0162` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.1919` n `101` status `ready` deltaP `13.4403` edge `0.0318` maxDD `-2.0994`
- `market_context_high->metal_24h` score `0.1517` n `48` status `ready` deltaP `15.7986` edge `-0.0693` maxDD `-0.2042`
- `market_context_high->index_4h` score `0.0848` n `58` status `ready` deltaP `11.1228` edge `0.0004` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
