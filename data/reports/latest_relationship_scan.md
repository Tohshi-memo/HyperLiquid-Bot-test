# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T14:22:37.779028+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9888`

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

- `market_context_high->unknown_1h` score `80.3144` n `47` status `ready` deltaP `9.2178` edge `6.6385` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `30.2719` n `46` status `ready` deltaP `15.4439` edge `2.4353` maxDD `-0.5817`
- `market_context_high->unknown_4h` score `30.0893` n `46` status `ready` deltaP `7.9268` edge `2.4546` maxDD `0.0`
- `market_context_high->equity_24h` score `17.1856` n `46` status `ready` deltaP `12.8397` edge `1.3566` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.5959` n `46` status `ready` deltaP `10.7639` edge `0.9779` maxDD `0.0`
- `market_context_high->index_24h` score `5.8005` n `46` status `ready` deltaP `21.8675` edge `0.3463` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.5783` n `96` status `ready` deltaP `-7.2916` edge `1.1993` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.3708` n `96` status `ready` deltaP `30.2083` edge `0.1974` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `3.2541` n `103` status `ready` deltaP `14.5365` edge `0.232` maxDD `-2.619`
- `market_context_high->index_4h` score `2.5212` n `46` status `ready` deltaP `29.1092` edge `0.0294` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.4511` n `103` status `ready` deltaP `9.3536` edge `0.2417` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.0292` n `103` status `ready` deltaP `11.8104` edge `0.1394` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.7063` n `103` status `ready` deltaP `14.505` edge `0.089` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3831` n `46` status `ready` deltaP `9.6633` edge `0.0815` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2007` n `103` status `ready` deltaP `18.8033` edge `0.0383` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1575` n `96` status `ready` deltaP `27.9514` edge `0.121` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.6804` n `47` status `ready` deltaP `11.4664` edge `0.0081` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6698` n `103` status `ready` deltaP `15.3523` edge `0.0128` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.4152` n `47` status `ready` deltaP `7.2748` edge `0.0265` maxDD `-1.5655`
- `market_context_high->metal_24h` score `0.2861` n `46` status `ready` deltaP `15.8439` edge `-0.0584` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
