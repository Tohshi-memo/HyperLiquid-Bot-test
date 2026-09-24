# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T05:07:35.572490+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.3126` n `47` status `ready` deltaP `10.8645` edge `5.9607` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `38.3753` n `46` status `ready` deltaP `25.6869` edge `3.0423` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `23.1088` n `46` status `ready` deltaP `20.6597` edge `1.788` maxDD `0.0`
- `market_context_high->equity_24h` score `22.1631` n `46` status `ready` deltaP `23.0828` edge `1.7031` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.4059` n `46` status `ready` deltaP `32.1105` edge `0.4118` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9743` n `103` status `ready` deltaP `14.6889` edge `0.4164` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.8171` n `103` status `ready` deltaP `18.8048` edge `0.3338` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `4.6341` n `103` status `ready` deltaP `-2.0041` edge `1.3038` maxDD `-63.6743`
- `market_context_high->index_4h` score `2.6134` n `47` status `ready` deltaP `30.6727` edge `0.0287` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.6012` n `103` status `ready` deltaP `14.0559` edge `0.1721` maxDD `-1.5895`
- `market_context_high->metal_24h` score `2.5275` n `46` status `ready` deltaP `26.087` edge `0.0601` maxDD `-0.2042`
- `news_risk_high->commodity_24h` score `2.2166` n `103` status `ready` deltaP `22.1851` edge `0.1547` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.096` n `103` status `ready` deltaP `16.3014` edge `0.1095` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.7376` n `47` status `ready` deltaP `13.4859` edge `0.0967` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.6002` n `103` status `ready` deltaP `23.3765` edge `0.0411` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2257` n `103` status `ready` deltaP `29.6639` edge `0.1225` maxDD `-1.7159`
- `news_risk_high->crypto_alt_24h` score `0.8467` n `103` status `ready` deltaP `-4.583` edge `0.8024` maxDD `-49.7699`
- `market_context_high->index_1h` score `0.8409` n `47` status `ready` deltaP `13.4125` edge `0.0085` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.6694` n `47` status `ready` deltaP `9.5203` edge `0.0326` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.6649` n `103` status `ready` deltaP `15.502` edge `0.0114` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
