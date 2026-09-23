# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T04:07:28.579110+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9794`

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

- `market_context_high->unknown_4h` score `46.2526` n `46` status `ready` deltaP `7.3171` edge `3.8056` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5659` n `46` status `ready` deltaP `13.5341` edge `2.3892` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6657` n `46` status `ready` deltaP `12.1453` edge `1.3179` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.75` n `46` status `ready` deltaP `10.5903` edge `0.9919` maxDD `0.0`
- `market_context_high->index_24h` score `5.6524` n `46` status `ready` deltaP `20.8258` edge `0.3409` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.8723` n `96` status `ready` deltaP `-9.2014` edge `1.1532` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.4946` n `96` status `ready` deltaP `34.8958` edge `0.2598` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.726` n `97` status `ready` deltaP `13.4555` edge `0.1952` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.1478` n `97` status `ready` deltaP `8.5774` edge `0.2216` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.0929` n `46` status `ready` deltaP `24.536` edge `0.0242` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.8865` n `103` status `ready` deltaP `11.0618` edge `0.1325` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4593` n `103` status `ready` deltaP `13.3074` edge `0.0764` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3985` n `97` status `ready` deltaP `20.661` edge `0.0424` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.9102` n `96` status `ready` deltaP `24.3056` edge `0.1136` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7814` n `46` status `ready` deltaP `6.6129` edge `0.0453` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6675` n `46` status `ready` deltaP `10.5051` edge `0.0109` maxDD `-0.0249`
- `market_context_high->equity_4h` score `0.6439` n `46` status `ready` deltaP `4.9377` edge `0.0514` maxDD `-0.4529`
- `news_risk_high->metal_1h` score `0.4433` n `103` status `ready` deltaP `13.1068` edge `0.0089` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.4347` n `97` status `ready` deltaP `13.6928` edge `0.0407` maxDD `-1.9941`
- `market_context_high->metal_24h` score `0.3696` n `46` status `ready` deltaP `17.2328` edge `-0.0607` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
