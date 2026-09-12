# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T01:37:26.341884+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11225`

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

- `news_risk_high->unknown_1h` score `383.2812` n `82` status `ready` deltaP `-3.1547` edge `32.0033` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `25.1155` n `91` status `ready` deltaP `43.1166` edge `1.8285` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `25.1155` n `91` status `ready` deltaP `43.1166` edge `1.8285` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.9294` n `47` status `ready` deltaP `52.7741` edge `1.649` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.855` n `149` status `ready` deltaP `37.8728` edge `1.6515` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `14.5698` n `47` status `ready` deltaP `25.2068` edge `1.0949` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `11.0617` n `47` status `ready` deltaP `32.7239` edge `0.7135` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.2895` n `91` status `ready` deltaP `36.9792` edge `0.5276` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2895` n `91` status `ready` deltaP `36.9792` edge `0.5276` maxDD `0.0`
- `market_context_high->equity_24h` score `8.9895` n `149` status `ready` deltaP `36.9792` edge `0.5026` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9482` n `91` status `ready` deltaP `43.9276` edge `0.49` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9482` n `91` status `ready` deltaP `43.9276` edge `0.49` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.0817` n `47` status `ready` deltaP `51.0417` edge `0.3332` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.8789` n `91` status `ready` deltaP `25.021` edge `1.2501` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.8789` n `91` status `ready` deltaP `25.021` edge `1.2501` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.8497` n `47` status `ready` deltaP `50.6058` edge `0.3261` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.7845` n `91` status `ready` deltaP `31.8966` edge `0.4386` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.7845` n `91` status `ready` deltaP `31.8966` edge `0.4386` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3092` n `91` status `ready` deltaP `51.5644` edge `0.1029` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3092` n `91` status `ready` deltaP `51.5644` edge `0.1029` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
