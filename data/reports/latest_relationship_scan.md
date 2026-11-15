# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T22:07:31.787279+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8264`

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

- `market_context_high->unknown_24h` score `761.5185` n `50` status `ready` deltaP `3.9861` edge `63.4333` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4121` n `50` status `ready` deltaP `50.565` edge `3.6012` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.1051` n `50` status `ready` deltaP `42.565` edge `3.2125` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.3768` n `50` status `ready` deltaP `60.6031` edge `2.5684` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.4293` n `50` status `ready` deltaP `44.3085` edge `2.6945` maxDD `-6.8139`
- `market_context_high->unknown_4h` score `17.7103` n `70` status `ready` deltaP `8.9939` edge `1.4159` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.9253` n `50` status `ready` deltaP `18.3085` edge `1.5227` maxDD `-34.0782`
- `news_risk_high->equity_4h` score `11.7384` n `50` status `ready` deltaP `36.9329` edge `0.845` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.3256` n `50` status `ready` deltaP `20.6031` edge `1.5088` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.9631` n `50` status `ready` deltaP `48.2461` edge `0.3506` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.6971` n `50` status `ready` deltaP `42.2461` edge `0.3068` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3124` n `50` status `ready` deltaP `41.0745` edge `0.2522` maxDD `0.0`
- `market_context_high->metal_24h` score `6.064` n `50` status `ready` deltaP `60.7626` edge `0.4615` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8686` n `50` status `ready` deltaP `43.9268` edge `0.1505` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.531` n `50` status `ready` deltaP `20.9939` edge `0.3752` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0566` n `50` status `ready` deltaP `25.622` edge `0.3108` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.8305` n `50` status `ready` deltaP `20.2994` edge `0.2469` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.621` n `50` status `ready` deltaP `33.5244` edge `0.1036` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4006` n `50` status `ready` deltaP `23.122` edge `0.0809` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1562` n `50` status `ready` deltaP `24.6946` edge `0.0405` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
