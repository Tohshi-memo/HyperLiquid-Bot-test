# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T21:22:32.850215+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8252`

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

- `market_context_high->unknown_24h` score `705.4593` n `53` status `ready` deltaP `3.9861` edge `58.7617` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.2273` n `50` status `ready` deltaP `50.565` edge `3.5858` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.7105` n `53` status `ready` deltaP `43.6971` edge `3.2554` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.3761` n `53` status `ready` deltaP `61.5088` edge `2.5623` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.6966` n `50` status `ready` deltaP `44.8284` edge `2.7253` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `12.123` n `53` status `ready` deltaP `17.0171` edge `1.4652` maxDD `-40.8051`
- `news_risk_high->equity_4h` score `11.835` n `50` status `ready` deltaP `37.3902` edge `0.85` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.4278` n `50` status `ready` deltaP `20.6031` edge `1.5219` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.0875` n `53` status `ready` deltaP `48.5857` edge `0.3587` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.6683` n `50` status `ready` deltaP `42.2461` edge `0.3044` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.378` n `50` status `ready` deltaP `41.5945` edge `0.2542` maxDD `0.0`
- `market_context_high->metal_24h` score `6.3358` n `53` status `ready` deltaP `61.8947` edge `0.4888` maxDD `-3.7989`
- `market_context_high->unknown_4h` score `5.3899` n `73` status `ready` deltaP `8.9939` edge `0.3892` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.8542` n `50` status `ready` deltaP `43.9268` edge `0.1493` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.7176` n `50` status `ready` deltaP `21.4512` edge `0.3877` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.182` n `50` status `ready` deltaP `26.0793` edge `0.3182` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.8952` n `50` status `ready` deltaP `20.7485` edge `0.2493` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6478` n `50` status `ready` deltaP `33.8293` edge `0.1038` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4286` n `50` status `ready` deltaP `23.4268` edge `0.0812` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1442` n `50` status `ready` deltaP `24.5449` edge `0.0405` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
