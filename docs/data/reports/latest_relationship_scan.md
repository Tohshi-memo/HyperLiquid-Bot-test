# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T05:37:25.718883+00:00`
- Price records: `672`
- Market context records: `6786`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11716`

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

- `market_context_high->unknown_24h` score `0.8891` n `176` status `ready` deltaP `-1.1995` edge `0.4972` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0705` n `176` status `ready` deltaP `8.144` edge `0.1384` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2591` n `184` status `ready` deltaP `6.4339` edge `0.0215` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.3878` n `184` status `ready` deltaP `-0.2278` edge `0.0003` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4022` n `184` status `ready` deltaP `3.8109` edge `0.0175` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.657` n `184` status `ready` deltaP `-1.8908` edge `-0.0002` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6814` n `184` status `ready` deltaP `-1.4026` edge `-0.0097` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7299` n `184` status `ready` deltaP `-5.5129` edge `-0.0041` maxDD `-1.2183`
- `market_context_high->equity_1h` score `-1.2614` n `184` status `ready` deltaP `2.3855` edge `-0.0179` maxDD `-3.9165`
- `market_context_high->fx_4h` score `-1.3276` n `176` status `ready` deltaP `5.7096` edge `-0.0019` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.3351` n `176` status `ready` deltaP `5.072` edge `-0.017` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4924` n `176` status `ready` deltaP `-2.9933` edge `-0.0224` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6618` n `184` status `ready` deltaP `-5.9067` edge `-0.009` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.5715` n `176` status `ready` deltaP `-5.4047` edge `-0.0076` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.9308` n `176` status `ready` deltaP `1.9817` edge `-0.0575` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.9889` n `176` status `ready` deltaP `1.3026` edge `-0.0517` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2499` n `176` status `ready` deltaP `-13.8858` edge `0.0583` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.3569` n `176` status `ready` deltaP `1.9402` edge `-0.1446` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4507` n `176` status `ready` deltaP `-9.2645` edge `-0.0055` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.0757` n `176` status `ready` deltaP `-17.6295` edge `-0.1975` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
