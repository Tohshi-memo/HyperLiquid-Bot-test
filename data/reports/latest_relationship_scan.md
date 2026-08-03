# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T03:07:28.061634+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `3888.5884` n `50` status `ready` deltaP `22.3819` edge `323.9419` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.0475` n `40` status `ready` deltaP `51.4583` edge `0.8673` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.1786` n `40` status `ready` deltaP `51.3194` edge `0.6022` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `3.2701` n `50` status `ready` deltaP `7.2561` edge `0.3005` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.3524` n `50` status `ready` deltaP `13.1037` edge `0.0634` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.6113` n `44` status `ready` deltaP `8.3703` edge `0.1072` maxDD `-2.7703`
- `news_risk_high->metal_4h` score `0.4745` n `50` status `ready` deltaP `10.4756` edge `0.0261` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `0.3666` n `47` status `ready` deltaP `7.5646` edge `0.034` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.3384` n `44` status `ready` deltaP `16.7544` edge `0.0113` maxDD `-1.3685`
- `market_context_high->crypto_alt_4h` score `0.2526` n `44` status `ready` deltaP `5.1829` edge `0.0884` maxDD `-4.9116`
- `news_risk_high->equity_1h` score `0.1841` n `50` status `ready` deltaP `5.509` edge `0.0609` maxDD `-2.916`
- `news_risk_high->metal_1h` score `0.0563` n `50` status `ready` deltaP `4.503` edge `0.0092` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.0077` n `47` status `ready` deltaP `6.9658` edge `-0.0085` maxDD `-0.7804`
- `news_risk_high->index_1h` score `-0.0107` n `50` status `ready` deltaP `3.6048` edge `0.0069` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0462` n `50` status `ready` deltaP `3.6467` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->crypto_alt_1h` score `-0.1993` n `50` status `ready` deltaP `5.0479` edge `0.009` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `-0.2203` n `50` status `ready` deltaP `6.4817` edge `0.0243` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.2463` n `50` status `ready` deltaP `5.3473` edge `0.0048` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.3419` n `50` status `ready` deltaP `4.2455` edge `-0.0196` maxDD `-1.8694`
- `market_context_high->fx_24h` score `-0.7079` n `40` status `ready` deltaP `0.6597` edge `0.0346` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
