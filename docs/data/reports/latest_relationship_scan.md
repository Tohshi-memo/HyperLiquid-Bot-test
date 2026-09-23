# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T16:07:40.418289+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9846`

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

- `market_context_high->unknown_1h` score `80.5604` n `47` status `ready` deltaP `9.2178` edge `6.659` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `31.1059` n `46` status `ready` deltaP `16.6591` edge `2.4967` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.6045` n `46` status `ready` deltaP `14.055` edge `1.3834` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.4682` n `46` status `ready` deltaP `11.6319` edge `1.0448` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `6.4123` n `96` status `ready` deltaP `-6.0764` edge `1.2607` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.9625` n `46` status `ready` deltaP `23.0828` edge `0.3517` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `3.7088` n `103` status `ready` deltaP `15.4511` edge `0.2638` maxDD `-2.619`
- `news_risk_high->commodity_24h` score `3.1872` n `96` status `ready` deltaP `28.9931` edge `0.1902` maxDD `-2.431`
- `news_risk_high->crypto_alt_4h` score `3.0415` n `103` status `ready` deltaP `10.2682` edge `0.2848` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.5104` n `46` status `ready` deltaP `29.1092` edge `0.0285` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `2.2296` n `103` status `ready` deltaP `12.1098` edge `0.1541` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.8946` n `103` status `ready` deltaP `15.2535` edge `0.0997` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3351` n `46` status `ready` deltaP `9.6633` edge `0.0775` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2397` n `103` status `ready` deltaP `19.2606` edge `0.0385` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1673` n `96` status `ready` deltaP `28.125` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.6828` n `47` status `ready` deltaP `11.4664` edge `0.0083` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6698` n `103` status `ready` deltaP `15.3523` edge `0.0128` maxDD `-0.7468`
- `news_risk_high->crypto_alt_24h` score `0.5772` n `96` status `ready` deltaP `-8.1598` edge `0.5906` maxDD `-32.7147`
- `market_context_high->metal_24h` score `0.4805` n `46` status `ready` deltaP `17.0592` edge `-0.0503` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.3961` n `47` status `ready` deltaP `7.1251` edge `0.0258` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
