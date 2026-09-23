# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T19:07:34.764190+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9883`

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

- `market_context_high->unknown_1h` score `83.0839` n `47` status `ready` deltaP `9.8166` edge `6.8653` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `32.7353` n `46` status `ready` deltaP `18.7425` edge `2.6186` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.5763` n `46` status `ready` deltaP `16.1383` edge `1.4505` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.5248` n `46` status `ready` deltaP `13.7153` edge `1.2023` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.0418` n `96` status `ready` deltaP `-3.993` edge `1.3826` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.2888` n `46` status `ready` deltaP `25.1661` edge `0.365` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.3644` n `103` status `ready` deltaP `16.6706` edge `0.3103` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.0178` n `103` status `ready` deltaP `11.7926` edge `0.356` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `2.9506` n `96` status `ready` deltaP `27.4306` edge `0.1809` maxDD `-2.431`
- `news_risk_high->crypto_alt_24h` score `2.6339` n `96` status `ready` deltaP `-6.0764` edge `0.7481` maxDD `-32.7147`
- `news_risk_high->crypto_alt_1h` score `2.3639` n `103` status `ready` deltaP `12.5589` edge `0.1623` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.2829` n `47` status `ready` deltaP `27.4715` edge `0.0225` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0241` n `103` status `ready` deltaP `15.8523` edge `0.1065` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3931` n `103` status `ready` deltaP `20.9375` edge `0.0401` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2218` n `96` status `ready` deltaP `28.9931` edge `0.1223` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.8956` n `46` status `ready` deltaP `19.1426` edge `-0.0296` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.8272` n `47` status `ready` deltaP `8.1506` edge `0.0564` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6408` n `47` status `ready` deltaP `11.167` edge `0.0068` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5643` n `103` status `ready` deltaP `14.6038` edge `0.009` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.4131` n `96` status `ready` deltaP `15.9723` edge `0.0309` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
