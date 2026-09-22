# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T13:52:29.182905+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9690`

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

- `market_context_high->unknown_4h` score `46.7926` n `46` status `ready` deltaP `7.3171` edge `3.8506` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.087` n `46` status `ready` deltaP `16.1383` edge `2.4986` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.287` n `46` status `ready` deltaP `15.2778` edge `1.2554` maxDD `0.0`
- `market_context_high->equity_24h` score `16.256` n `46` status `ready` deltaP `12.3189` edge `1.2826` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5416` n `46` status `ready` deltaP `20.1314` edge `0.3363` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `3.3699` n `101` status `ready` deltaP `-9.2169` edge `1.0281` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.2693` n `101` status `ready` deltaP `39.169` edge `0.2886` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.2865` n `101` status `ready` deltaP `11.9068` edge `0.2321` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.0459` n `101` status `ready` deltaP `12.938` edge `0.1308` maxDD `-2.058`
- `market_context_high->index_4h` score `1.9505` n `46` status `ready` deltaP `23.0116` edge `0.0225` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.6053` n `101` status `ready` deltaP `14.4983` edge `0.1629` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.3782` n `101` status `ready` deltaP `14.5847` edge `0.0699` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `1.0538` n `101` status `ready` deltaP `17.1773` edge `0.0369` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.029` n `46` status `ready` deltaP `7.6816` edge `0.0652` maxDD `-0.4529`
- `market_context_high->metal_24h` score `0.9479` n `46` status `ready` deltaP `21.7467` edge `-0.0426` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.894` n `46` status `ready` deltaP `7.5111` edge `0.0487` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.7309` n `46` status `ready` deltaP `7.602` edge `0.0697` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.6746` n `46` status `ready` deltaP `10.6548` edge `0.0105` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5586` n `101` status `ready` deltaP `14.1489` edge `0.0124` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.417` n `101` status `ready` deltaP `17.9369` edge `0.0183` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
