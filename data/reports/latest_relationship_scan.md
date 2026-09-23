# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T20:22:49.496837+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9427`

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

- `market_context_high->unknown_1h` score `72.2011` n `47` status `ready` deltaP `9.8166` edge `5.9584` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `33.3556` n `46` status `ready` deltaP `19.6105` edge `2.6645` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.1054` n `46` status `ready` deltaP `17.0064` edge `1.4888` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `16.3911` n `46` status `ready` deltaP `14.5833` edge `1.2687` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.662` n `96` status `ready` deltaP `-3.125` edge `1.4285` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.4542` n `46` status `ready` deltaP `26.0341` edge `0.373` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.4428` n `103` status `ready` deltaP `16.9755` edge `0.3148` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.2876` n `103` status `ready` deltaP `12.5548` edge `0.3734` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `3.5001` n `96` status `ready` deltaP `-5.2084` edge `0.8145` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.796` n `96` status `ready` deltaP `26.5625` edge `0.1738` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.4526` n `103` status `ready` deltaP `13.008` edge `0.1667` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.3691` n `47` status `ready` deltaP `28.2337` edge `0.0246` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0193` n `103` status `ready` deltaP `15.7026` edge `0.1071` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4308` n `103` status `ready` deltaP `21.3948` edge `0.0402` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2218` n `96` status `ready` deltaP `28.9931` edge `0.1223` maxDD `-1.7159`
- `market_context_high->metal_24h` score `1.1234` n `46` status `ready` deltaP `20.0106` edge `-0.0164` maxDD `-0.2042`
- `market_context_high->equity_4h` score `1.0274` n `47` status `ready` deltaP `8.9128` edge `0.068` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6852` n `47` status `ready` deltaP `11.6161` edge `0.0075` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6194` n `103` status `ready` deltaP `15.2026` edge `0.0096` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.5612` n `96` status `ready` deltaP `16.8403` edge `0.0441` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
