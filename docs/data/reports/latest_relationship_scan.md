# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T07:52:15.440794+00:00`
- Price records: `627`
- Market context records: `733`
- Flow alert records: `2071`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `12.2929` n `146` status `ready` deltaP `29.4456` edge `0.8615` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4972` n `146` status `ready` deltaP `7.7897` edge `0.4943` maxDD `-0.0508`
- `market_context_high->index_24h` score `-0.0973` n `146` status `ready` deltaP `0.5706` edge `0.1876` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.3243` n `151` status `ready` deltaP `5.5598` edge `0.0085` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.4182` n `156` status `ready` deltaP `3.0829` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5431` n `156` status `ready` deltaP `1.8733` edge `0.0397` maxDD `-3.7959`
- `market_context_high->equity_24h` score `-0.8268` n `146` status `ready` deltaP `-1.1281` edge `0.1991` maxDD `-10.5047`
- `market_context_high->index_1h` score `-0.8916` n `156` status `ready` deltaP `1.1185` edge `0.0036` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-1.0263` n `151` status `ready` deltaP `17.1632` edge `0.1246` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.0584` n `156` status `ready` deltaP `-0.8201` edge `-0.0017` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0946` n `156` status `ready` deltaP `5.3659` edge `-0.0038` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4806` n `156` status `ready` deltaP `3.913` edge `-0.018` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.6265` n `156` status `ready` deltaP `-5.051` edge `-0.0247` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.8499` n `151` status `ready` deltaP `1.1412` edge `-0.0095` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1168` n `151` status `ready` deltaP `2.4409` edge `0.0643` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7776` n `151` status `ready` deltaP `-1.8242` edge `-0.0041` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1841` n `156` status `ready` deltaP `-4.0972` edge `-0.0421` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5902` n `151` status `ready` deltaP `-5.2631` edge `0.086` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9332` n `151` status `ready` deltaP `4.4776` edge `-0.1698` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2954` n `146` status `ready` deltaP `-14.6864` edge `-0.0638` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
