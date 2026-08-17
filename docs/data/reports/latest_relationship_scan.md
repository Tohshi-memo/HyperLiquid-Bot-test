# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T00:07:27.259774+00:00`
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

- `market_context_high->unknown_24h` score `76.4001` n `81` status `ready` deltaP `-33.9699` edge `10.2897` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.7528` n `81` status `ready` deltaP `34.0278` edge `0.2041` maxDD `-0.4576`
- `market_context_high->commodity_4h` score `0.9098` n `109` status `ready` deltaP `10.7141` edge `0.0515` maxDD `-0.7687`
- `market_context_high->index_24h` score `-0.1551` n `81` status `ready` deltaP `11.0918` edge `-0.0417` maxDD `-0.6137`
- `market_context_high->metal_4h` score `-0.2013` n `109` status `ready` deltaP `15.4509` edge `0.0119` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.2671` n `112` status `ready` deltaP `1.1762` edge `0.0118` maxDD `-0.6855`
- `market_context_high->fx_1h` score `-0.3657` n `112` status `ready` deltaP `0.7378` edge `0.0011` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.4777` n `112` status `ready` deltaP `2.0744` edge `-0.0035` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.6078` n `109` status `ready` deltaP `1.6978` edge `-0.0015` maxDD `-0.504`
- `market_context_high->index_1h` score `-0.6604` n `112` status `ready` deltaP `-4.6514` edge `-0.0015` maxDD `-0.5064`
- `market_context_high->crypto_major_24h` score `-0.8146` n `81` status `ready` deltaP `-3.6266` edge `0.1469` maxDD `-12.8395`
- `market_context_high->crypto_major_4h` score `-0.847` n `109` status `ready` deltaP `2.446` edge `-0.0041` maxDD `-4.6638`
- `market_context_high->crypto_major_1h` score `-1.1718` n `112` status `ready` deltaP `-4.7637` edge `-0.0201` maxDD `-3.8701`
- `market_context_high->index_4h` score `-1.1879` n `109` status `ready` deltaP `-9.9015` edge `-0.0054` maxDD `-0.8045`
- `market_context_high->crypto_alt_1h` score `-1.6761` n `112` status `ready` deltaP `-4.1702` edge `-0.0097` maxDD `-4.5069`
- `market_context_high->equity_1h` score `-2.4609` n `112` status `ready` deltaP `-9.8695` edge `-0.044` maxDD `-4.289`
- `market_context_high->metal_24h` score `-2.461` n `81` status `ready` deltaP `-14.1783` edge `0.0302` maxDD `-7.0954`
- `market_context_high->fx_24h` score `-2.5575` n `81` status `ready` deltaP `-22.1451` edge `-0.0195` maxDD `-1.8596`
- `market_context_high->equity_24h` score `-3.8555` n `81` status `ready` deltaP `5.382` edge `-0.2423` maxDD `-18.0299`
- `market_context_high->crypto_alt_4h` score `-5.4762` n `109` status `ready` deltaP `-6.8836` edge `-0.0423` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
