# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T22:37:28.859661+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4790`

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

- `market_context_high->unknown_1h` score `364.0318` n `50` status `ready` deltaP `10.5749` edge `30.2704` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.5285` n `50` status `ready` deltaP `10.6707` edge `24.2229` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9347` n `72` status `ready` deltaP `42.7083` edge `1.1474` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.5248` n `50` status `ready` deltaP `19.4861` edge `0.9175` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.081` n `50` status `ready` deltaP `31.8264` edge `0.6862` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.6869` n `72` status `ready` deltaP `31.4237` edge `0.5629` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.9494` n `50` status `ready` deltaP `19.8293` edge `0.6006` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.4549` n `50` status `ready` deltaP `18.0183` edge `0.5467` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `6.3779` n `115` status `ready` deltaP `24.54` edge `0.5023` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3873` n `50` status `ready` deltaP `15.4012` edge `0.2459` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1595` n `50` status `ready` deltaP `14.4491` edge `0.212` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7653` n `50` status `ready` deltaP `30.8598` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5501` n `115` status `ready` deltaP `22.0109` edge `0.1312` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `1.8776` n `72` status `ready` deltaP `6.7708` edge `0.4947` maxDD `-14.9292`
- `news_risk_high->crypto_major_4h` score `1.8499` n `115` status `ready` deltaP `17.0467` edge `0.3478` maxDD `-10.2755`
- `market_context_high->fx_1h` score `1.4723` n `50` status `ready` deltaP `20.6407` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.4197` n `72` status `ready` deltaP `13.5417` edge `0.2189` maxDD `-2.1736`
- `market_context_high->equity_24h` score `1.3608` n `50` status `ready` deltaP `6.3681` edge `0.3182` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.2074` n `115` status `ready` deltaP `5.9229` edge `0.1172` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.9699` n `50` status `ready` deltaP `19.9861` edge `0.0929` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
