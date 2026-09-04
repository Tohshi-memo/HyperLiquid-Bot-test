# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T20:07:26.522750+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10780`

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

- `risk_on_high->unknown_4h` score `19.7046` n `133` status `ready` deltaP `7.9314` edge `1.651` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.7046` n `133` status `ready` deltaP `7.9314` edge `1.651` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4958` n `133` status `ready` deltaP `-2.1015` edge `1.0297` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4958` n `133` status `ready` deltaP `-2.1015` edge `1.0297` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.8606` n `214` status `ready` deltaP `8.9925` edge `0.8313` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.7173` n `217` status `ready` deltaP `-1.1556` edge `0.7972` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.9002` n `46` status `ready` deltaP `19.4973` edge `0.222` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.2045` n `46` status `ready` deltaP `9.4247` edge `0.1692` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.0717` n `46` status `ready` deltaP `12.5604` edge `0.1061` maxDD `-0.042`
- `news_risk_high->equity_1h` score `1.6626` n `46` status `ready` deltaP `16.1286` edge `0.0701` maxDD `-0.7924`
- `news_risk_high->metal_4h` score `1.6375` n `46` status `ready` deltaP `17.1659` edge `0.0483` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.507` n `46` status `ready` deltaP `10.5713` edge `0.0752` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1205` n `46` status `ready` deltaP `14.3973` edge `0.0108` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7017` n `46` status `ready` deltaP `9.0732` edge `0.0173` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.2811` n `46` status `ready` deltaP `10.2532` edge `0.0003` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.1981` n `46` status `ready` deltaP `8.6306` edge `0.0036` maxDD `-0.9036`
- `news_risk_high->crypto_alt_1h` score `0.1592` n `46` status `ready` deltaP `3.7556` edge `0.0185` maxDD `-1.0885`
- `risk_on_high->metal_1h` score `0.0805` n `133` status `ready` deltaP `12.1134` edge `0.0008` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0805` n `133` status `ready` deltaP `12.1134` edge `0.0008` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.057` n `46` status `ready` deltaP `-0.5207` edge `0.04` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
