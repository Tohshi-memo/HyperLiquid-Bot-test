# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T05:07:24.847763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11383`

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

- `market_context_high->unknown_24h` score `1188.9965` n `135` status `ready` deltaP `13.9699` edge `98.9951` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.3005` n `82` status `ready` deltaP `-3.7535` edge `32.0089` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `23.7986` n `59` status `ready` deltaP `54.505` edge `1.7099` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `23.7112` n `83` status `ready` deltaP `42.587` edge `1.715` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.7112` n `83` status `ready` deltaP `42.587` edge `1.715` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.9155` n `135` status `ready` deltaP `36.7592` edge `1.4973` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.3254` n `59` status `ready` deltaP `29.967` edge `1.2928` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.1066` n `59` status `ready` deltaP `33.5894` edge `0.7948` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0459` n `83` status `ready` deltaP `36.9792` edge `0.5073` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0459` n `83` status `ready` deltaP `36.9792` edge `0.5073` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7315` n `135` status `ready` deltaP `36.9792` edge `0.4811` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.3383` n `83` status `ready` deltaP `43.5039` edge `0.442` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.3383` n `83` status `ready` deltaP `43.5039` edge `0.442` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1621` n `59` status `ready` deltaP `51.0417` edge `0.3399` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9417` n `59` status `ready` deltaP `51.4713` edge `0.328` maxDD `-0.0797`
- `risk_on_high->crypto_major_24h` score `6.3462` n `83` status `ready` deltaP `21.5257` edge `1.0769` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.3462` n `83` status `ready` deltaP `21.5257` edge `1.0769` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.3168` n `83` status `ready` deltaP `30.295` edge `0.4103` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.3168` n `83` status `ready` deltaP `30.295` edge `0.4103` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.183` n `83` status `ready` deltaP `51.2466` edge `0.0945` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
