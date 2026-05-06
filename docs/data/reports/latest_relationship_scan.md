# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T20:07:26.706290+00:00`
- Price records: `484`
- Market context records: `576`
- Flow alert records: `1628`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.7664` n `146` status `ready` deltaP `7.3048` edge `0.3533` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9252` n `146` status `ready` deltaP `9.5643` edge `0.2134` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0389` n `146` status `ready` deltaP `10.8054` edge `0.0201` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2781` n `146` status `ready` deltaP `2.6476` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5272` n `146` status `ready` deltaP `2.1469` edge `0.0392` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6967` n `146` status `ready` deltaP `0.0345` edge `-0.0042` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1523` n `146` status `ready` deltaP `-4.0182` edge `-0.0089` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2752` n `146` status `ready` deltaP `4.8003` edge `-0.0068` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3141` n `146` status `ready` deltaP `-2.2764` edge `-0.0133` maxDD `-4.4826`
- `market_context_high->index_24h` score `-1.9034` n `146` status `ready` deltaP `-5.6864` edge `0.0788` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9389` n `146` status `ready` deltaP `3.964` edge `-0.0157` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1818` n `146` status `ready` deltaP `3.1144` edge `0.0544` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1909` n `146` status `ready` deltaP `0.6288` edge `-0.0345` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-3.0229` n `146` status `ready` deltaP `11.234` edge `0.0438` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.2877` n `146` status `ready` deltaP `-3.2505` edge `-0.0371` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.32` n `146` status `ready` deltaP `-4.7603` edge `-0.049` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.507` n `146` status `ready` deltaP `-5.4086` edge `0.0939` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.7824` n `146` status `ready` deltaP `-9.8137` edge `0.0107` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5887` n `146` status `ready` deltaP `-5.0871` edge `-0.0372` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.1596` n `146` status `ready` deltaP `0.8781` edge `-0.248` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
