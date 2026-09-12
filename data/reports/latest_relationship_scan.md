# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T09:52:26.102756+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11803`

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

- `market_context_high->unknown_24h` score `2792.6115` n `116` status `ready` deltaP `13.7273` edge `232.6313` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.2441` n `82` status `ready` deltaP `-3.4541` edge `32.0022` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.3758` n `59` status `ready` deltaP `54.505` edge `1.758` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `21.5297` n `67` status `ready` deltaP `41.1484` edge `1.5428` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.5297` n `67` status `ready` deltaP `41.1484` edge `1.5428` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.0922` n `116` status `ready` deltaP `34.818` edge `1.3583` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.6278` n `59` status `ready` deltaP `29.967` edge `1.318` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.2015` n `59` status `ready` deltaP `33.9366` edge `0.8004` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0569` n `67` status `ready` deltaP `37.3264` edge `0.5059` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0569` n `67` status `ready` deltaP `37.3264` edge `0.5059` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7173` n `116` status `ready` deltaP `37.3264` edge `0.4776` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.3281` n `59` status `ready` deltaP `52.9514` edge `0.341` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.1278` n `67` status `ready` deltaP `42.6579` edge `0.4301` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1278` n `67` status `ready` deltaP `42.6579` edge `0.4301` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9105` n `59` status `ready` deltaP `51.4713` edge `0.3254` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.2135` n `67` status `ready` deltaP `25.8782` edge `0.3478` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.2135` n `67` status `ready` deltaP `25.8782` edge `0.3478` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.0071` n `67` status `ready` deltaP `50.3835` edge `0.0856` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0071` n `67` status `ready` deltaP `50.3835` edge `0.0856` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.0899` n `67` status `ready` deltaP `37.5068` edge `0.1001` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
