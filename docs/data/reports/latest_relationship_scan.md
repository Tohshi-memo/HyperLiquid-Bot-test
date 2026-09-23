# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T07:37:36.716927+00:00`
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

- `market_context_high->unknown_4h` score `47.0896` n `46` status `ready` deltaP `7.7744` edge `3.8723` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.2515` n `46` status `ready` deltaP `13.5341` edge `2.363` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6117` n `46` status `ready` deltaP `12.1453` edge `1.3134` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.2628` n `46` status `ready` deltaP `10.5903` edge `0.9513` maxDD `0.0`
- `market_context_high->index_24h` score `5.6368` n `46` status `ready` deltaP `20.8258` edge `0.3396` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.5579` n `96` status `ready` deltaP `-9.2014` edge `1.127` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.3871` n `96` status `ready` deltaP `34.7222` edge `0.252` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6251` n `103` status `ready` deltaP `13.4694` edge `0.1867` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1587` n `46` status `ready` deltaP `25.2982` edge `0.0246` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.1136` n `103` status `ready` deltaP `8.1341` edge `0.2217` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.7654` n `103` status `ready` deltaP `10.3133` edge `0.1274` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4173` n `103` status `ready` deltaP `13.008` edge `0.0749` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4015` n `103` status `ready` deltaP `20.9375` edge `0.0408` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.0618` n `96` status `ready` deltaP `26.5625` edge `0.118` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8329` n `46` status `ready` deltaP `7.2117` edge `0.0456` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7483` n `46` status `ready` deltaP `5.8524` edge `0.054` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6555` n `46` status `ready` deltaP `10.3554` edge `0.0109` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4637` n `103` status `ready` deltaP `13.2565` edge `0.0096` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2244` n `103` status `ready` deltaP `7.9574` edge `0.01` maxDD `-0.2147`
- `market_context_high->fx_1h` score `0.1046` n `46` status `ready` deltaP `5.9945` edge `0.0044` maxDD `-0.1854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
