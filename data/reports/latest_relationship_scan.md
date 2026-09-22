# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T13:37:32.896603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9930`

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

- `market_context_high->unknown_4h` score `46.831` n `46` status `ready` deltaP `7.3171` edge `3.8538` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.1813` n `46` status `ready` deltaP `16.3119` edge `2.5053` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.3681` n `46` status `ready` deltaP `15.4514` edge `1.261` maxDD `0.0`
- `market_context_high->equity_24h` score `16.2812` n `46` status `ready` deltaP `12.3189` edge `1.2847` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5452` n `46` status `ready` deltaP `20.1314` edge `0.3366` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `3.4642` n `101` status `ready` deltaP `-9.0433` edge `1.0348` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.2662` n `101` status `ready` deltaP `39.169` edge `0.2882` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.2865` n `101` status `ready` deltaP `11.9068` edge `0.2321` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.0855` n `101` status `ready` deltaP `13.0877` edge `0.1331` maxDD `-2.058`
- `market_context_high->index_4h` score `1.9675` n `46` status `ready` deltaP `23.1641` edge `0.0229` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.6113` n `101` status `ready` deltaP `14.4983` edge `0.1634` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.4249` n `101` status `ready` deltaP `14.7344` edge `0.0728` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.0724` n `46` status `ready` deltaP `7.8341` edge `0.0678` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.0538` n `101` status `ready` deltaP `17.1773` edge `0.0369` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.942` n `46` status `ready` deltaP `7.6608` edge `0.0517` maxDD `-0.2751`
- `market_context_high->metal_24h` score `0.9292` n `46` status `ready` deltaP `21.5731` edge `-0.043` maxDD `-0.2042`
- `market_context_high->crypto_alt_4h` score `0.7309` n `46` status `ready` deltaP `7.602` edge `0.0697` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.6926` n `46` status `ready` deltaP `10.8045` edge `0.011` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5753` n `101` status `ready` deltaP `14.2986` edge `0.0128` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.4048` n `101` status `ready` deltaP `17.7633` edge `0.0179` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
