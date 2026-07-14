# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T08:07:24.691893+00:00`
- Price records: `672`
- Market context records: `6690`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->commodity_24h` score `0.6412` n `192` status `ready` deltaP `10.7639` edge `0.1685` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.4776` n `192` status `ready` deltaP `10.1828` edge `0.0579` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `0.3616` n `192` status `ready` deltaP `-1.5625` edge `0.432` maxDD `-12.3511`
- `market_context_high->crypto_alt_1h` score `0.2303` n `192` status `ready` deltaP `6.9018` edge `0.0496` maxDD `-3.7803`
- `market_context_high->unknown_1h` score `-0.1503` n `192` status `ready` deltaP `-5.358` edge `0.1133` maxDD `-3.2083`
- `market_context_high->fx_1h` score `-0.2896` n `192` status `ready` deltaP `1.8151` edge `0.001` maxDD `-0.6845`
- `market_context_high->index_1h` score `-0.4435` n `192` status `ready` deltaP `1.419` edge `0.0051` maxDD `-0.7136`
- `market_context_high->equity_1h` score `-0.4845` n `192` status `ready` deltaP `4.4536` edge `0.0109` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-0.5452` n `192` status `ready` deltaP `-2.8911` edge `0.0019` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.5642` n `192` status `ready` deltaP `0.7173` edge `-0.0088` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.918` n `192` status `ready` deltaP `10.3024` edge `0.0016` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.4004` n `192` status `ready` deltaP `6.3262` edge `-0.0011` maxDD `-3.3157`
- `market_context_high->crypto_major_4h` score `-1.4923` n `192` status `ready` deltaP `8.2698` edge `0.085` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.6477` n `192` status `ready` deltaP `-3.6713` edge `-0.0373` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.7502` n `192` status `ready` deltaP `6.2246` edge `0.0743` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1456` n `192` status `ready` deltaP `-1.4735` edge `0.0208` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.1328` n `192` status `ready` deltaP `-15.9299` edge `0.0857` maxDD `-10.5788`
- `market_context_high->equity_4h` score `-5.1937` n `192` status `ready` deltaP `6.8851` edge `-0.0518` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.4473` n `192` status `ready` deltaP `-10.7639` edge `-0.0071` maxDD `-9.0067`
- `market_context_high->metal_24h` score `-7.0211` n `192` status `ready` deltaP `-6.4236` edge `-0.0088` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
