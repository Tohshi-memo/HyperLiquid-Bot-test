# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T23:52:28.298784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `85.0352` n `81` status `ready` deltaP `-32.9089` edge `11.3897` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `5.0266` n `81` status `ready` deltaP `35.0888` edge `0.2141` maxDD `-0.3313`
- `market_context_high->commodity_4h` score `0.9902` n `109` status `ready` deltaP `11.4791` edge `0.0531` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.19` n `112` status `ready` deltaP `1.9194` edge `0.0125` maxDD `-0.624`
- `market_context_high->metal_4h` score `-0.2084` n `109` status `ready` deltaP `15.4509` edge `0.011` maxDD `-4.5909`
- `market_context_high->index_24h` score `-0.3203` n `81` status `ready` deltaP `10.0309` edge `-0.0432` maxDD `-0.6957`
- `market_context_high->fx_1h` score `-0.3585` n `112` status `ready` deltaP `0.7378` edge `0.0017` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.4785` n `112` status `ready` deltaP `2.0744` edge `-0.0036` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.537` n `109` status `ready` deltaP `2.4628` edge `-0.0007` maxDD `-0.504`
- `market_context_high->index_1h` score `-0.6597` n `112` status `ready` deltaP `-4.6514` edge `-0.0014` maxDD `-0.5064`
- `market_context_high->crypto_major_4h` score `-0.6737` n `109` status `ready` deltaP `3.211` edge `0.0019` maxDD `-4.1081`
- `market_context_high->crypto_major_24h` score `-0.8929` n `81` status `ready` deltaP `-3.6266` edge `0.1441` maxDD `-13.4187`
- `market_context_high->crypto_alt_1h` score `-1.0832` n `112` status `ready` deltaP `-4.1702` edge `-0.0089` maxDD `-4.5069`
- `market_context_high->crypto_major_1h` score `-1.1656` n `112` status `ready` deltaP `-4.7637` edge `-0.0193` maxDD `-3.8701`
- `market_context_high->index_4h` score `-1.1879` n `109` status `ready` deltaP `-9.9015` edge `-0.0054` maxDD `-0.8045`
- `market_context_high->metal_24h` score `-2.44` n `81` status `ready` deltaP `-14.1783` edge `0.0329` maxDD `-7.0954`
- `market_context_high->equity_1h` score `-2.4609` n `112` status `ready` deltaP `-9.8695` edge `-0.044` maxDD `-4.289`
- `market_context_high->fx_24h` score `-2.4789` n `81` status `ready` deltaP `-21.0841` edge `-0.0165` maxDD `-1.8596`
- `market_context_high->equity_24h` score `-4.305` n `81` status `ready` deltaP `4.321` edge `-0.2654` maxDD `-19.8929`
- `market_context_high->crypto_alt_4h` score `-5.325` n `109` status `ready` deltaP `-6.1185` edge `-0.0348` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
