# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T09:22:25.837720+00:00`
- Price records: `672`
- Market context records: `5648`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.5956` n `180` status `ready` deltaP `14.4444` edge `0.6279` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.08` n `180` status `ready` deltaP `20.1042` edge `0.0602` maxDD `-1.6714`
- `market_context_high->crypto_major_4h` score `0.67` n `237` status `ready` deltaP `10.2423` edge `0.2168` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4527` n `237` status `ready` deltaP `7.229` edge `0.1534` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.1364` n `237` status `ready` deltaP `5.9169` edge `0.1341` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2623` n `240` status `ready` deltaP `1.9336` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3748` n `240` status `ready` deltaP `5.3793` edge `0.0336` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5639` n `240` status `ready` deltaP `-0.7161` edge `0.0` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6247` n `240` status `ready` deltaP `1.4396` edge `0.0345` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7076` n `240` status `ready` deltaP `3.5679` edge `0.0418` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9412` n `240` status `ready` deltaP `0.4366` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0317` n `240` status `ready` deltaP `-0.6188` edge `-0.0053` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2923` n `237` status `ready` deltaP `1.6755` edge `0.0065` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0221` n `237` status `ready` deltaP `-1.5366` edge `0.0089` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3036` n `180` status `ready` deltaP `10.3125` edge `0.0346` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0607` n `237` status `ready` deltaP `-14.8265` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8032` n `237` status `ready` deltaP `-2.1875` edge `-0.0348` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4922` n `180` status `ready` deltaP `4.1666` edge `0.0519` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3463` n `180` status `ready` deltaP `-12.2917` edge `-0.252` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.0559` n `180` status `ready` deltaP `-16.875` edge `-0.1146` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
