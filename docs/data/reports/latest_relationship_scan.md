# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T11:22:33.979305+00:00`
- Price records: `672`
- Market context records: `4822`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `12.9882` n `112` status `ready` deltaP `11.7462` edge `1.0458` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.9647` n `112` status `ready` deltaP `17.5305` edge `0.6679` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.855` n `105` status `ready` deltaP `14.7371` edge `0.2112` maxDD `-3.0555`
- `market_context_high->equity_4h` score `0.7377` n `112` status `ready` deltaP `12.0644` edge `0.1523` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.6585` n `112` status `ready` deltaP `9.7125` edge `0.0403` maxDD `-1.0138`
- `market_context_high->commodity_4h` score `0.3693` n `112` status `ready` deltaP `15.0697` edge `0.0641` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.1446` n `112` status `ready` deltaP `5.9773` edge `0.0238` maxDD `-1.4613`
- `market_context_high->equity_1h` score `-0.1166` n `112` status `ready` deltaP `3.2774` edge `0.0248` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.4272` n `112` status `ready` deltaP `3.3101` edge `0.0008` maxDD `-1.5439`
- `market_context_high->index_1h` score `-1.0102` n `112` status `ready` deltaP `-0.3047` edge `0.0012` maxDD `-1.3348`
- `market_context_high->fx_1h` score `-1.0488` n `112` status `ready` deltaP `-2.8122` edge `-0.0037` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-2.1067` n `112` status `ready` deltaP `4.1756` edge `-0.0152` maxDD `-12.7225`
- `market_context_high->metal_1h` score `-2.1967` n `112` status `ready` deltaP `-0.5721` edge `-0.0675` maxDD `-13.4916`
- `market_context_high->crypto_major_1h` score `-2.24` n `112` status `ready` deltaP `2.2562` edge `-0.0447` maxDD `-17.9354`
- `market_context_high->commodity_24h` score `-2.3581` n `105` status `ready` deltaP `18.3383` edge `0.0863` maxDD `-27.5371`
- `market_context_high->fx_24h` score `-2.4057` n `105` status `ready` deltaP `-11.7461` edge `-0.0194` maxDD `-2.8884`
- `market_context_high->crypto_alt_4h` score `-3.7104` n `112` status `ready` deltaP `8.7979` edge `0.0108` maxDD `-38.2779`
- `market_context_high->index_24h` score `-4.076` n `105` status `ready` deltaP `-4.0526` edge `-0.1047` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.2542` n `112` status `ready` deltaP `5.7055` edge `-0.1449` maxDD `-60.5192`
- `market_context_high->metal_4h` score `-8.5883` n `112` status `ready` deltaP `5.9887` edge `-0.3305` maxDD `-60.1721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
