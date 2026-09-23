# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T21:52:31.149065+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9826`

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

- `market_context_high->unknown_1h` score `72.2022` n `47` status `ready` deltaP `10.2657` edge `5.9555` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `34.1133` n `46` status `ready` deltaP `20.6522` edge `2.7207` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.6879` n `46` status `ready` deltaP `18.048` edge `1.5304` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `17.4476` n `46` status `ready` deltaP `15.625` edge `1.3498` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.4572` n `97` status `ready` deltaP `-2.8351` edge `1.4095` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.6372` n `46` status `ready` deltaP `27.0758` edge `0.3813` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.5972` n `103` status `ready` deltaP `13.4694` edge `0.3931` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5334` n `103` status `ready` deltaP `17.4328` edge `0.3193` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `3.5569` n `97` status `ready` deltaP `-4.9936` edge `0.8178` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.702` n `97` status `ready` deltaP `25.7785` edge `0.1712` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.449` n `103` status `ready` deltaP `13.008` edge `0.1664` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4102` n `47` status `ready` deltaP `28.5385` edge `0.026` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9593` n `103` status `ready` deltaP `15.4032` edge `0.1041` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.482` n `103` status `ready` deltaP `22.0045` edge `0.0404` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.3748` n `46` status `ready` deltaP `21.0523` edge `-0.0024` maxDD `-0.2042`
- `market_context_high->equity_4h` score `1.1879` n `47` status `ready` deltaP `9.675` edge `0.0763` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.0996` n `97` status `ready` deltaP `27.4485` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7235` n `47` status `ready` deltaP `12.0652` edge `0.0077` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5811` n `103` status `ready` deltaP `14.7535` edge `0.0094` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.5556` n `97` status `ready` deltaP `17.1302` edge `0.0488` maxDD `-3.0086`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
