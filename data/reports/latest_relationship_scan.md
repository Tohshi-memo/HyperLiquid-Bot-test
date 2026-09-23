# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T07:52:34.576128+00:00`
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

- `market_context_high->unknown_4h` score `47.0836` n `46` status `ready` deltaP `7.7744` edge `3.8718` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.2467` n `46` status `ready` deltaP `13.5341` edge `2.3626` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6081` n `46` status `ready` deltaP `12.1453` edge `1.3131` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.2556` n `46` status `ready` deltaP `10.5903` edge `0.9507` maxDD `0.0`
- `market_context_high->index_24h` score `5.6356` n `46` status `ready` deltaP `20.8258` edge `0.3395` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.5531` n `96` status `ready` deltaP `-9.2014` edge `1.1266` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.3787` n `96` status `ready` deltaP `34.7222` edge `0.2513` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6673` n `103` status `ready` deltaP `13.6219` edge `0.1892` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1599` n `46` status `ready` deltaP `25.2982` edge `0.0247` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.1486` n `103` status `ready` deltaP `8.2865` edge `0.2236` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.7702` n `103` status `ready` deltaP `10.3133` edge `0.1278` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4209` n `103` status `ready` deltaP `13.008` edge `0.0752` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3868` n `103` status `ready` deltaP `20.785` edge `0.0406` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.0724` n `96` status `ready` deltaP `26.7361` edge `0.1182` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8329` n `46` status `ready` deltaP `7.2117` edge `0.0456` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7555` n `46` status `ready` deltaP `5.8524` edge `0.0546` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6567` n `46` status `ready` deltaP `10.3554` edge `0.011` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4649` n `103` status `ready` deltaP `13.2565` edge `0.0097` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2232` n `103` status `ready` deltaP `7.9574` edge `0.0099` maxDD `-0.2147`
- `market_context_high->fx_1h` score `0.1034` n `46` status `ready` deltaP `5.9945` edge `0.0043` maxDD `-0.1854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
