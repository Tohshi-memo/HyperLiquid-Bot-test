# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T19:22:26.715117+00:00`
- Price records: `672`
- Market context records: `7060`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.5737` n `189` status `ready` deltaP `16.0207` edge `0.011` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1987` n `189` status `ready` deltaP `3.9683` edge `0.0021` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.288` n `189` status `ready` deltaP `2.2519` edge `0.0345` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5363` n `189` status `ready` deltaP `4.5877` edge `0.0359` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-0.6434` n `189` status `ready` deltaP `-1.1137` edge `0.0233` maxDD `-1.8929`
- `market_context_high->metal_1h` score `-0.7763` n `189` status `ready` deltaP `-3.2016` edge `-0.0014` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.8082` n `189` status `ready` deltaP `-1.3046` edge `-0.0038` maxDD `-2.2895`
- `market_context_high->unknown_4h` score `-1.005` n `189` status `ready` deltaP `-5.4757` edge `0.1162` maxDD `-4.742`
- `market_context_high->commodity_1h` score `-1.3681` n `189` status `ready` deltaP `-5.0059` edge `-0.019` maxDD `-1.9306`
- `market_context_high->equity_1h` score `-1.9248` n `189` status `ready` deltaP `3.6173` edge `-0.0286` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.2696` n `189` status `ready` deltaP `1.3122` edge `-0.0014` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.304` n `189` status `ready` deltaP `1.1428` edge `-0.0331` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4099` n `189` status `ready` deltaP `-2.0916` edge `-0.056` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.5284` n `189` status `ready` deltaP `-7.5098` edge `-0.0446` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.7839` n `189` status `ready` deltaP `1.5647` edge `0.0112` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.9382` n `189` status `ready` deltaP `3.7441` edge `0.0268` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5014` n `189` status `ready` deltaP `0.2894` edge `-0.011` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-3.668` n `189` status `ready` deltaP `-14.5172` edge `0.1412` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.8826` n `189` status `ready` deltaP `4.0126` edge `-0.1503` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.3274` n `189` status `ready` deltaP `-19.2791` edge `-0.0894` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
