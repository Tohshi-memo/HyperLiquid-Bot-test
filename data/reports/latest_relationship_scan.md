# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T15:52:33.705358+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9864`

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

- `market_context_high->unknown_1h` score `80.4296` n `47` status `ready` deltaP `9.2178` edge `6.6481` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `30.9744` n `46` status `ready` deltaP `16.4855` edge `2.4869` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.5378` n `46` status `ready` deltaP `13.8814` edge `1.379` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.3067` n `46` status `ready` deltaP `11.4583` edge `1.0325` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `6.2808` n `96` status `ready` deltaP `-6.25` edge `1.2509` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.9378` n `46` status `ready` deltaP `22.9091` edge `0.3508` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `3.6294` n `103` status `ready` deltaP `15.2987` edge `0.2582` maxDD `-2.619`
- `news_risk_high->commodity_24h` score `3.2131` n `96` status `ready` deltaP `29.1667` edge `0.1912` maxDD `-2.431`
- `news_risk_high->crypto_alt_4h` score `2.9357` n `103` status `ready` deltaP `10.1158` edge `0.277` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.5116` n `46` status `ready` deltaP `29.1092` edge `0.0286` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `2.1888` n `103` status `ready` deltaP `11.9601` edge `0.1517` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.867` n `103` status `ready` deltaP `15.1038` edge `0.0984` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3375` n `46` status `ready` deltaP `9.6633` edge `0.0777` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2263` n `103` status `ready` deltaP `19.1082` edge `0.0384` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1673` n `96` status `ready` deltaP `28.125` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.6828` n `47` status `ready` deltaP `11.4664` edge `0.0083` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6686` n `103` status `ready` deltaP `15.3523` edge `0.0127` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.4522` n `46` status `ready` deltaP `16.8856` edge `-0.0515` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `0.4157` n `96` status `ready` deltaP `-8.3334` edge `0.5783` maxDD `-32.7147`
- `market_context_high->equity_1h` score `0.39` n `47` status `ready` deltaP `7.1251` edge `0.0254` maxDD `-1.5655`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
