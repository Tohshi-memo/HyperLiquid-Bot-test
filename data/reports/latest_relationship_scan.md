# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T10:22:29.440515+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11807`

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

- `market_context_high->unknown_24h` score `2988.7815` n `114` status `ready` deltaP `13.697` edge `248.979` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.2489` n `82` status `ready` deltaP `-3.4541` edge `32.0026` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.3986` n `59` status `ready` deltaP `54.505` edge `1.7599` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `21.1969` n `65` status `ready` deltaP `40.9188` edge `1.5166` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.1969` n `65` status `ready` deltaP `40.9188` edge `1.5166` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.852` n `114` status `ready` deltaP `34.576` edge `1.3399` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.6218` n `59` status `ready` deltaP `29.967` edge `1.3175` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.2207` n `59` status `ready` deltaP `33.9366` edge `0.802` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0473` n `65` status `ready` deltaP `37.3264` edge `0.5051` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0473` n `65` status `ready` deltaP `37.3264` edge `0.5051` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7137` n `114` status `ready` deltaP `37.3264` edge `0.4773` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.3595` n `59` status `ready` deltaP `53.2986` edge `0.3413` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.2019` n `65` status `ready` deltaP `42.4742` edge `0.4375` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.2019` n `65` status `ready` deltaP `42.4742` edge `0.4375` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9105` n `59` status `ready` deltaP `51.4713` edge `0.3254` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.0177` n `65` status `ready` deltaP `25.0516` edge `0.337` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0177` n `65` status `ready` deltaP `25.0516` edge `0.337` maxDD `-3.8693`
- `risk_on_high->index_24h` score `4.9793` n `65` status `ready` deltaP `50.2457` edge `0.0842` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9793` n `65` status `ready` deltaP `50.2457` edge `0.0842` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.2136` n `65` status `ready` deltaP `38.6633` edge `0.1027` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
