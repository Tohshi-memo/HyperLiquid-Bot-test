# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T17:37:28.540411+00:00`
- Price records: `672`
- Market context records: `6731`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11736`

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

- `market_context_high->unknown_24h` score `1.3564` n `176` status `ready` deltaP `2.7935` edge `0.5305` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0142` n `176` status `ready` deltaP `8.1009` edge `0.0338` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1172` n `176` status `ready` deltaP `5.3484` edge `0.031` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3392` n `176` status `ready` deltaP `0.6328` edge `0.0008` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.3586` n `176` status `ready` deltaP `7.9704` edge `0.1038` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5983` n `176` status `ready` deltaP `-0.8676` edge `0.0005` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6009` n `176` status `ready` deltaP `0.1463` edge `-0.0097` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6661` n `176` status `ready` deltaP `-4.6918` edge `-0.0016` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.0896` n `176` status `ready` deltaP `3.7051` edge `-0.0128` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.209` n `176` status `ready` deltaP `6.5964` edge `-0.011` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2161` n `176` status `ready` deltaP `7.5388` edge `0.0002` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4956` n `176` status `ready` deltaP `-2.0787` edge `-0.0289` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.9636` n `176` status `ready` deltaP `-7.9239` edge `-0.0207` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.1489` n `176` status `ready` deltaP `6.0976` edge `0.0153` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.3536` n `176` status `ready` deltaP `3.7416` edge `0.0135` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6066` n `176` status `ready` deltaP `-6.3193` edge `-0.006` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.9195` n `176` status `ready` deltaP `5.4462` edge `-0.1119` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-3.9678` n `176` status `ready` deltaP `-17.8493` edge `0.0249` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3599` n `176` status `ready` deltaP `-8.7437` edge `-0.0014` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.6455` n `176` status `ready` deltaP `-9.2961` edge `-0.0697` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
