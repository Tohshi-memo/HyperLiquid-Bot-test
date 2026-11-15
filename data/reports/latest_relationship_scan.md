# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T09:52:23.406398+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

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

- `market_context_high->unknown_24h` score `533.5389` n `66` status `ready` deltaP `2.4263` edge `44.4454` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.3714` n `50` status `ready` deltaP `48.8319` edge `3.4427` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1403` n `66` status `ready` deltaP `42.6501` edge `3.0482` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.8944` n `66` status `ready` deltaP `57.8121` edge `2.2968` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.7441` n `50` status `ready` deltaP `46.3882` edge `2.8492` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.3491` n `50` status `ready` deltaP `39.6768` edge `0.8776` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.1895` n `50` status `ready` deltaP `16.9636` edge `1.3874` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.522` n `66` status `ready` deltaP `44.9372` edge `0.3364` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.242` n `50` status `ready` deltaP `48.1802` edge `0.2823` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3257` n `50` status `ready` deltaP `40.513` edge `0.2874` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.1802` n `66` status `ready` deltaP `58.332` edge `0.4926` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.6613` n `50` status `ready` deltaP `23.7378` edge `0.4511` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0875` n `50` status `ready` deltaP `46.2134` edge `0.1535` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.0101` n `50` status `ready` deltaP `28.9756` edge `0.3679` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9828` n `50` status `ready` deltaP `21.3473` edge `0.2526` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5186` n `50` status `ready` deltaP `32.3049` edge `0.1032` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `3.0605` n `66` status `ready` deltaP `12.6306` edge `1.2034` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.8046` n `50` status `ready` deltaP `27.5427` edge `0.0851` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3107` n `50` status `ready` deltaP `26.491` edge `0.0414` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2699` n `50` status `ready` deltaP `16.8982` edge `0.0233` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
