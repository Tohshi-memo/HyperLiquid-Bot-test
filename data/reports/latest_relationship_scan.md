# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T09:07:32.945665+00:00`
- Price records: `672`
- Market context records: `8181`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8660.5611` n `42` status `ready` deltaP `36.9792` edge `721.4669` maxDD `0.0`
- `market_context_high->equity_24h` score `19.3553` n `50` status `ready` deltaP `43.375` edge `1.4148` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.8288` n `51` status `ready` deltaP `39.5654` edge `0.5743` maxDD `-0.52`
- `market_context_high->metal_24h` score `8.4541` n `50` status `ready` deltaP `43.5764` edge `0.414` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.212` n `47` status `ready` deltaP `30.3872` edge `0.5111` maxDD `-1.3479`
- `market_context_high->index_4h` score `4.0941` n `51` status `ready` deltaP `36.6691` edge `0.101` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.4287` n `50` status `ready` deltaP `25.6048` edge `0.1459` maxDD `-1.1366`
- `market_context_high->crypto_alt_24h` score `3.36` n `50` status `ready` deltaP `8.0625` edge `0.6833` maxDD `-15.1696`
- `news_risk_high->crypto_major_4h` score `3.2797` n `47` status `ready` deltaP `17.7932` edge `0.3634` maxDD `-2.2569`
- `market_context_high->equity_1h` score `3.0084` n `51` status `ready` deltaP `16.2323` edge `0.1628` maxDD `-0.6254`
- `news_risk_high->index_4h` score `2.7678` n `47` status `ready` deltaP `23.2356` edge `0.0948` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.6089` n `51` status `ready` deltaP `27.191` edge `0.0686` maxDD `-0.5973`
- `market_context_high->index_24h` score `1.9922` n `50` status `ready` deltaP `17.5417` edge `0.2052` maxDD `-1.3389`
- `news_risk_high->crypto_major_1h` score `1.8942` n `50` status `ready` deltaP `12.0419` edge `0.1173` maxDD `-1.1783`
- `market_context_high->index_1h` score `1.8325` n `51` status `ready` deltaP `21.187` edge `0.0253` maxDD `-0.1069`
- `news_risk_high->metal_4h` score `1.6192` n `47` status `ready` deltaP `14.8839` edge `0.0825` maxDD `-0.7433`
- `news_risk_high->crypto_alt_1h` score `1.6113` n `50` status `ready` deltaP `12.0419` edge `0.0974` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.4034` n `47` status `ready` deltaP `16.2753` edge `0.2106` maxDD `-5.8012`
- `market_context_high->fx_24h` score `1.0606` n `50` status `ready` deltaP `21.5278` edge `0.0578` maxDD `-0.5608`
- `news_risk_high->index_1h` score `0.6224` n `50` status `ready` deltaP `8.5988` edge `0.0234` maxDD `-0.3089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
