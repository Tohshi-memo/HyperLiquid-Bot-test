# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T13:52:31.002516+00:00`
- Price records: `672`
- Market context records: `6714`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `market_context_high->unknown_24h` score `1.4648` n `176` status `ready` deltaP `2.7935` edge `0.5444` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0649` n `176` status `ready` deltaP `8.55` edge `0.0373` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0057` n `176` status `ready` deltaP `5.9472` edge `0.0363` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3392` n `176` status `ready` deltaP `0.6328` edge `0.0008` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4978` n `176` status `ready` deltaP `7.9704` edge `0.0922` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5562` n `176` status `ready` deltaP `-0.2688` edge `0.0019` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6562` n `176` status `ready` deltaP `-0.6022` edge `-0.0118` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6724` n `176` status `ready` deltaP `-4.6918` edge `-0.0024` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-0.9432` n `176` status `ready` deltaP `4.0045` edge `-0.0026` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.0426` n `176` status `ready` deltaP `8.7306` edge `-0.0039` maxDD `-5.7046`
- `market_context_high->unknown_1h` score `-1.1235` n `176` status `ready` deltaP `-8.5227` edge `0.0533` maxDD `-3.2083`
- `market_context_high->fx_4h` score `-1.2059` n `176` status `ready` deltaP `7.6913` edge `0.0005` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.7095` n `176` status `ready` deltaP `-4.2129` edge `-0.0421` maxDD `-5.5853`
- `market_context_high->crypto_major_4h` score `-1.9101` n `176` status `ready` deltaP `6.25` edge `0.0449` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0665` n `176` status `ready` deltaP `4.6563` edge `0.0442` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.4455` n `176` status `ready` deltaP `-4.9474` edge `0.0055` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.5814` n `176` status `ready` deltaP `6.8182` edge `-0.0777` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-4.0062` n `176` status `ready` deltaP `-17.8493` edge `0.0217` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.264` n `176` status `ready` deltaP `-7.8756` edge `0.0008` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.117` n `176` status `ready` deltaP `-6.692` edge `-0.0193` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
