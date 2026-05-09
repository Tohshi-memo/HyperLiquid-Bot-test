# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T08:37:14.830172+00:00`
- Price records: `672`
- Market context records: `847`
- Flow alert records: `2379`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1332`

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

- `market_context_high->crypto_major_24h` score `11.7866` n `158` status `ready` deltaP `27.5866` edge `0.8317` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.1115` n `158` status `ready` deltaP `7.1796` edge `0.3829` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4784` n `33` status `ready` deltaP `9.733` edge `0.2615` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4784` n `33` status `ready` deltaP `9.733` edge `0.2615` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.5468` n `33` status `ready` deltaP `19.3552` edge `0.1204` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.5468` n `33` status `ready` deltaP `19.3552` edge `0.1204` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.4437` n `33` status `ready` deltaP `13.507` edge `0.1224` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.4437` n `33` status `ready` deltaP `13.507` edge `0.1224` maxDD `-0.038`
- `risk_on_high->crypto_alt_4h` score `2.2666` n `33` status `ready` deltaP `19.5676` edge `0.0789` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.2666` n `33` status `ready` deltaP `19.5676` edge `0.0789` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.1027` n `33` status `ready` deltaP `12.9605` edge `0.0285` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1027` n `33` status `ready` deltaP `12.9605` edge `0.0285` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8327` n `33` status `ready` deltaP `5.5155` edge `0.1531` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8327` n `33` status `ready` deltaP `5.5155` edge `0.1531` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3382` n `33` status `ready` deltaP `8.7371` edge `0.0227` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3382` n `33` status `ready` deltaP `8.7371` edge `0.0227` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2112` n `33` status `ready` deltaP `7.349` edge `0.0016` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2112` n `33` status `ready` deltaP `7.349` edge `0.0016` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.151` n `33` status `ready` deltaP `4.5818` edge `-0.0195` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.151` n `33` status `ready` deltaP `4.5818` edge `-0.0195` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
