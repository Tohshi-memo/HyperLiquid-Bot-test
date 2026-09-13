# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T16:07:28.645470+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13440`

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

- `market_context_high->unknown_24h` score `17835.3348` n `56` status `ready` deltaP `10.2093` edge `1486.23` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `8585.1926` n `36` status `ready` deltaP `13.5823` edge `715.3479` maxDD `-0.1252`
- `risk_on_and_context->unknown_24h` score `8585.1926` n `36` status `ready` deltaP `13.5823` edge `715.3479` maxDD `-0.1252`
- `news_risk_high->unknown_1h` score `422.2767` n `82` status `ready` deltaP `-4.9511` edge `35.2649` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.5311` n `82` status `ready` deltaP `35.513` edge `1.3563` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.394` n `82` status `ready` deltaP `38.0236` edge `1.4264` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.79` n `82` status `ready` deltaP `25.5467` edge `0.7402` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.9195` n `82` status `ready` deltaP `49.3187` edge `0.2655` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5912` n `82` status `ready` deltaP `24.5879` edge `0.2641` maxDD `-0.6334`
- `risk_on_high->crypto_alt_24h` score `4.5176` n `36` status `ready` deltaP `16.4751` edge `0.5498` maxDD `-4.7693`
- `risk_on_and_context->crypto_alt_24h` score `4.5176` n `36` status `ready` deltaP `16.4751` edge `0.5498` maxDD `-4.7693`
- `risk_on_high->commodity_24h` score `4.253` n `36` status `ready` deltaP `39.8276` edge `0.0889` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.253` n `36` status `ready` deltaP `39.8276` edge `0.0889` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2254` n `56` status `ready` deltaP `39.8276` edge `0.0866` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.7158` n `56` status `ready` deltaP `11.5148` edge `0.5251` maxDD `-7.3715`
- `market_context_high->metal_24h` score `1.1449` n `56` status `ready` deltaP `13.83` edge `0.1272` maxDD `-1.1428`
- `risk_on_high->index_24h` score `1.0645` n `36` status `ready` deltaP `31.8391` edge `0.0149` maxDD `-3.2548`
- `risk_on_and_context->index_24h` score `1.0645` n `36` status `ready` deltaP `31.8391` edge `0.0149` maxDD `-3.2548`
- `market_context_high->index_24h` score `0.7342` n `56` status `ready` deltaP `31.2438` edge `0.0221` maxDD `-4.568`
- `risk_on_high->metal_24h` score `0.478` n `36` status `ready` deltaP `3.3142` edge `0.1015` maxDD `-0.9846`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
