# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T13:22:32.663989+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `46.8766` n `46` status `ready` deltaP `7.3171` edge `3.8576` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.2948` n `46` status `ready` deltaP `16.4855` edge `2.5136` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.4636` n `46` status `ready` deltaP `15.625` edge `1.2678` maxDD `0.0`
- `market_context_high->equity_24h` score `16.3287` n `46` status `ready` deltaP `12.4925` edge `1.2875` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.55` n `46` status `ready` deltaP `20.1314` edge `0.337` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `3.5776` n `101` status `ready` deltaP `-8.8697` edge `1.0431` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.2623` n `101` status `ready` deltaP `39.169` edge `0.2877` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.2817` n `101` status `ready` deltaP `11.9068` edge `0.2317` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.1107` n `101` status `ready` deltaP `13.2374` edge `0.1342` maxDD `-2.058`
- `market_context_high->index_4h` score `1.9833` n `46` status `ready` deltaP `23.3165` edge `0.0232` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.6283` n `101` status `ready` deltaP `14.6507` edge `0.1638` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.4513` n `101` status `ready` deltaP `14.8841` edge `0.074` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.111` n `46` status `ready` deltaP `7.9865` edge `0.07` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.0538` n `101` status `ready` deltaP `17.1773` edge `0.0369` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.9744` n `46` status `ready` deltaP `7.8105` edge `0.0534` maxDD `-0.2751`
- `market_context_high->metal_24h` score `0.9081` n `46` status `ready` deltaP `21.3995` edge `-0.0436` maxDD `-0.2042`
- `market_context_high->crypto_alt_4h` score `0.7262` n `46` status `ready` deltaP `7.602` edge `0.0693` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.707` n `46` status `ready` deltaP `10.9542` edge `0.0112` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5909` n `101` status `ready` deltaP `14.4483` edge `0.0131` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.3911` n `101` status `ready` deltaP `17.5897` edge `0.0173` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
