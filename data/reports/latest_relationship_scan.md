# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T19:22:36.352620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `45.8562` n `46` status `ready` deltaP `7.0122` edge `3.7746` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4856` n `46` status `ready` deltaP `12.6661` edge `2.3883` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2457` n `46` status `ready` deltaP `12.1453` edge `1.2829` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.1528` n `46` status `ready` deltaP `11.8056` edge `1.1007` maxDD `0.0`
- `market_context_high->index_24h` score `5.545` n `46` status `ready` deltaP `19.7841` edge `0.3389` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.3424` n `96` status `ready` deltaP `39.5833` edge `0.2992` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.7921` n `96` status `ready` deltaP `-10.0694` edge `1.1523` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `3.0417` n `96` status `ready` deltaP `15.0915` edge `0.2106` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.0284` n `96` status `ready` deltaP `11.8902` edge `0.2729` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.2558` n `96` status `ready` deltaP `12.7308` edge `0.1385` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8668` n `46` status `ready` deltaP `22.2494` edge `0.0206` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5721` n `96` status `ready` deltaP `14.0781` edge `0.0765` maxDD `-1.8141`
- `news_risk_high->crypto_alt_24h` score `1.2619` n `96` status `ready` deltaP `-7.9861` edge `0.6465` maxDD `-32.7147`
- `news_risk_high->fx_4h` score `1.1832` n `96` status `ready` deltaP `18.4197` edge `0.0394` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.0731` n `46` status `ready` deltaP `22.4412` edge `-0.0368` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.7298` n `46` status `ready` deltaP `6.6129` edge `0.041` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6303` n `46` status `ready` deltaP `10.2057` edge `0.0098` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6113` n `96` status `ready` deltaP `14.8765` edge `0.0111` maxDD `-0.7468`
- `news_risk_high->fx_24h` score `0.5389` n `96` status `ready` deltaP `19.7917` edge `0.0961` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `0.5285` n `96` status `ready` deltaP `19.2709` edge `0.0237` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
