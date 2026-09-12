# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T01:22:31.994620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11247`

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

- `news_risk_high->unknown_1h` score `383.2644` n `82` status `ready` deltaP `-3.1547` edge `32.0019` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `25.0711` n `91` status `ready` deltaP `43.1166` edge `1.8248` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `25.0711` n `91` status `ready` deltaP `43.1166` edge `1.8248` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.8377` n `46` status `ready` deltaP `52.589` edge `1.6426` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.9903` n `150` status `ready` deltaP `37.9444` edge `1.6623` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `14.3251` n `46` status `ready` deltaP `24.6981` edge `1.0779` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `11.0027` n `46` status `ready` deltaP `32.6314` edge `0.7092` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.2967` n `91` status `ready` deltaP `36.9792` edge `0.5282` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2967` n `91` status `ready` deltaP `36.9792` edge `0.5282` maxDD `0.0`
- `market_context_high->equity_24h` score `9.0039` n `150` status `ready` deltaP `36.9792` edge `0.5038` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9434` n `91` status `ready` deltaP `43.9276` edge `0.4896` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9434` n `91` status `ready` deltaP `43.9276` edge `0.4896` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.0829` n `46` status `ready` deltaP `51.0417` edge `0.3333` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.8641` n `91` status `ready` deltaP `25.021` edge `1.2482` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.8641` n `91` status `ready` deltaP `25.021` edge `1.2482` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.8375` n `46` status `ready` deltaP `50.5133` edge `0.3257` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.7785` n `91` status `ready` deltaP `31.8966` edge `0.4381` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.7785` n `91` status `ready` deltaP `31.8966` edge `0.4381` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.314` n `91` status `ready` deltaP `51.5644` edge `0.1033` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.314` n `91` status `ready` deltaP `51.5644` edge `0.1033` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
